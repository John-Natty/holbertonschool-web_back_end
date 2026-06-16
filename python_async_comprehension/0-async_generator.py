#!/usr/bin/env python3
"""Module that defines an asynchronous generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield a random float between 0 and 10 every second."""
    # Loop exactly 10 times, as required by the task.
    for _ in range(10):
        # Wait asynchronously for 1 second.
        await asyncio.sleep(1)

        # Yield a random float between 0 and 10.
        yield random.uniform(0, 10)
