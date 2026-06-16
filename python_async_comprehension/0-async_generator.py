#!/usr/bin/env python3
"""Module that defines an asynchronous generator."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield a random float between 0 and 10 every second.

    The generator loops 10 times. At each iteration, it waits
    asynchronously for 1 second, then yields a random floating-point
    number between 0 and 10.
    """
    # Repeat the process exactly 10 times, as required by the task.
    for _ in range(10):
        # Wait asynchronously for 1 second without blocking the event loop.
        await asyncio.sleep(1)

        # Yield one random float between 0 and 10.
        yield random.uniform(0, 10)
