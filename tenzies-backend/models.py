from sqlalchemy import Boolean, Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from database import Base

class RollSession(Base):
    __tablename__ = "roll_session"

    id = Column(Integer, primary_key=True, index=True)
    end = Column(Boolean, default=False)
    start_at = Column(DateTime)

    rolls = relationship("Roll", back_populates="sessions")

class Roll(Base):
    __tablename__ = "roll"

    id = Column(Integer, primary_key=True, index=True)
    roll_at = Column(DateTime)
    position_1 = Column(Integer)
    position_2 = Column(Integer)
    position_3 = Column(Integer)
    position_4 = Column(Integer)
    position_5 = Column(Integer)
    position_6 = Column(Integer)
    roll_session_id = Column(Integer, ForeignKey("roll_session.id"))



