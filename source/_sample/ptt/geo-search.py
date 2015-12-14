#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET geo/search
# See https://dev.twitter.com/rest/reference/get/geo/search

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.geo.search(query='千代田区')

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4)
