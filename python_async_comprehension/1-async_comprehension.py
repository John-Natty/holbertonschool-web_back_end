#!/usr/bin/env python3
"""Module that collects random numbers using an async comprehension."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator.

    The values are collected using an async comprehension and returned
    as a list of floats.
    """
    # For each value yielded asynchronously by async_generator(),
    # add it to a list and return the completed list.
    return [number async for number in async_generator()]
