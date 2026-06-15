#!/usr/bin/env python3
"""This module runs several asynchronous coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times and return delays by completion order."""
    # This list stores the delay values returned by the coroutines.
    delays: List[float] = []

    # Create n tasks so they can run concurrently.
    tasks = [
        asyncio.create_task(wait_random(max_delay))
        for _ in range(n)
    ]

    # Collect each result when its task is finished.
    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    # Return the collected delay values.
    return delays
