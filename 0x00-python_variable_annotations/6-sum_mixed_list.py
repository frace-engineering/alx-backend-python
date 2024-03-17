#!/usr/bin/env python3
"""Craete a type annotated function that sums a list of mixed variable types
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Sum the list elements of mixed varialble types.

    Args:
        mxd_lst of type float and int.

    return:
        the sum of type float.
    """
    return sum(mxd_lst)
