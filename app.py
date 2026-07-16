from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from config import *

from models.transcriber import MeetingTranscriber
from models.summarizer import MeetingSummarizer
from models.text_chunker import TextChunker

from utils.file_handler import FileHandler
from utils.helper import allowed_file


app = Flask(__name__)


# Load Models Once

transcriber = MeetingTranscriber(WHISPER_MODEL)

summarizer = MeetingSummarizer()



chunker = TextChunker()

handler = FileHandler(

    UPLOAD_FOLDER,

    TRANSCRIPT_FOLDER,

    SUMMARY_FOLDER

)


@app.route("/")

def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])

def upload():

    if "audio" not in request.files:

        return jsonify({

            "error": "No file uploaded."

        })


    file = request.files["audio"]


    if file.filename == "":

        return jsonify({

            "error": "No file selected."

        })


    if not allowed_file(file.filename):

        return jsonify({

            "error": "Unsupported file format."

        })


    filepath, filename = handler.save_audio(file)


    # Speech To Text

    transcript = transcriber.transcribe(filepath)


    # Split Transcript

    chunks = chunker.split(transcript)


    summaries = []


    for chunk in chunks:

        summary = summarizer.summarize(chunk)

        summaries.append(summary)


    final_summary = "\n".join(summaries)


    transcript_path = handler.save_transcript(

        filename,

        transcript

    )


    summary_path = handler.save_summary(

        filename,

        final_summary

    )


    return jsonify({

        "transcript": transcript,

        "summary": final_summary,

        "transcript_file": transcript_path,

        "summary_file": summary_path

    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)