#!/usr/bin/env python3
"""Basic  Authenication"""
from .auth import Auth
import base64


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
