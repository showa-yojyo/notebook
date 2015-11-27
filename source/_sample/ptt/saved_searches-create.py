#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST saved_searches/create
# See https://dev.twitter.com/rest/reference/post/saved_searches/create

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()

# Don't abuse OR.
response = tw.saved_searches.create(query='イルベロ OR イルマティックエンベロープ')
pprint(response)
