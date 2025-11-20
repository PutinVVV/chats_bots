from bot.domain.messenger import Messenger
from bot.domain.storage import Storage
from bot.interface.keyboards import PIZZA_DRINK_MAPPING, ORDER_KEYBOARD
from bot.handlers.handler import Handler, HandlerStatus


class PizzaDrinksHandler(Handler):
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

        if state != "WAIT_FOR_DRINKS":
            return False

        callback_data = update["callback_query"]["data"]
        return callback_data.startswith("drink_")

    def handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> HandlerStatus:
        telegram_id = update["callback_query"]["from"]["id"]
        callback_data = update["callback_query"]["data"]

        drink = PIZZA_DRINK_MAPPING.get(callback_data)
        order_json["drink"] = drink
        storage.update_user_order_json(telegram_id, order_json)
        storage.update_user_state(telegram_id, "WAIT_FOR_ORDER_APPROVE")

        messenger.answer_callback_query(update["callback_query"]["id"])

        order_summary = (
            "Your order:\n"
            f"- Pizza: {order_json.get('pizza_name', 'Not selected')}\n"
            f"- Size: {order_json.get('pizza_size', 'Not selected')}\n"
            f"- Drink: {order_json.get('drink', 'Not selected')}\n\n"
            "Сonfirm the order?"
        )

        messenger.delete_message(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            message_id=update["callback_query"]["message"]["message_id"],
        )
        messenger.send_message(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            text=order_summary,
            reply_markup=ORDER_KEYBOARD,
        )
        return HandlerStatus.STOP
