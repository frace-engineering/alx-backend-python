#!/usr/bin/env python3
"""A coroutine that takes no argument """
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Use async comprehension to collect and yield random numbers.

    Args:
        None.

    Retrun:
        random numbers.
    """
    return [i async for i in async_generator()]
