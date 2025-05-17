# Tech Joint

A simple demo web application for uploading audio files and transcribing them with OpenAI's Whisper model.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install [ffmpeg](https://ffmpeg.org/) for audio conversion. On Ubuntu you can run:
   ```bash
   sudo apt-get update && sudo apt-get install ffmpeg
   ```
3. Export your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=YOUR_KEY_HERE
   ```
4. Start the application:
   ```bash
   uvicorn src.app:app --reload
   ```

Open [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html) in your browser.
Use the microphone icon under **Tools** to access the transcription page.

## Features

- Landing page shows available activities and a tools section.
- Audio transcription tool converts unsupported types to MP3 before sending to OpenAI.
