#!/usr/bin/env python3
"""Craete a type annotated function that sums a list of mixed variable types
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum the list elements of mixed varialble types.

    Args:
        mxd_lst of type float and int.

    return:
        the sum of type float.
    """
    res = 0
    for item in mxd_lst:
        res += item

    return res
