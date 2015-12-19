#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST account/remove_profile_banner
# See https://dev.twitter.com/rest/reference/post/account/remove_profile_banner

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.account.remove_profile_banner()

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4)
