import os

import whisper
import torch


class MeetingTranscriber:

    def __init__(self, model_name="base"):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        print("=" * 50)
        print("Loading Whisper Model")
        print("=" * 50)

        print("Device :", self.device)

        self.model = whisper.load_model(
            model_name,
            device=self.device
        )

        print("Whisper Loaded Successfully\n")

    def transcribe(self, audio_path):

        if not os.path.exists(audio_path):

            raise FileNotFoundError(
                f"{audio_path} not found."
            )

        result = self.model.transcribe(audio_path)

        return result["text"]

    def transcribe_with_metadata(self, audio_path):

        if not os.path.exists(audio_path):

            raise FileNotFoundError(
                f"{audio_path} not found."
            )

        return self.model.transcribe(audio_path)