#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import testrandom
import testwidget

suite1 = testrandom.suite()
suite2 = testwidget.suite()
alltests = unittest.TestSuite([suite1, suite2])

#unittest.TextTestRunner(verbosity=2).run(alltests)

unittest.main()
