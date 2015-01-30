# -*- coding: utf-8 -*-
import unittest
import nose

def test():
    assert False

def setup_func():
    """setup test fixtures"""
    pass

def teardown_func():
    """tear down test fixtures"""
    pass

@nose.with_setup(setup_func, teardown_func)
def test2():
    """test2"""
    assert True

if __name__ == '__main__':
    pass
