#!/usr/bin/env python3
"""Module that measures the runtime of async comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of four parallel async comprehensions."""
    # Save the start time before launching the async comprehensions.
    start_time = time.time()

    # Run async_comprehension four times in parallel.
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # Save the end time after all async comprehensions are finished.
    end_time = time.time()

    # Return the total elapsed runtime.
    return end_time - start_time
