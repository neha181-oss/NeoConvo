# NeoConvo: Multi-Language Voice Chatbot with RAG

**NeoConvo** is a cutting-edge, multi-language voice chatbot powered by **Retrieval-Augmented Generation (RAG)** technology. It facilitates real-time, context-aware conversations in several languages, such as English, Hindi, Telugu, and Tamil. The chatbot uses speech-to-text for input and generates responses in text and speech, providing a seamless user experience.

## Features

- **Multi-language Support**: Choose from a variety of languages including English, Hindi, Telugu, and Tamil.
- **Speech-to-Text**: Converts user speech into text for a natural conversation flow.
- **Text-to-Speech**: Generates audio responses to ensure a fully interactive voice experience.
- **Context-Aware Responses**: Utilizes **Retrieval-Augmented Generation (RAG)** for more accurate and relevant responses.
- **Google Generative AI**: Leverages Google’s advanced AI model for generating human-like text responses.

## Requirements

- **Streamlit**: For building the interactive web interface.
- **Langchain**: For connecting with AI models and templates.
- **Google Text-to-Speech (gTTS)**: To generate spoken responses.
- **Speech-to-Text**: For voice input.
- **API Key**: Secure API key for Google AI integration (requires `secrets.toml` in Streamlit).

## Usage

1. Select the desired language from the sidebar.
2. Speak into the microphone to input your query.
3. The chatbot will process your input, fetch a response, and provide both a text answer and an audio response.
4. Continue the conversation with multiple queries, which will be stored in the chat history.

## Acknowledgments

- **Streamlit** for easy and quick web app development.
- **Google AI** for the powerful generative language model.
- **Langchain** for integrating AI models with prompts.
