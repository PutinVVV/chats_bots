from abc import ABC, abstractmethod


class Messenger(ABC):
    @abstractmethod
    def sendMessage(self, chat_id: int, text: str, **params) -> dict: ...

    @abstractmethod
    def getUpdates(self, **params) -> dict: ...

    @abstractmethod
    def answerCallbackQuery(self, callback_query_id: str, **params) -> dict: ...

    @abstractmethod
    def deleteMessage(chat_id: int, message_id: int) -> dict: ...
