#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET blocks/ids
# See https://dev.twitter.com/rest/reference/get/blocks/ids

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.blocks.ids()

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
