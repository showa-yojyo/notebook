#!/usr/bin/env python

# Demonstration GET friendships/incoming
# See https://dev.twitter.com/rest/reference/get/friendships/incoming

from secret import twitter_instance

tw = twitter_instance()

next_cursor = -1 # [1]
while next_cursor: # [1]
    response = tw.friendships.incoming(cursor=next_cursor)
    print(response['ids'])
    next_cursor = response['next_cursor'] # [1]
