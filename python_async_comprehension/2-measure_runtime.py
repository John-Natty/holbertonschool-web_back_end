#!/usr/bin/env python3
"""Module that measures runtime for async comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of four parallel async comprehensions."""
    # Save the start time.
    start_time = time.perf_counter()

    # Run async_comprehension four times in parallel.
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    # Return the elapsed time.
    return time.perf_counter() - start_time
