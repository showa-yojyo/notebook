# -*- coding: utf-8 -*-

# Demonstration POST saved_searches/list
# See https://dev.twitter.com/docs/api/1.1/post/saved_searches/list

from twitter import *
from secret import twitter_instance

tw = twitter_instance()

# ちなみに OR は多用しないほうがよい。
response = tw.saved_searches.list()
for item in response:
    print('{query}'.format(**item))
