from pydantic import BaseModel
from datetime import datetime
from typing import List


class ReadRoll(BaseModel):
    id: int
    roll_at: datetime
    position_1: int
    position_2: int
    position_3: int
    position_4: int
    position_5: int
    position_6: int
    roll_session_id: int

    class Config:
        orm_mode = True

class CreateRoll(BaseModel):
    id: int
    roll_at: datetime
    position_1: int
    position_2: int
    position_3: int
    position_4: int
    position_5: int
    position_6: int
    roll_session_id: int

class ReadRollSession(BaseModel):
    id: int
    end: bool
    start_at: datetime
    rolls: List[CreateRoll] = []

    class Config:
        orm_mode = True

class CreateRollSession(BaseModel):
    end: bool
    start_at: datetime