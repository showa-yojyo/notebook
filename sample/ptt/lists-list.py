#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET lists/list
# See https://dev.twitter.com/docs/api/1.1/get/lists/list

from secret import twitter_instance

tw = twitter_instance()

# Comment 1
response = tw.lists.list(screen_name='showa_yojyo')

# Comment 2
for item in response:
    print('{mode} {full_name} {description}'.format(**item))
