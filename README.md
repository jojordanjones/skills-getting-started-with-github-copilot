# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey @jojordanjones!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/jojordanjones/skills-getting-started-with-github-copilot/issues/1)

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

## New Feature

This repository now includes a simple web-based tool for transcribing audio files using OpenAI models. After starting the FastAPI app, open `/static/transcribe.html` to upload an audio file and receive a transcript.

### Running the server

1. Install the Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Install `ffmpeg` if you want to transcribe files that are not in one of OpenAI's supported formats (`mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav`, or `webm`). The application uses `pydub` to convert unsupported files, which requires `ffmpeg` to be available on your system.

3. Export your OpenAI API key:

   ```bash
   export OPENAI_API_KEY=your-key-here
   ```

4. Launch the server:

   ```bash
   uvicorn src.app:app --reload
   ```

