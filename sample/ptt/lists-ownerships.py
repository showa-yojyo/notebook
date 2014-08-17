# -*- coding: utf-8 -*-

# Demonstration POST lists/ownerships
# https://dev.twitter.com/docs/api/1.1/post/lists/ownerships

from twitter import *
from secret import twitter_instance

tw = twitter_instance()
response = tw.lists.ownerships(screen_name='showa_yojyo')

for item in response['lists']:
    print('{mode} {full_name} {description}'.format(**item))
