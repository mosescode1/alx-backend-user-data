#!/usr/bin/env python3
"""Flitering user data obfuscating them"""
import re
from typing import List


def filter_datum(fields: List, redaction: str, message: str, separator: str):
    """Filter_datum for filtering protected data"""
    for field in fields:
        message = re.sub(rf'{field}=.*?(?={separator}|$)',
                         f'{field}={redaction}', message)
    return message
