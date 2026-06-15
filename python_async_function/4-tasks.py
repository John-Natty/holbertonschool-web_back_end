#!/usr/bin/env python3
"""This module runs multiple asynchronous tasks concurrently."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times and return delays by completion order."""
    # Store the delay values returned by each task.
    delays: List[float] = []

    # Create n asyncio tasks using task_wait_random.
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Collect each task result in the order the tasks complete.
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    # Return the collected delays without manually sorting them.
    return delays
