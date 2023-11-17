import speech_recognition as sr
from speech_recognition import RequestError

from utils.format_converter import convert_to_wav_format
from monitoring.main_logging import get_logger

logger = get_logger(__name__)


def turn_voice_to_text(
    input_path, output_path, speach_lang: str, duration: int = 60
) -> str:
    """
    Convert voice to text
    """

    # convert voice to wav format
    convert_to_wav_format(str(input_path), str(output_path))

    error_message: str = ""

    # Recognizing Voice
    recognizer = sr.Recognizer()
    audioFile = sr.AudioFile(str(output_path))

    with audioFile as source:
        recognizer.adjust_for_ambient_noise(source)
        data = recognizer.record(source, duration=duration)

    # recognizing voice using Google API
    try:
        transcript = recognizer.recognize_google(
            data,
            key=None,
            language=speach_lang,
        )

    # internet problem or key error
    except RequestError as e:
        logger.error(f"Error with internet or key\n" f"{str(e)}")

        error_message = "Error happened when converting"
        return error_message

    except Exception as e:
        logger.error(f"Error happened\n" f"{str(e)}")

        error_message = "Error happened when converting"
        return error_message

    # removing audio files
    input_path.unlink()
    output_path.unlink()

    return transcript
