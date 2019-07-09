from source.MessagesGetter import MessagesGetter
from source.Handler import Handler


class Main:
    @staticmethod
    def message_getter_starter():
        mgs = MessagesGetter()
        mgs.start()

    @staticmethod
    def handler_starter():
        Handler.events_handler()
