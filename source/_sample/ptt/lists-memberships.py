#!/usr/bin/env python

# Demonstration GET lists/memberships
# https://dev.twitter.com/rest/reference/get/lists/memberships

from secret import twitter_instance

tw = twitter_instance()
kwargs = dict(screen_name='showa_yojyo')

next_cursor = -1
while next_cursor:
    # [1]
    response = tw.lists.memberships(cursor=next_cursor, **kwargs)
    lists = response['lists']

    # [2]
    for item in lists:
        print('{full_name}, {description}'.format_map(item).replace('\n', '\\n'))

    next_cursor = response['next_cursor']
