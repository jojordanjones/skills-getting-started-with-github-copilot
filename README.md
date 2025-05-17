# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey @jojordanjones!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/jojordanjones/skills-getting-started-with-github-copilot/issues/1)

---

© 2025 GitHub • [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) • [MIT License](https://gh.io/mit)

## New Feature

This repository now includes **Tech Joint**, a simple site for hosting tools. The first tool lets you transcribe audio using OpenAI's Whisper model.

### Running Tech Joint

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in the environment:
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```
3. Start the server with Uvicorn:
   ```bash
   uvicorn src.app:app --reload
   ```
4. Open your browser to `http://localhost:8000/static/index.html` to see the tools.

The transcription page will prompt you to upload an audio file and returns the text. The API key is required for this feature to function.
