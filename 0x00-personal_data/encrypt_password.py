#!/usr/bin/env python3
"""Checking and validating paswword"""
import bcrypt
from typing import ByteString


def hash_password(password: str) -> bytes:
    """Hassing password"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if password is valid"""
    return bcrypt.checkpw(password.encode(), hashed_password)
