#!/usr/bin/env python3
"""Asynchronous coroutine function """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Use the return value of max_random(), genarate coroutines.
    Args:
        n of type int
        max_delay of type float
    Return:
        list of delays of type float
    """
    routines = [task_wait_random(max_delay) for _ in range(n)]
    delay_list = await asyncio.gather(*routines)
    return sorted(delay_list)
