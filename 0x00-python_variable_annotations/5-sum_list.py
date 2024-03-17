#!/usr/bin/env python3
"""Create a type annotated function that takes a  variable of type float
and returns the sun of type float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum the values of a list.

    Args:
        input_list of type float.

    return:
        sum of the list elements of type float.
    """
    return sum(input_list)
