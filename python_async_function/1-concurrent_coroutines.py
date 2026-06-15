#!/usr/bin/env python3
"""Module for running multiple asynchronous coroutines concurrently."""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times and return delays in completion order."""
    # Store each delay returned by the wait_random coroutine.
    delays: List[float] = []

    # Create n coroutines using the same maximum delay.
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Wait for each coroutine in the order it finishes.
    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    # Return the delays without using sort(), as required.
    return delays
