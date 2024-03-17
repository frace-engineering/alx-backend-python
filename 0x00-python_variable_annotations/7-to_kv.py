#!/usr/bin/env python3
"""Create a type annotated function that takes twoargs of type string and
integer or float and return a tuple of type str and float..
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Take two args and square one and return tuple.

    Args:
        k of type string.

        v of type integer or float.

    return:
        tuple with values k and v*v.
    """
    return (k, v*v)
