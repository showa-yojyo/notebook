#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST accout/settings
# https://dev.twitter.com/rest/reference/post/account/settings

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.account.settings(
    _method='POST',
    sleep_time_enabled=True,
    start_sleep_time='03', end_sleep_time='24',
    time_zone='Tokyo',
    lang='ja')

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4)
