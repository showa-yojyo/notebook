#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET friends/ids
# See https://dev.twitter.com/rest/reference/friends/ids

from secret import twitter_instance

tw = twitter_instance()

next_cursor = -1 # [1]
while next_cursor: # [1]
    response = tw.friends.ids(
        stringify_ids=True, # [2]
        cursor=next_cursor,) # [1]

    print(','.join(response['ids'])) # [3]
    next_cursor = response['next_cursor'] # [1]
