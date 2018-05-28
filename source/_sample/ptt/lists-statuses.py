#!/usr/bin/env python

# Demonstration GET lists/statuses
# See https://dev.twitter.com/rest/reference/get/lists/statuses

from secret import twitter_instance

tw = twitter_instance()

# [1]
kwargs = dict(
    owner_screen_name='showa_yojyo',
    slug='informative',
    per_page=10,
    page=1,
    include_entities=False,
    include_rts=True)

response = tw.lists.statuses(**kwargs)
for item in response:
    # [2]
    print(item['user']['screen_name'])
    print('{text}\n{created_at} {source}'.format_map(item))
    print('-' * 70)
