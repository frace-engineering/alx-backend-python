#!/usr/bin/env python3
"""
0-basic_async_syntax.py
Demonstrating async coroutine using random module.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asyncronous coroutine that waits for randome number of
    seconds from 0 - 10, then return the number.

    Args:
       max_delay of type int.

    Return:
        max_delay of type union[int, float].
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
