from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal1, engine

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal1()
    try:
        yield db
    finally:
        db.close()


@app.get("/sessions/", response_model=list[schemas.ReadRollSession], tags=["sessions"])
def get_sessions(skip: int = 0, limit: int =100, db: Session = Depends(get_db)):
    return crud.get_roll_sessions(db=db, skip=skip, limit=limit)

@app.post("/sessions/", response_model=schemas.ReadRollSession, tags=["sessions"])
def post_session(roll_session: schemas.CreateRollSession, db: Session = Depends(get_db)):
    print("they called me")
    return crud.create_roll_session(db=db, roll_session=roll_session)

@app.get("/session/{session_id}", response_model=schemas.ReadRollSession, tags=["sessions"])
def get_session(session_id: int, db: Session = Depends(get_db)):
    db_roll_session = crud.get_roll_session(db=db, roll_session_id=session_id)
    if db_roll_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return db_roll_session



@app.get("/rolls/", response_model=list[schemas.ReadRoll], tags=["rolls"])
def get_rolls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_rolls(db=db, skip=skip, limit=limit)

@app.post("/roll/", response_model=schemas.ReadRoll, tags=["rolls"])
def post_roll(roll: schemas.CreateRoll, session_id:int, db: Session = Depends(get_db)):
    return crud.create_roll(db = db, roll=roll, roll_session_id=session_id)

@app.get("/roll/{roll_id}", response_model=schemas.ReadRoll, tags=["rolls"])
def get_roll(roll_id: int, db: Session = Depends(get_db)):
    roll = crud.get_roll(db=db, roll_id=roll_id)
    if roll is None:
        return HTTPException(status_code=404, detail="roll does not exist")
    return roll
