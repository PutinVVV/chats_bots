import json
import asyncio

from bot.domain.messenger import Messenger
from bot.domain.storage import Storage
from bot.interface.keyboards import PIZZA_NAME_KEYBOARD
from bot.handlers.handler import Handler, HandlerStatus


class PizzaFinish(Handler):
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
        if state != "WHAIT_FOR_APROVE":  
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
        callback_query = update["callback_query"]
        chat_id = callback_query["message"]["chat"]["id"]
        user_id = callback_query["from"]["id"]
        callback_data = callback_query["data"]

        await messenger.answer_callback_query(callback_query["id"])
        await messenger.delete_message(chat_id=chat_id, message_id=callback_query["message"]["message_id"])

        order_actions = {
            "order_confirm": "Confirm order",
            "order_again": "Start again",
        }
        action = order_actions.get(callback_data)

        # Получим актуальный заказ
        current_order = await storage.get_user_order(user_id)
        if current_order:
            order_text = (
                f"Your order confirmed 🍕:\n"
                f"Pizza: {current_order['pizza_name']}\n"
                f"Size: {current_order['pizza_size']}\n"
                f"Drink: {current_order['drink']}"
            )
        else:
            order_text = "No order found."

        if action == "Confirm order":
            await storage.update_user_state(user_id, "ORDER_FINISHED")
            await messenger.send_message(chat_id=chat_id, text=order_text)

        elif action == "Start again":
            await storage.clear_user_state_and_order(user_id) 
            await storage.update_user_state(user_id, "WHAIT_FOR_PIZZA_NAME")
            await asyncio.gather(
                messenger.send_message(
                    chat_id=chat_id,
                    text="Starting over! Please choose pizza name",
                    reply_markup=PIZZA_NAME_KEYBOARD,
                )
            )

        return HandlerStatus.STOP
