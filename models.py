from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(Float)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    room_type = Column(String)
    price = Column(Float)
    image_url = Column(String)

    def __repr__(self):
        return f"<Property(title={self.title}, rating={self.rating}, location={self.location}, price={self.price})>"
