#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST account/update_delivery_device
# See https://dev.twitter.com/rest/reference/post/account/update_delivery_device

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.account.update_delivery_device(
    device='sms',
    include_entities=False)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
