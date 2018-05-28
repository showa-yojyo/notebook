#!/usr/bin/env python
"""mynose.py: Demonstrate Nose package.
"""
import nose

def test():
    """A method."""
    assert False

def setup_func():
    """setup test fixtures"""
    pass

def teardown_func():
    """tear down test fixtures"""
    pass

@nose.with_setup(setup_func, teardown_func)
def test2():
    """A method."""
    assert True

if __name__ == '__main__':
    pass
