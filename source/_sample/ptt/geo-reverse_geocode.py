#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET geo/reverse_geocode
# See https://dev.twitter.com/rest/reference/get/geo/reverse_geocode

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.geo.reverse_geocode(lat=35.696805, long=139.773828)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
