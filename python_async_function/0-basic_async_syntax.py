#!/usr/bin/env python3
"""This module defines a basic asynchronous coroutine."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return the delay value."""
    # Generate a random floating-point number between 0 and max_delay.
    delay = random.uniform(0, max_delay)

    # Pause the coroutine without blocking the whole event loop.
    await asyncio.sleep(delay)

    # Return the same delay that was used for the asynchronous pause.
    return delay
