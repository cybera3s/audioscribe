from telethon import events
from telethon.types import Message, User, Channel
# from telethon import TelegramClient

import ffmpeg
import speech_recognition as sr
from pathlib import Path

LANG: str = "fa"
AUDIO_FOLDER = Path("")


def convert_to(input, output) -> bool:
    """
    Converts input file to provided output format

    Return:
        True if has no err else False
    """

    stream = ffmpeg.input(input)
    stream = ffmpeg.output(stream, output)
    out, err = ffmpeg.run(stream)

    if not err:
        return True
    return False


def voice_to_text(input_path, output_path) -> str:
    convert_to(str(input_path), str(output_path))

    # Recognizing Voice
    recognizer = sr.Recognizer()
    audioFile = sr.AudioFile(str(output_path))

    with audioFile as source:
        data = recognizer.record(source)

    # recognizing voice using Google API
    try:
        transcript = recognizer.recognize_google(
            data,
            key=None,
            language=LANG,
        )
    except Exception as e:
        return str(e)

    # removing audio files
    input_path.unlink()
    output_path.unlink()

    return transcript


@events.register(events.NewMessage(outgoing=True))
async def handle_outgoing_voices(event) -> None:
    """
    handle outgoing voices
    """

    message: Message = event.message

    input_voice = "saved_voice"
    input_path = Path(input_voice + ".oga")

    output_voice = "voice_output.wav"
    output_path = Path(output_voice)

    # message is audio
    if message.media and message.file.mime_type.startswith("audio"):
        sender = await event.get_sender()
        first_name = sender.first_name
        await message.download_media(input_voice)

        transcript: str = voice_to_text(input_path, output_path)

        edited_caption: str = f"**{first_name}**:\n" + transcript
        await message.edit(edited_caption)


@events.register(events.MessageEdited(incoming=True))
async def handle_incoming_voices(event) -> None:
    """
    handles incoming voices
    if like them
    convert
    """

    message: Message = event.message

    accepted_emoji: str = "👍"

    input_voice = "incoming/saved_voice"
    input_path = Path(input_voice + ".oga")

    output_voice = "incoming/voice_output.wav"
    output_path = Path(output_voice)

    sender = await event.get_sender()

    # message is audio
    if message.media and message.file.mime_type.startswith("audio"):
        if message.reactions.results:
            reacted_emoji: str = message.reactions.results[0].reaction.emoticon

            if reacted_emoji == accepted_emoji:
                first_name: str = "said"

                # get sender if is user
                if isinstance(sender, User):
                    first_name: str | None = sender.first_name
                elif isinstance(sender, Channel):
                    first_name: str = sender.title

                await message.download_media(input_voice)

                transcript: str = voice_to_text(input_path, output_path)
                edited_caption: str = f"**{first_name}**:\n" + transcript
                await message.reply(edited_caption)
