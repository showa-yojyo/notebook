#!/usr/bin/env python

# Demonstration POST saved_searches/list
# See https://dev.twitter.com/rest/reference/post/saved_searches/list

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()

response = tw.saved_searches.list()
pprint(response)
