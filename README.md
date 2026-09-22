# 🤖 AI Chatbot with Memory

A stateful conversational AI chatbot built with Google's **Gemini API**, featuring persistent conversation memory, a clean web UI, and a modular architecture. Built as **Project 1** for the DecodeLabs Generative AI Industrial Training Kit.

## ✨ Features

- **Contextual Memory** — Remembers previous messages within a session using an in-memory conversation array
- **Sliding Window Management** — Automatically prunes older messages (FIFO) to stay within the model's token budget
- **Two Interfaces**:
  - 🖥️ Terminal chat (`chatbot_gemini_memory.py`)
  - 🌐 Web UI built with Streamlit (`chatbot_ui.py`)
- **Custom Personality** — Configurable system instruction shapes the bot's tone
- **Persistent Chat History** — Terminal version saves/loads conversations to a local JSON file
- **Streaming Responses** — Web UI shows replies word-by-word, like a live typing effect
- **Multiple Chat Sessions** — Start and switch between separate conversations in the web UI
- **File Upload Support** — Attach an image or PDF and ask the bot about it (web UI)
- **Shared Backend Architecture** — Both interfaces import their logic from a single `bot_engine.py` module, avoiding code duplication

## 🏗️ Project Structure

```
├── bot_engine.py               # Core logic: API calls, memory, save/load, streaming
├── chatbot_gemini_memory.py    # Terminal interface
├── chatbot_ui.py                # Streamlit web interface
├── requirements.txt             # Python dependencies
├── .gitignore                   # Excludes .env, .venv, cache files
└── .env                          # API key (not committed — create this yourself)
```

## 🛠️ Tech Stack

- **Python 3.11+**
- **Google Gemini API** (`google-genai` SDK)
- **Streamlit** (web UI)
- **python-dotenv** (environment variable management)

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\Activate      # Windows
source .venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
Get a free key from [Google AI Studio](https://aistudio.google.com/apikey), then create a `.env` file in the project root:
```
GOOGLE_API_KEY=your-api-key-here
```

### 5. Run it

**Terminal version:**
```bash
python chatbot_gemini_memory.py
```

**Web UI version:**
```bash
streamlit run chatbot_ui.py
```

## 📸 Preview

*(Add a screenshot of the Streamlit UI here once you have one — drag an image into this README on GitHub and it will generate the markdown for you.)*

## 🎯 What This Project Demonstrates

This project was built to practice core concepts in generative AI engineering:
- Transforming a stateless LLM API into a stateful, contextual conversation
- Structured message payloads (role/content objects)
- Session state management
- Token budget awareness and sliding-window truncation
- Clean separation between business logic and presentation layer

## 📄 License

This project is open source and available for learning purposes.

## 🙋 Author

Built as part of the DecodeLabs Industrial Training Kit (Batch 2026).
