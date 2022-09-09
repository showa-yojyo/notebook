#!/usr/bin/env python

# Demonstration GET followers/ids
# See https://dev.twitter.com/rest/reference/get/followers/ids

from secret import twitter_instance

tw = twitter_instance()

next_cursor = -1
while next_cursor:
    response = tw.followers.ids(
        stringify_ids=True,
        cursor=next_cursor)

    print(','.join(response['ids']))
    next_cursor = response['next_cursor']
