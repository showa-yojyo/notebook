#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET favorites
# See https://dev.twitter.com/docs/api/1.1/get/favorites/list

from secret import twitter_instance

tw = twitter_instance()

kwargs = dict(
    screen_name='showa_yojyo',
    count=10,
    page=1,
    include_entities=1)

response = tw.favorites.list(**kwargs)
for status in response:
    print('@{user[screen_name]}'.format(**status))
    print('{text}\n{created_at} %{source}'.format(**status))
    print('-' * 70)
