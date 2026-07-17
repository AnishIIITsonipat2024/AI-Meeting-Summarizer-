# 🎙️ AI Meeting Summarizer

An AI-powered web application that automatically transcribes meeting audio into text and generates concise meeting summaries using **OpenAI Whisper** and **Facebook BART**. The application provides an intuitive web interface for uploading audio files and downloading the generated transcript and summary.

---

## 📸 Application Preview

### Home Page

![Home Page](screenshots/home.png)

### Generated Transcript & Summary

![Result](screenshots/output.png)

---

## ✨ Features

- 🎤 Upload meeting audio files
- 📝 Automatic speech-to-text transcription using OpenAI Whisper
- 🤖 AI-generated meeting summaries using Facebook BART
- 📄 View transcript and summary side-by-side
- 📥 Download transcript and summary as text files
- 🌐 Clean and responsive web interface
- 🐳 Dockerized for easy deployment

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### AI & NLP
- OpenAI Whisper
- Hugging Face Transformers
- Facebook BART (`facebook/bart-large-cnn`)

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Docker

---

## 📂 Project Structure

```
AI-Meeting-Summarizer/
│
├── app.py
├── config.py
├── summarizer.py
├── transcribe.py
├── utils/
├── static/
│   ├── css/
│   └── js/
├── templates/
├── uploads/
├── outputs/
├── screenshots/
│   ├── home.png
│   └── result.png
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AnishIIITsonipat2024/AI-Meeting-Summarizer-.git
cd AI-Meeting-Summarizer-
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🐳 Docker

## Build the Docker Image

```bash
docker build -t ai-meeting-summarizer .
```

## Run the Docker Container

```bash
docker run -p 5000:5000 ai-meeting-summarizer
```

Now open:

```
http://localhost:5000
```

---

## 🔄 Workflow

1. Upload a meeting audio file.
2. Whisper converts speech into text.
3. The transcript is processed by Facebook BART.
4. The application generates a concise summary.
5. View and download the transcript and summary.

---

## 📋 Requirements

- Python 3.10+
- pip
- Docker (optional)

---

## 📈 Future Enhancements

- 🎙️ Speaker diarization
- 🌍 Multi-language translation
- 📌 Action item extraction
- 🧠 Named Entity Recognition (NER)
- 😊 Sentiment analysis
- 📄 PDF/DOCX export
- ⚡ Real-time meeting summarization
- ☁️ Cloud deployment (AWS, Azure, GCP)

---

## 👨‍💻 Author

**Anish**

B.Tech CSE, IIIT Sonipat

GitHub: https://github.com/AnishIIITsonipat2024

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
