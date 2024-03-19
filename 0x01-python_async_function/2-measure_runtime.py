#!/usr/bin/env python3
"""Mearsure the run time of a function """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time of execution of (wait_n(n, max_delay)) function.

    Args:
        n of type int.
        max_delay of type int.

    Return:
        average runtime of the waitn function, type float.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(wait_n(n, max_delay)))
    total_time = time.perf_counter() - start_time
    average_time = total_time / n
    return average_time
