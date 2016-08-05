#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" testrandom.py: Demonstrate Nose.
"""
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
    """A test case."""

    def setUp(self):
        self.seq = list(range(10))

    def test_shuffle(self):
        """A method."""
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

    def test_choice(self):
        """A method."""
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        """A method."""
        self.assertRaises(ValueError, random.sample, self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

def build_suite():
    """A function."""
    return unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)

if __name__ == '__main__':
    #unittest.main()
    unittest.TextTestRunner(verbosity=2).run(build_suite())
