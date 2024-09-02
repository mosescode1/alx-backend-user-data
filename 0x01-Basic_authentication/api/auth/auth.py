"""Authentication class"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method for authenticating"""
        return False

    def authorization_header(self, request=None) -> str:
        """Method for request headers"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retuning the authenticated user"""
        return None
