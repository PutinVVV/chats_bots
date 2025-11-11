import json

PIZZA_NAME_KEYBOARD = json.dumps(
    {
        "inline_keyboard": [
            [
                {"text": "Margarita", "callback_data": "pizza_margherita"},
                {"text": "Pepperoni", "callback_data": "pizza_pepperoni"},
            ],
            [
                {"text": "4 Cheese", "callback_data": "pizza_4cheese"},
                {"text": "Bavarian", "callback_data": "pizza_bavarian"},
            ],
            [
                {"text": "Diablo", "callback_data": "pizza_diablo"},
                {"text": "Venetsia", "callback_data": "pizza_venetsia"},
            ],
        ],
    },
)

PIZZA_SIZE_KEYBOARD = json.dumps(
    {
        "inline_keyboard": [
            [
                {"text": "Small (25cm)", "callback_data": "size_small"},
                {"text": "Medium (30cm)", "callback_data": "size_medium"},
            ],
            [
                {"text": "Large (35cm)", "callback_data": "size_large"},
            ],
        ],
    },
)

PIZZA_DRINKS_KEYBOARD = json.dumps(
    {
        "inline_keyboard": [
            [
                {"text": "Coca-Cola", "callback_data": "drink_coca_cola"},
                {"text": "Coca-Cola zero", "callback_data": "drink_pepsi"},
            ],
            [
                {"text": "Lipton green tea", "callback_data": "drink_orange_juice"},
                {"text": "Lipton black tea", "callback_data": "drink_apple_juice"},
            ],
            [
                {"text": "Latte", "callback_data": "drink_water"},
                {"text": "Americano", "callback_data": "drink_iced_tea"},
            ],
            [
                {"text": "No drinks", "callback_data": "drink_none"},
            ],
        ],
    },
)

ORDER_KEYBOARD = json.dumps(
    {
        "inline_keyboard": [
            [
                {"text": "Confirm", "callback_data": "order_ok"},
            ],
            [
                {"text": "Start again", "callback_data": "order_restart"},
            ],
        ],
    },
)

PIZZA_NAME_MAPPING = {
    "pizza_margherita": "Margarita",
    "pizza_pepperoni": "Pepperoni",
    "pizza_4cheese": "4 Cheese",
    "pizza_bavarian": "Bavarian",
    "pizza_diablo": "Diablo",
    "pizza_venetsia": "Venetsia",
}

PIZZA_SIZE_MAPPING = {
    "size_small": "Small (25cm)",
    "size_medium": "Medium (30cm)",
    "size_large": "Large (35cm)",
}

PIZZA_DRINK_MAPPING = {
    "drink_coca_cola": "Coca-Cola",
    "drink_pepsi": "Coca-Cola zero",
    "drink_orange_juice": "Lipton green tea",
    "drink_apple_juice": "Lipton black tea",
    "drink_water": "Latte",
    "drink_iced_tea": "Americano",
    "drink_none": "No drinks",
}