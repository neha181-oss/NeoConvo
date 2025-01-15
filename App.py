from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from streamlit_mic_recorder import speech_to_text
from gtts.lang import tts_langs
import streamlit as st
from gtts import gTTS
import os

# Initialize session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "audio_files" not in st.session_state:
    st.session_state.audio_files = []

# Define user and bot templates for chat display
user_template = "<div style='color: blue;'><strong>User:</strong> {{MSG}}</div>"
bot_template = "<div style='color: green;'><strong>Bot:</strong> {{MSG}}</div>"

# Sidebar: Language selection
language_mapping = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
}
language = st.sidebar.selectbox("Select Language", list(language_mapping.keys()))
response_lang = language_mapping[language]

# Set up chat template
chat_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            f"You are a helpful AI assistant. Please always respond to user queries in {language}.",
        ),
        ("human", "{human_input}"),
    ]
)

# Load API key securely
try:
    api_key = st.secrets["google_ai"]["AIzaSyBMwS2u5ZCg-6VrHCifNU1ngAi_baaxsxA_key"]  # Requires Streamlit secrets.toml
except KeyError:
    st.error("API key not found. Please configure yoAIzaSyBMwS2u5ZCg-6VrHCifNU1ngAi_baaxsxAur API key in Streamlit secrets.")
    st.stop()

# Initialize the language model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
chain = chat_template | model | StrOutputParser()

# Title and instructions
st.title("🎙️ Multi-Language Voice Chatbot 🤖")
st.subheader(f"General Q/A in {language}")

# Capture voice input
text = speech_to_text(language=response_lang, use_container_width=True, just_once=True, key=f"STT_{language}")

if text:
    st.subheader(f"Recognized {language} Text:")
    st.write(f"**User:** {text}")

    with st.spinner("Fetching Response and Converting Text To Speech..."):
        try:
            # Get AI responses
            res = chain.invoke({"human_input": text})
            st.session_state.conversation_history.append({"role": "user", "content": text})
            st.session_state.conversation_history.append({"role": "bot", "content": res})

            # Generate audio response
            response_audio_file = f"response_audio_{len(st.session_state.audio_files) + 1}.mp3"
            tts = gTTS(text=res, lang=response_lang)
            tts.save(response_audio_file)
            st.session_state.audio_files.append(response_audio_file)
        except Exception as e:
            st.error(f"Error: {e}")

# Display chat history and audio
for i, message in enumerate(st.session_state.conversation_history):
    if message["role"] == "user":
        st.markdown(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
    elif message["role"] == "bot":
        st.markdown(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
        if i // 2 < len(st.session_state.audio_files):  # Avoid index errors
            st.audio(st.session_state.audio_files[i // 2])
