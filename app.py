import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(page_title="Construction Assistant", page_icon="🏗️", layout="wide")

# Title
st.title("Construction Assistant")
st.markdown("""
### 🏗️ Welcome to your Construction Knowledge Hub!  
Whether you’re an engineer, architect, builder, or just curious about how the world around us is built, this assistant is here to guide you.  
Ask me anything related to construction, and I’ll help break it down with clarity and precision.  

#### Topics I can help you with:
- 🧱 Construction methods and techniques  
- 🪵 Building materials and their properties  
- 🏛️ Structural engineering and design  
- 📐 Architecture and blueprints  
- 🦺 Safety regulations and protocols  
- 🚜 Construction equipment and tools  
- 📊 Project management in construction  
""")


def clear_current_chat():
    """Clear current chat session"""
    st.session_state.messages = []
    st.rerun()

# Initialize session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for API key and clear chat
with st.sidebar:
    st.header("Settings")
    groq_api_key = st.text_input("Enter your GROQ API Key:", type="password")
    st.markdown("Get your API key from [GROQ Console](https://console.groq.com/keys)")
    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        clear_current_chat()

# Load API key from .env if not entered in sidebar
if not groq_api_key:
    groq_api_key = os.getenv("GROQ_API_KEY")

# Check if API key is provided
if not groq_api_key:
    st.warning("Please enter your GROQ API key in the sidebar or set it in a .env file to start chatting.")
    st.stop()

# Initialize GROQ client
try:
    client = Groq(api_key=groq_api_key)
except Exception as e:
    st.error(f"Error initializing GROQ client: {e}")
    st.stop()

# System prompt for construction-focused responses
CONSTRUCTION_PROMPT = """You are a construction industry expert assistant. You ONLY answer questions related to:
- Construction methods and techniques
- Building materials and their properties
- Structural engineering and design
- Architecture and blueprints
- Safety regulations and protocols
- Construction equipment and tools
- Project management in construction
- Building codes and standards
- Cost estimation and budgeting
- Sustainable and green construction

If a user asks about topics unrelated to construction, politely redirect them to construction-related topics. Keep responses professional, accurate, and helpful."""

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask about construction, building, materials, etc."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Prepare messages for GROQ API
                messages = [{"role": "system", "content": CONSTRUCTION_PROMPT}]
                messages.extend(st.session_state.messages)

                # Call GROQ API (streaming response)
                response_stream = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=messages,
                    temperature=1,
                    max_completion_tokens=8192,
                    top_p=1,
                    reasoning_effort="medium",
                    stream=True,
                    stop=None,
                )

                # Collect streamed response content
                assistant_response = ""
                response_placeholder = st.empty()

                for chunk in response_stream:
                    content_piece = getattr(chunk.choices[0].delta, "content", "")
                    assistant_response += content_piece or ""
                    response_placeholder.write(assistant_response)

                # Add assistant response to chat
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

            except Exception as e:
                st.error(f"Error generating response: {e}")
                # Remove the user message if there was an error
                if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
                    st.session_state.messages.pop()

# Footer
st.markdown("---")