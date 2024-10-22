from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Password(Base):
    __tablename__ = "passwords"
    __table_args__ = {'extend_existing': True}  # Allow extending the existing table definition

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    service = Column(String, index=True)
    encrypted_password = Column(String)
