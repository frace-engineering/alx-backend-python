#!/usr/bin/env python3
"""Create a type annotated function to concatenate strings """


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings.

    Args:
       str1 and str2 of type string.

    return:
        concatenated string
    """
    return str1 + str2
