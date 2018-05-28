#!/usr/bin/env python

# Demonstration POST lists/ownerships
# https://dev.twitter.com/rest/reference/post/lists/ownerships

from secret import twitter_instance

tw = twitter_instance()

next_cursor = -1
while next_cursor:
    response = tw.lists.ownerships(
        screen_name='showa_yojyo',
        cursor=next_cursor)

    for item in response['lists']:
        print('{mode}:{full_name}:{description}'.format_map(item).replace('\n', '\\n'))

    next_cursor = response['next_cursor']
