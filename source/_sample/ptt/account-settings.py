#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET accout/settings
# https://dev.twitter.com/rest/reference/get/account/settings

from secret import twitter_instance
import pprint

tw = twitter_instance()
settings = tw.account.settings()

#print(settings)
pprint.pprint(settings)
