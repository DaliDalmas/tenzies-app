from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/sessions")
def get_sessions():
    pass

@app.post("/session")
def post_session():
    pass

@app.get("/session/{session_id}")
def get_session():
    pass

@app.delete("/session/{session_id}")
def delete_session():
    pass


@app.get("/rolls")
def get_rolls():
    pass

@app.post("/roll")
def post_roll():
    pass

@app.get("/roll/{roll_id}")
def get_roll():
    pass

@app.delete("/roll/{roll_id}")
def delete_roll():
    pass