# -*- coding: utf-8 -*-

# Demonstration GET lists/statuses
# See https://dev.twitter.com/docs/api/1.1/get/lists/statuses

from twitter import *
from secret import twitter_instance

tw = twitter_instance()

# Comment 1
kwargs = dict(
    owner_screen_name='showa_yojyo',
    slug='news',
    per_page=10,
    page=1,
    include_entities=1,
    include_rts=1)

response = tw.lists.statuses(**kwargs)
for item in response:
    # Comment 2
    print(item['user']['screen_name'])
    print('{text}\n{created_at} {source}'.format(**item))
    print('-' * 70)
