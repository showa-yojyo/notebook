#!/usr/bin/env python
""" testeven.py: Demonstrate Nose.
"""

def test_evens():
    """Test method check_even."""
    for i in range(0, 5):
        yield check_even, i, i * 3

def check_even(val1, val2):
    """Determine if either of numbers is even."""
    assert val1 % 2 == 0 or val2 % 2 == 0
