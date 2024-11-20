# Maya: Your Personal Virtual Assistant

Maya is a voice-activated personal assistant powered by Python. It combines advanced speech recognition, OpenAI's capabilities, and various APIs to assist with tasks like browsing, fetching news, playing music, and more.

---

## Features

1. **Voice Activation**: Initiates upon hearing the wake word `Maya`.
2. **Web Browsing**: Quickly opens popular websites like Google, YouTube, Facebook, and Instagram.
3. **News Updates**: Retrieves the latest headlines using the News API.
4. **Music Playback**: Plays specific songs based on voice commands.
5. **AI-Powered Assistance**: Leverages OpenAI to process and respond to user queries.
6. **Text-to-Speech**: Responds using dynamic voice synthesis with GTTS and Pyttsx3.

---

## How It Works

1. **Wake Word**: Start the assistant by saying "Maya."
2. **Command Recognition**: Provide commands after activation. Maya processes these using:
   - Hardcoded logic for predefined commands (e.g., "open Google").
   - OpenAI's API for general queries.
3. **Response Delivery**: Maya speaks responses using GTTS or plays music/news as requested.

---

## Requirements

- **Python Libraries**:
  - `speech_recognition`
  - `webbrowser`
  - `pyttsx3`
  - `requests`
  - `openai`
  - `pygame`
  - `gTTS`
- **APIs**:
  - News API: [Get your API key](https://newsapi.org/register).
  - OpenAI API: [Sign up for access](https://platform.openai.com/signup/).

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/maya-virtual-assistant.git
   cd maya-virtual-assistant
