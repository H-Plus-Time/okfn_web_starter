from sqlalchemy import Column, Integer, String, Float
from database import Base, safe_val

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    latitude = Column(Float)
    longitude = Column(Float)
    # For brevity, using UNIX Time rather than the Flask DateTime type
    visit_time = Column(Integer)

    

    def __init__(self, attr_dict):
        self.name = safe_val(attr_dict, "name")
        self.email = safe_val(attr_dict, "email")
        self.longitude = safe_val(attr_dict, "longitude")
        self.latitude = safe_val(attr_dict, "latitude")
        self.visit_time = safe_val(attr_dict, "visit_time")


    def __repr__(self):
        return pprint.pprint(to_json(self))

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}