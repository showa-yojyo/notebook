#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET statuses/oembed
# See https://dev.twitter.com/rest/reference/get/statuses/oembed

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()
response = tw.statuses.oembed(
    url='https://twitter.com/showa_yojyo/status/674636677982257152',)

pprint(response)
