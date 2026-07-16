from transformers import pipeline


class MeetingSummarizer:

    def __init__(self):

        print("=" * 50)
        print("Loading BART")
        print("=" * 50)

        self.summarizer = pipeline(

            task="summarization",

            model="facebook/bart-large-cnn"

        )

        print("BART Loaded Successfully\n")

    def summarize(

        self,

        text,

        max_length=150,

        min_length=50,

        do_sample=False

    ):

        summary = self.summarizer(

            text,

            max_length=max_length,

            min_length=min_length,

            do_sample=do_sample

        )

        return summary[0]["summary_text"]