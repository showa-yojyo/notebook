#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET users/show
# See https://dev.twitter.com/rest/reference/get/users/show

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()

# [1]
response = tw.users.show(
    screen_name='showa_yojyo',
    include_entities=False)

# [2]
pprint(response)
