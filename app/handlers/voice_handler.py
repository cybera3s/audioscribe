from telethon import events
from telethon.types import Message, User, Channel

# from telethon import TelegramClient
from pathlib import Path

from utils.voice_to_text import turn_voice_to_text
from config import settings
from monitoring.main_logging import get_logger


logger = get_logger(__name__)


def is_voice_message(message: Message) -> bool:
    """True if message is voice message"""
    return message.media and message.file.mime_type.startswith("audio")


@events.register(events.NewMessage(outgoing=True))
async def handle_outgoing_voices(event) -> None:
    """
    This function handles outgoing voice messages
    turn them to text
    then add to the text as caption to the message
    """

    message: Message = event.message

    outgoing_input_voice: Path = settings.outgoing_voices_path.joinpath(
        "out_voice.oga"
    )
    outgoing_output_voice: Path = settings.outgoing_voices_path.joinpath(
        "out_voice"
    )

    # message is audio
    if is_voice_message(message):
        logger.info("outgoing voice sent")
        sender = await event.get_sender()
        first_name = sender.first_name

        # download voice
        await message.download_media(outgoing_input_voice)

        transcript: str = turn_voice_to_text(
            outgoing_input_voice, outgoing_output_voice, settings.speach_lang
        )

        edited_caption: str = f"**{first_name}**:\n" + transcript
        await message.edit(edited_caption)


@events.register(events.MessageEdited(incoming=True))
async def handle_incoming_voices(event) -> None:
    """
    This handles incoming voice messages
    if you like them
    then turn voice to text
    and send the text as a reply to the voice message
    """

    message: Message = event.message

    confirm_emoji: str = settings.CONFIRM_EMOJI

    incoming_input_voice: Path = settings.incoming_voices_path.joinpath(
        "in_voice.oga"
    )
    incoming_output_voice: Path = settings.incoming_voices_path.joinpath(
        "in_voice"
    )

    sender = await event.get_sender()

    # message is audio
    if is_voice_message(message):
        logger.info("incoming voice message received")

        # message has reactions
        if message.reactions.results:
            # get first reacioned emoji
            reacted_emoji: str = message.reactions.results[0].reaction.emoticon

            if reacted_emoji == confirm_emoji:
                first_name: str = "said"

                # change first name base sender type
                if isinstance(sender, User):
                    first_name: str | None = sender.first_name
                elif isinstance(sender, Channel):
                    first_name: str = sender.title

                await message.download_media(incoming_input_voice)

                transcript: str = turn_voice_to_text(
                    incoming_input_voice,
                    incoming_output_voice,
                    settings.speach_lang,
                )
                edited_caption: str = f"**{first_name}**:\n" + transcript
                await message.reply(edited_caption)
