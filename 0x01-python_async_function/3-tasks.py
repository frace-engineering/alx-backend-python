#!/usr/bin/env python3
"""Genarate asyncio function"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asynchronous from the regular function.

    Args:
        max_delay of type int.

    Return:
        task of type asyncio.Task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
