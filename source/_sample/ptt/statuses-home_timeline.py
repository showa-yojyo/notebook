#!/usr/bin/env python

# GET statuses/home_timeline
# See https://dev.twitter.com/rest/reference/get/statuses/home_timeline

from secret import twitter_instance

tw = twitter_instance()

# [1]
statuses = tw.statuses.home_timeline(
    count=50,
    trim_user=True,
    include_entities=False,
    exclude_replies=False,)

# [2]
for stat in statuses:
    print('{created_at}|{text}'.format(**stat).replace('\n', '\\n'))
