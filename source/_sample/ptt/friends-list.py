#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET friends/list
# See https://dev.twitter.com/rest/reference/friends/list

from secret import twitter_instance

tw = twitter_instance()
next_cursor = -1

while next_cursor != 0:
    response = tw.friends.list(
        screen_name='showa_yojyo',
        cursor=next_cursor,
        count=200,
        skip_status=True,
        include_user_entities=False,)

    for follower in response['users']:
        print('''
{screen_name} / {name}
{description}
{url}
'''.format(**follower))

    next_cursor = response['next_cursor']
