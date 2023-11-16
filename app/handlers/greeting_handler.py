from telethon import events
from telethon.types import Message
from telethon import TelegramClient



@events.register(events.NewMessage(incoming=True))
async def hello_handler(event) -> None:
    """
    Reply to incoming 'hello' and 'hi'
    """

    client: TelegramClient = event.client
    message: Message = event.message

    if message.text == "hello" or message.text == "hi":
        await message.reply('hi there!')
    

