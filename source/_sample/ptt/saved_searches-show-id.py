#!/usr/bin/env python

# Demonstration POST saved_searches/show/:id
# See https://dev.twitter.com/rest/reference/post/saved_searches/show/%3Aid

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()

# [1]
response = tw.saved_searches.show._id(_id=4631629399)
pprint(response)
