#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST direct_messages/new
# See https://dev.twitter.com/rest/reference/post/direct_messages/new

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.direct_messages.new(
    screen_name='showa_yojyo',
    text='いい感じでモジャってますね。')

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
