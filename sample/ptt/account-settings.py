# -*- coding: utf-8 -*-

# Demonstration GET accout/settings
# https://dev.twitter.com/docs/api/1.1/get/account/settings

from twitter import *
from secret import twitter_instance
import pprint

tw = twitter_instance()
settings = tw.account.settings()

#print(settings)
pprint.pprint(settings)
