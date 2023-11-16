from telethon import TelegramClient

# local imports
from config import settings


# import handlers
from handlers import greeting_handler


# Remember to use your own values from my.telegram.org!
api_id = settings.api_id
api_hash = settings.api_hash
session_name = settings.session_name


client = TelegramClient(session_name, api_id, api_hash)


def register_handlers() -> None:
    """
    Registers handlers
    """

    client.add_event_handler(greeting_handler.hello_handler)


register_handlers()

if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
