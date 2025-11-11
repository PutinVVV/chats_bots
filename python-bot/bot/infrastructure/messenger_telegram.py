import json
import os
import urllib
from dotenv import load_dotenv

from bot.domain.messenger import Messenger

load_dotenv()


class MessengerTelegram(Messenger):
    def _get_telegram_base_uri(self) -> str:
        return f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BASE_URI')}"

    def _get_telegram_file_uri(self) -> str:
        return f"https://api.telegram.org/file/bot{os.getenv('TELEGRAM_BASE_URI')}"

    def _make_request(self, method: str, **param) -> dict:
        json_data = json.dumps(param).encode("utf-8")
        request = urllib.request.Request(
            url=f"{self._get_telegram_base_uri()}/{method}",
            data=json_data,
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")
            response_json = json.loads(response_body)
            assert response_json["ok"]
            return response_json["result"]

    def send_message(self, chat_id: int, text: str, **params) -> dict:
        return self._make_request("sendMessage", chat_id=chat_id, text=text, **params)

    def get_updates(self, **params) -> dict:
        return self._make_request("getUpdates", **params)

    def delete_message(self, chat_id: int, message_id: int) -> dict:
        return self._make_request(
            "deleteMessage",
            chat_id=chat_id,
            message_id=message_id,
        )

    def answer_callback_query(self, callback_query_id: str, **params) -> dict:
        return self._make_request(
            "answerCallbackQuery",
            callback_query_id=callback_query_id,
            **params,
        )
