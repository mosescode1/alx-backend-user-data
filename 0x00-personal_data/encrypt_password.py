#!/usr/bin/env python3
"""Flitering user data obfuscating them"""
import re


def filter_datum(fields: list, redaction: str, message: str, separator: str):
    """Filter_datum for filtering protected data"""

    for field in fields:
        # Construct a regex pattern to match 'field=value' format
        pattern = rf'{field}=.*?(?={separator}|$)'
        print(pattern)
        # Replace the field value with the redaction string
        message = re.sub(pattern, f'{field}={redaction}', message)

    return message
