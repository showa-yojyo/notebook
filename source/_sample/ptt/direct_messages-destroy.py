#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST direct_messages/destroy
# See https://dev.twitter.com/rest/reference/post/direct_messages/destroy

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.direct_messages.destroy(
    _id=677846047566114819,
    include_entities=False)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
