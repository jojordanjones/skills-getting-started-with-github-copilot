"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path
import io
import tempfile
from typing import Set
import openai

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """Transcribe an uploaded audio file using OpenAI."""

    # Ensure API key is configured
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")

    openai.api_key = api_key

    ALLOWED_EXTS: Set[str] = {".mp3", ".mp4", ".mpeg", ".mpga", ".m4a", ".wav", ".webm"}

    suffix = Path(file.filename).suffix.lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = Path(tmp.name)

    convert_path = tmp_path
    if suffix not in ALLOWED_EXTS:
        try:
            from pydub import AudioSegment
            audio = AudioSegment.from_file(tmp_path)
            convert_path = tmp_path.with_suffix(".mp3")
            audio.export(convert_path, format="mp3")
        except Exception as exc:
            os.remove(tmp_path)
            raise HTTPException(status_code=400, detail=f"Unsupported file type: {suffix}") from exc
        finally:
            if convert_path != tmp_path:
                os.remove(tmp_path)

    with open(convert_path, "rb") as audio_file:
        try:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    os.remove(convert_path)

    return {"transcript": transcript["text"]}
