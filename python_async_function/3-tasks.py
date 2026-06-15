#!/usr/bin/env python3
"""This module creates asyncio tasks from asynchronous coroutines."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio task for wait_random."""
    # Create a task from the wait_random coroutine.
    task = asyncio.create_task(wait_random(max_delay))

    # Return the created task so it can be awaited later.
    return task
