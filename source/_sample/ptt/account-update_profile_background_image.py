#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST account/update_profile_background_image
# See https://dev.twitter.com/rest/reference/post/account/update_profile_background_image

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
imagepath = 'profile-background.png'
with open(imagepath, mode='rb') as fp:
    filedata = fp.read()

# [2]
response = tw.account.update_profile_background_image(
    image=filedata, tile=True)

# [3]
dump(response, sys.stdout, ensure_ascii=False, indent=4)
