#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""alltset.py: Demonstrate some of unittest.
"""
import unittest
import testrandom
import testwidget

def main():
    """Main function."""
    suite1 = testrandom.build_suite()
    suite2 = testwidget.build_suite()
    alltests = unittest.TestSuite([suite1, suite2])

    unittest.TextTestRunner(verbosity=2).run(alltests)
    #unittest.main()

if __name__ == '__main__':
    main()
