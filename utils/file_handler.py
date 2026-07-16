import os
from werkzeug.utils import secure_filename


class FileHandler:

    def __init__(self,
                 upload_folder,
                 transcript_folder,
                 summary_folder):

        self.upload_folder = upload_folder
        self.transcript_folder = transcript_folder
        self.summary_folder = summary_folder

        os.makedirs(upload_folder, exist_ok=True)
        os.makedirs(transcript_folder, exist_ok=True)
        os.makedirs(summary_folder, exist_ok=True)

    def save_audio(self, file):

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            self.upload_folder,
            filename
        )

        file.save(filepath)

        return filepath, filename

    def save_transcript(self, filename, transcript):

        txt_name = os.path.splitext(filename)[0] + ".txt"

        path = os.path.join(
            self.transcript_folder,
            txt_name
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(transcript)

        return path

    def save_summary(self, filename, summary):

        txt_name = (
            os.path.splitext(filename)[0]
            + "_summary.txt"
        )

        path = os.path.join(
            self.summary_folder,
            txt_name
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(summary)

        return path