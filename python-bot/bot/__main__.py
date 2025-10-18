from bot.dispatcher import Dispatcher
from bot.handlers.database_logger import DatabaseLogger
from bot.handlers.message_echo import MessageEcho
from bot.handlers.message_photo_echo import MessagePhotoEcho
from bot.long_polling import start_long_polling

if __name__ == "__main__":
    try:
        dispatcher = Dispatcher()
        dispatcher.add_handlers(DatabaseLogger(), MessageEcho(), MessagePhotoEcho())
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("\nBye!")