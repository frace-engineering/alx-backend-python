#!/usr/bin/env python3
"""Create a type annotated function that floors a float """
import math


def floor(n: float) -> int:
    """
    Floor a float.

    Args:
       n of type float.

    return:
        int(floor(n)).
    """
    return math.floor(n)
