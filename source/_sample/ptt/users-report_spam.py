#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST users/report_spam
# See https://dev.twitter.com/rest/reference/post/users/report_spam

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.users.report_spam(screen_name='showa_yojyo')

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
