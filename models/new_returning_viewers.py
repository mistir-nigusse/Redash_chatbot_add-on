from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NewReturningViewers(Base):
    __tablename__ = 'new_returning_viewers'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    viewer_type = Column(String(50))
    views = Column(String)
