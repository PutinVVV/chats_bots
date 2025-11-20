from bot.handlers.database_logger import DatabaseLogger
from bot.handlers.ensure_user_exists import EnsureUserExists
from bot.handlers.handler import Handler
from bot.handlers.message_start import MessageStart
from bot.handlers.pizza_drinks import PizzaDrinksHandler
from bot.handlers.pizza_order import PizzaOrderHandler
from bot.handlers.pizza_selection import PizzaSlectionHandler
from bot.handlers.pizza_size import PizzaSizeHandler


def get_handlers() -> list[Handler]:
    return [
        DatabaseLogger(),
        EnsureUserExists(),
        MessageStart(),
        PizzaSlectionHandler(),
        PizzaSizeHandler(),
        PizzaDrinksHandler(),
        PizzaOrderHandler(),
    ]
