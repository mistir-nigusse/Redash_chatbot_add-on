from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    cities = Column(String(255))
    city_name = Column(String(255))
    views = Column(String)


