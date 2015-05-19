#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mywidget

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = mywidget.Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

def suite():
##    suite = unittest.TestSuite()
##    suite.addTest(WidgetTestCase('test_default_size'))
##    suite.addTest(WidgetTestCase('test_resize'))

    suite = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
    return suite

if __name__ == '__main__':
    #unittest.TextTestRunner(verbosity=2).run(suite())
    unittest.main()

