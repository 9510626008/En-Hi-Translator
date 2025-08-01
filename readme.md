# 🌐 English ↔ Hindi Translator (FastAPI + Argos Translate)

This is a simple multilingual translation web application built using **FastAPI**, **Jinja2 Templates**, and **Argos Translate**. It allows bidirectional translation between English and Hindi (also supports Gujarati if models are added).

---

## 🚀 Features

- 🔄 Translate text between English and Hindi
- 🌐 Web-based interface using HTML forms
- ⚡ FastAPI backend for lightweight performance
- 🧠 Powered by Argos Translate models (offline capable)
- 📦 Easy to extend with other languages

---

## 🏗️ Project Structure

Translator/
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI entry point
│ ├── translator.py # Translation logic
│ └── download_models.py # One-time translation model setup
│
├── templates/
│ └── index.html # Web UI
│
├── run.py # Starts the FastAPI server
├── requirements.txt # Dependencies
├── .gitignore
└── README.md


---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/En-Hi-Translator.git
cd En-Hi-Translator
2. Create Virtual Environment (Optional but recommended)
python -m venv venv310
# Windows
venv310\Scripts\activate
# Linux/macOS
source venv310/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Download Translation Models
python app/download_models.py
This will download and install:

English → Hindi

Hindi → English

(Optionally) English ↔ Gujarati

5. Run the Application
python run.py

6. Open in Browser
http://127.0.0.1:8000