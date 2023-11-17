import ffmpeg


def convert_to_wav_format(input, output) -> bool:
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
