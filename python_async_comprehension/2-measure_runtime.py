#!/usr/bin/env python3
"""Module that measures the runtime of async comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of four parallel async comprehensions."""
    # Save the time before starting the four coroutines.
    start_time = time.time()

    # Run async_comprehension four times concurrently.
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # Save the time after all four coroutines are finished.
    end_time = time.time()

    # Return the total elapsed time.
    return end_time - start_time
