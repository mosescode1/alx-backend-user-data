#!/usr/bin/env python3
"""Basic  Authenication"""
from auth import Auth


class BasicAuth(Auth):
    """Basic authentication models"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Base64 part"""
        if not authorization_header or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]
