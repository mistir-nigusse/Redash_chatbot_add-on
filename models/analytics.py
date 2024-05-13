from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Analytics(Base):
    __tablename__ = 'analytics'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    content_type = Column(String(50))
    device_type = Column(String(50))
    operating_system = Column(String(50))
    sharing_service = Column(String(50))
    subscription_source = Column(String(50))
    subscription_status = Column(String(50))
    subtitles_cc = Column(Boolean)
    traffic_source = Column(String(50))
    views = Column(Integer)
