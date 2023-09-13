from sqlalchemy.orm import Session

import models, schemas

def get_roll_session(db: Session, roll_session_id: str):
    return db.query(models.RollSession).filter(models.RollSession.id==roll_session_id).first()

def get_roll_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RollSession).offset(skip).limit(limit).all()

def create_roll_session(db: Session, roll_session: schemas.CreateRollSession):
    db_roll_session = models.RollSession(
            end = roll_session.end,
            start_at = roll_session.start_at
    )
    db.add(db_roll_session)
    db.commit()
    db.refresh(db_roll_session)
    return db_roll_session


def get_roll(db: Session, roll_id: str):
    return db.query(models.Roll).filter(models.Roll.id==roll_id).first()

def get_rolls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Roll).offset(skip).limit(limit).all()

def create_roll(db: Session, roll: schemas.CreateRoll, roll_session_id: int):
    db_roll = models.RollSession(
        id = roll.id,
        roll_at = roll.roll_at,
        position_1 = roll.position_1,
        position_2 = roll.position_2,
        position_3 = roll.position_3,
        position_4 = roll.position_4,
        position_5 = roll.position_5,
        position_6 = roll.position_6,
        roll_session_id = roll_session_id
    )
    db.add(db_roll)
    db.commit()
    db.refresh(db_roll)
    return db_roll