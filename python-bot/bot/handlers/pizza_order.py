import asyncio

from bot.domain.messenger import Messenger
from bot.domain.storage import Storage
from bot.handlers.handler import Handler, HandlerStatus


class PizzaOrderHandler(Handler):
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

        if state != "WAIT_FOR_ORDER_APPROVE":
            return False

        callback_data = update["callback_query"]["data"]
        return callback_data.startswith("order_")

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

        """depending on the response, it was possible to accept different states for further processing
        then this handler returns CONTINUE, and add handlers to those different states
        which will be after him in the __init__"""
        if callback_data == "order_ok":
            order_summary = (
                "Order accepted!\n"
                f"- Pizza: {order_json.get('pizza_name', 'Not selected')}\n"
                f"- Size: {order_json.get('pizza_size', 'Not selected')}\n"
                f"- Drink: {order_json.get('drink', 'Not selected')}\n\n"
                "To re-order, press /start"
            )
        else:
            order_summary = "The order was not accepted!\n\nTo re-order, press /start"

        await asyncio.gather(
            messenger.answer_callback_query(callback_query_id),
            storage.update_user_state(telegram_id, "ORDER_FINISHED"),
            messenger.delete_message(chat_id=chat_id, message_id=message_id),
            messenger.send_message(
                chat_id=chat_id,
                text=order_summary,
            ),
        )
        return HandlerStatus.STOP
        