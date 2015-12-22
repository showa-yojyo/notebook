#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET friendships/show
# See https://dev.twitter.com/rest/reference/get/friendships/show

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
users = (
    dict(source_screen_name='asahi', target_screen_name='Sankei_news'),
    dict(source_screen_name='Sankei_news', target_screen_name='asahi'),)

for i in users:
    response = tw.friendships.show(**i)

    dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
    sys.stdout.write('\n')
