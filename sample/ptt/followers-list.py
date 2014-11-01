#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET followers/list
# See https://dev.twitter.com/docs/api/1.1/followers/list

from secret import twitter_instance

tw = twitter_instance()
next_cursor = -1

while next_cursor != 0:
    response = tw.followers.list(
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