# Construction Assistant

A Streamlit-based chatbot assistant for all things construction, powered by the GROQ API.

## Features
- **Chatbot Interface:** Ask questions about construction, building, engineering, and architecture.
- **GROQ API Integration:** Uses the GROQ LLM for accurate, real-time responses.
- **Sidebar Settings:** Enter your GROQ API key and clear chat history easily.
- **Persistent Chat:** Chat history remains after page refresh and is only cleared when you click "Clear Chat."
- **Streaming Responses:** See answers appear in real-time as they are generated.
- **Secure API Key Handling:** API key can be provided via sidebar or loaded from a `.env` file.

## Setup Instructions

1. **Clone the repository** (if needed):
   ```sh
   git clone <your-repo-url>
   cd <project-folder>
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your GROQ API key:**
   - Option 1: Add a `.env` file in the project root with:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Option 2: Enter your API key in the sidebar when running the app.

4. **Run the app:**
   ```sh
   streamlit run app.py
   ```

5. **Usage:**
   - Enter your GROQ API key if prompted.
   - Ask any construction-related question in the chat box.
   - Click "Clear Chat" to erase the chat history.

## Requirements
- Python 3.8+
- See `requirements.txt` for Python dependencies.

## File Overview
- `app.py` — Main Streamlit application.
- `requirements.txt` — Python dependencies.
- `.env` — (Optional) Store your GROQ API key securely.

## License
MIT License

---

**Note:** This assistant is focused on construction topics. For best results, keep your questions related to construction, engineering, architecture, or building.
