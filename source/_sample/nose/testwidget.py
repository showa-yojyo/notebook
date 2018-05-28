#!/usr/bin/env python
""" testwidget.py: Demonstrate Nose.
"""
import unittest
import mywidget

class WidgetTestCase(unittest.TestCase):
    """A test case."""

    def setUp(self):
        self.widget = mywidget.Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        """A method."""
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorrect default size')

    def test_resize(self):
        """A method."""
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')

def build_suite():
    """A function."""
    #suite = unittest.TestSuite()
    #suite.addTest(WidgetTestCase('test_default_size'))
    #suite.addTest(WidgetTestCase('test_resize'))

    suite = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
    return suite

if __name__ == '__main__':
    #unittest.TextTestRunner(verbosity=2).run(build_suite())
    unittest.main()

