import os


ALLOWED_EXTENSIONS = {

    "mp3",
    "wav",
    "m4a",
    "flac",
    "aac",
    "ogg"

}


def allowed_file(filename):

    return (

        "." in filename

        and

        filename.rsplit(".", 1)[1].lower()

        in ALLOWED_EXTENSIONS

    )


def get_filename(path):

    return os.path.basename(path)