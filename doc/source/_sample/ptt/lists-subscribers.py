#!/usr/bin/env python

# Demonstration GET lists/subscribers
# https://dev.twitter.com/rest/reference/get/lists/subscribers

from secret import twitter_instance

tw = twitter_instance()

next_cursor = -1
while next_cursor:
    response = tw.lists.subscribers(
        owner_screen_name='showa_yojyo',
        slug='informative',
        cursor=next_cursor)

    for item in response['users']:
        print('{screen_name}: {description}'.format_map(item).replace('\n', '\\n'))

    next_cursor = response['next_cursor']
