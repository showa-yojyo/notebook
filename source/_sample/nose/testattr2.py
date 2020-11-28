#!/usr/bin/env python
""" testattr2.py: Demonstrate Nose.
"""
from nose.plugins.attrib import attr

@attr(speed='slow')
def test_load_all_images():
    """A test cast that takes several minutes."""
    # ...
    pass

@attr(online=True)
def test_download_hardcore_images():
    """A test that makes sense only with network access."""
    # ...
    pass

# Other test cases...
