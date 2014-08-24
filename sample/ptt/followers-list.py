#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET followers/list
# See https://dev.twitter.com/docs/api/1.1/followers/list

from twitter import *
from secret import twitter_instance

tw = twitter_instance()
followers = tw.followers.list(
    screen_name='showa_yojyo',
    cursor=-1,
    count=20,
    skip_status=True,
    include_user_entities=False,)

# I don't use cursor parameter because I have few (less than 20) followers.
for follower in followers['users']:
    print('''
{screen_name} / {name}
{description}
{url}
'''.format(**follower))
