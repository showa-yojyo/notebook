#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST favorites/destroy
# See https://dev.twitter.com/rest/reference/post/favorites/destroy

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.favorites.destroy(
    _id=653256646810955776,
    include_entities=False)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
