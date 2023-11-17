import ffmpeg
from monitoring.main_logging import get_logger


logger = get_logger(__name__)


def convert_to_wav_format(input, output) -> bool:
    """
    Converts input file to wav format

    Return:
        True if has no err else False
    """

    stream = ffmpeg.input(input)
    stream = ffmpeg.output(stream, output, format="wav")
    out, err = ffmpeg.run(stream, capture_stdout=True, overwrite_output=True)

    if not err:
        return True
    else:
        logger.error(err)
        return False
