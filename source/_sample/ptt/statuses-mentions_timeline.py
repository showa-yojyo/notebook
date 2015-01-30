#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GET statuses/mentions_timeline
# See https://dev.twitter.com/docs/api/1.1/get/statuses/mentions_timeline

from secret import twitter_instance

tw = twitter_instance()

# Comment 1
statuses = tw.statuses.mentions_timeline(count=50, include_entities='true')

# Comment 2
for stat in statuses:
    entities = stat['entities']
    print('{created_at} {text}'.format(**entities))
