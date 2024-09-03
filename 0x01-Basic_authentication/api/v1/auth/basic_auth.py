#!/usr/bin/env python3
"""Basic  Authenication"""
from .auth import Auth
import base64
from typing import TypeVar
from models.user import User
import uuid


class BasicAuth(Auth):
    """Basic authentication models"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns Base64 part for basic auth"""

        if (
            not authorization_header
            or not isinstance(authorization_header, str)
            or not authorization_header.startswith("Basic ")
        ):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """DEcode"""
        if base64_authorization_header is None:
            return None

        try:
            string = base64.b64decode(
                base64_authorization_header).decode("utf-8")
            return string
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str):
        """extracing data"""
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        username, password = decoded_base64_authorization_header.split(":")
        return (username, password)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns User object or None if not found"""
        if (user_email is None
                or not isinstance(user_email, str)):
            return None

        if (user_pwd is None
                or not isinstance(user_pwd, str)):
            return None

        user_list = User.all()
        if not user_list:
            return None
        valid_user = None

        for user in user_list:
            if user.email == user_email:
                valid_user = user

        if valid_user is None:
            return None

        if not valid_user.is_valid_password(user_pwd):
            return None

        return valid_user
