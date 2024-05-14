from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Analytics(Base):
    __tablename__ = 'analytics'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    content_type = Column(String(50))
    views_content_type = Column(Integer)
    device_type = Column(String(50))
    views_device_type = Column(Integer)
    operating_system = Column(String(50))
    sharing_service = Column(String(50))
    subscription_source = Column(String(50))
 

