#!/usr/bin/env python

# Demonstration GET statuses/user_timeline
# See https://dev.twitter.com/rest/reference/get/statuses/user_timeline

from secret import twitter_instance

tw = twitter_instance()

# [1]
response = tw.statuses.user_timeline(
    screen_name='showa_yojyo',
    count=50,
    trim_user=False,
    contributor_details=False,
    include_entities=False,
    include_rts=False,)

# [2]
for stat in response:
    print('{created_at}|@{user[screen_name]}|{text}'.format_map(stat).replace('\n', '\\n'))
