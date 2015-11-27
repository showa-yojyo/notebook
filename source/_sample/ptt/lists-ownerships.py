#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST lists/ownerships
# https://dev.twitter.com/rest/reference/post/lists/ownerships

from secret import twitter_instance

tw = twitter_instance()

next_cursor = -1
while next_cursor != 0:
    response = tw.lists.ownerships(
        screen_name='showa_yojyo',
        cursor=next_cursor)

    for item in response['lists']:
        print('{mode}:{full_name}:{description}'.format(**item).replace('\n', '\\n'))

    next_cursor = response['next_cursor']
