#!/usr/bin/env python

# Demonstration POST saved_searches/destroy
# See https://dev.twitter.com/rest/reference/post/saved_searches/destroy/%3Aid

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()

response = tw.saved_searches.destroy._id(_id=4378204334)
pprint(response)
