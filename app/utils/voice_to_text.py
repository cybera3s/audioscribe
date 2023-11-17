import speech_recognition as sr

from utils.format_converter import convert_to_wav_format


def voice_to_text(input_path, output_path, lang: str) -> str:
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
            language=lang,
        )
    except Exception as e:
        return str(e)

    # removing audio files
    input_path.unlink()
    output_path.unlink()

    return transcript
