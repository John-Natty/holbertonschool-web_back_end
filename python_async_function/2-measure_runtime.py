#!/usr/bin/env python3
"""This module measures the runtime of asynchronous coroutines."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n."""
    # Store the current time before running the coroutines.
    start_time = time.time()

    # Run the wait_n coroutine using the asyncio event loop.
    asyncio.run(wait_n(n, max_delay))

    # Store the current time after all coroutines have completed.
    end_time = time.time()

    # Calculate the total elapsed time.
    total_time = end_time - start_time

    # Return the average time per coroutine.
    return total_time / n
