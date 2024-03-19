#!/usr/bin/env python3
"""Async coroutine genarator"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """
    Loop ten times asynchronously and yield random number.

    Args:
        None.

    Return:
        Yields random number after a wait if 1sec.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
