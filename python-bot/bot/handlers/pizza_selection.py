import asyncio

from bot.domain.messenger import Messenger
from bot.domain.storage import Storage
from bot.interface.keyboards import PIZZA_NAME_MAPPING, PIZZA_SIZE_KEYBOARD
from bot.handlers.handler import Handler, HandlerStatus


class PizzaSlectionHandler(Handler):
    def can_handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> bool:
        if "callback_query" not in update:
            return False

        if state != "WAIT_FOR_PIZZA_NAME":
            return False

        callback_data = update["callback_query"]["data"]
        return callback_data.startswith("pizza_")

    async def handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> HandlerStatus:
        telegram_id = update["callback_query"]["from"]["id"]
        callback_data = update["callback_query"]["data"]
        chat_id = update["callback_query"]["message"]["chat"]["id"]
        message_id = update["callback_query"]["message"]["message_id"]
        callback_query_id = update["callback_query"]["id"]
        pizza_name = PIZZA_NAME_MAPPING.get(callback_data)

        await asyncio.gather(
            storage.update_user_order_json(telegram_id, {"pizza_name": pizza_name}),
            storage.update_user_state(telegram_id, "WAIT_FOR_PIZZA_SIZE"),
            messenger.answer_callback_query(callback_query_id),
        )
        await asyncio.gather(
            messenger.delete_message(
                chat_id=chat_id,
                message_id=message_id,
            ),
            messenger.send_message(
                chat_id=chat_id,
                text="Please select pizza size",
                reply_markup=PIZZA_SIZE_KEYBOARD,
            ),
        )
        return HandlerStatus.STOP
