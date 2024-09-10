#!/usr/bin/python3
"""User Model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from typing import List, Optional, Union, ByteString
Base = declarative_base()


class User(Base):
    """User Model"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    # def __init__(self, email: str, hashed_password: ByteString, session_id=None, reset_token=None):
    #     if not session_id is None:
    #         self.session_id = session_id
    #     if not reset_token is None:
    #         self.reset_token = reset_token

    #     self.email = email
    #     self.hashed_password = hashed_password
