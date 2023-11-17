import speech_recognition as sr

from utils.format_converter import convert_to_wav_format
from monitoring.main_logging import get_logger

logger = get_logger(__name__)


def turn_voice_to_text(input_path, output_path, speach_lang: str) -> str:
    convert_to_wav_format(str(input_path), str(output_path))

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
            language=speach_lang,
        )
    except Exception as e:
        return str(e)

    # removing audio files
    input_path.unlink()
    output_path.unlink()

    return transcript
