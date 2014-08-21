# -*- coding: UTF-8 -*-
import nose
from nose.plugins.attrib import attr

def test_regular():
    """A regular test case"""
    nose.tools.ok_(True)

def test_big_download():
    """A very slow test case"""
    pass

# Directly set "slow" attribute to test_big_download.
test_big_download.slow = True

@attr('slow')
def test_big_download2():
    """A test with attribute"""
    pass

@attr(speed='slow')
def test_big_download3():
    """A test with attribute specific value"""
    pass

@attr(tags=['http'])
def test_tags():
    pass
