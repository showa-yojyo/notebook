#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST saved_searches/destroy
# See https://dev.twitter.com/rest/reference/post/saved_searches/destroy/%3Aid

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()

response = tw.saved_searches.destroy(id=4378204334)
pprint(response)
