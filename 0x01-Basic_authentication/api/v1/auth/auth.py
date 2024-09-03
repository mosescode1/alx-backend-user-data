#!/usr/bin/env python3
"""Authentication class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authenticaltion class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method for authenticating"""

        if not path:
            return True

        if not excluded_paths:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        # Check if the normalized path is in the list of excluded paths
        if normalized_path in excluded_paths:
            return False

        # If path is not in excluded_paths, return True
        return True

    def authorization_header(self, request=None) -> str:
        """Method for request headers"""

        if request is None:
            return None

        if request.headers.get("Authorization") is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Retuning the authenticated user"""
        return None
