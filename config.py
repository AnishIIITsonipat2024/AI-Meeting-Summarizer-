import os

# ===========================
# Project Directories
# ===========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

TRANSCRIPT_FOLDER = os.path.join(
    BASE_DIR,
    "outputs",
    "transcripts"
)

SUMMARY_FOLDER = os.path.join(
    BASE_DIR,
    "outputs",
    "summaries"
)

WHISPER_MODEL = "base"

SUMMARY_MODEL = "facebook/bart-large-cnn"

MAX_SUMMARY_LENGTH = 150

MIN_SUMMARY_LENGTH = 50