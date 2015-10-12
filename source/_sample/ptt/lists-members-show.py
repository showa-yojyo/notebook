#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET lists/members/show
# https://dev.twitter.com/rest/reference/get/lists/members/show

from secret import twitter_instance

tw = twitter_instance()

params = dict(
    owner_screen_name='showa_yojyo',
    slug='news',
    screen_name='asahi',
    include_entities=False,
    skip_status=False,)

response = tw.lists.members.show(**params)
print('{screen_name} / {name} {description}'.format(**response))
