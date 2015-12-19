#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST account/update_profile_banner
# See https://dev.twitter.com/rest/reference/post/account/update_profile_banner

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
imagepath = "profile-banner.png"
with open(imagepath, mode='rb') as fp:
    filedata = fp.read()

# [2]
response = tw.account.update_profile_banner(banner=filedata)

# [3]
dump(response, sys.stdout, ensure_ascii=False, indent=4)
