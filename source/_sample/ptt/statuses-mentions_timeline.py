#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GET statuses/mentions_timeline
# See https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline

from secret import twitter_instance

tw = twitter_instance()

# [1]
response = tw.statuses.mentions_timeline(
    count=50,
    trim_user=True,
    contributor_details=False,
    include_entities=False,)

# [2]
for stat in response:
    print('{created_at}|{text}'.format(**stat).replace('\n', '\\n'))
