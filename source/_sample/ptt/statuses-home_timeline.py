#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GET statuses/home_timeline
# See https://dev.twitter.com/docs/api/1.1/get/statuses/home_timeline

from secret import twitter_instance

tw = twitter_instance()

statuses = tw.statuses.home_timeline(
    count=10,
    include_rts='true',
    include_entities='true',
    exclude_replies='false',)

for stat in statuses:
    print('{created_at} {text}'.format(**stat))
