#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET geo/id/:place_id
# See https://dev.twitter.com/rest/reference/get/geo/id/%3Aplace_id

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.geo.id._id(_id='28b9063fdce43645')

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4)
