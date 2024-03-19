#!/usr/bin/env python3
"""Measure the runtime of an async programme """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run an async code four times and measure the total time of execution.

    Args:
        None.

    Return:
        Total run time of execution.
        type float.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    duration = time.perf_counter() - start_time
    return duration
