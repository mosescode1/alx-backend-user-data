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


a = BasicAuth()

print(a.extract_base64_authorization_header(None))
print(a.extract_base64_authorization_header(89))
print(a.extract_base64_authorization_header("Holberton School"))
print(a.extract_base64_authorization_header("Basic Holberton"))
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
print(a.extract_base64_authorization_header("Basic1234"))
