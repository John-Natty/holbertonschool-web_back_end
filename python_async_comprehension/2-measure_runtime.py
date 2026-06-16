#!/usr/bin/env python3
"""Module that measures the runtime of async comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of four parallel async comprehensions."""
    # Start the timer before running the coroutines.
    start_time = time.perf_counter()

    # Run async_comprehension four times in parallel.
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # Stop the timer after all coroutines are finished.
    end_time = time.perf_counter()

    # Return the elapsed time.
    return end_time - start_time
