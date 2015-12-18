#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET direct_messages/show
# See https://dev.twitter.com/rest/reference/get/direct_messages/show

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.direct_messages.show(_id=677846047566114819)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4)
