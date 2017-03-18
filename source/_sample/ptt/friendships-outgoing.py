#!/usr/bin/env python

# Demonstration GET friendships/outgoing
# See https://dev.twitter.com/rest/reference/get/friendships/outgoing

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

next_cursor = -1 # [1]
while next_cursor: # [1]
    response = tw.friendships.outgoing(cursor=next_cursor)
    print(response['ids'])
    next_cursor = response['next_cursor'] # [1]
