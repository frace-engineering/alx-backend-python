#!/usr/bin/env python3
# a.py

import asyncio
import random


async def count(bulb=1):
    print(f"{bulb} for One")
    await asyncio.sleep(1)

    print(f"{bulb} for Two")


async def main():
    await asyncio.gather(*(count(i) for i in range(6))) 

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    Time_taken = time.perf_counter() - s
    print(f"{__file__} executed in {Time_taken: 0.2f} secnds.")
