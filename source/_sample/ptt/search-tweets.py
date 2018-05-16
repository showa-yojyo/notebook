#!/usr/bin/env python

# Demonstration GET search/tweets
# See https://dev.twitter.com/rest/reference/get/search/tweets

from secret import twitter_instance

MAX_COUNT = 30

tw = twitter_instance()

# [1]
kwargs = dict(
    q='ネシカ OR nesica',
    include_entities=False,)

# [2]
total = 0
while total < MAX_COUNT:
    # [1]
    response = tw.search.tweets(**kwargs)

    # [2]
    if not 'statuses' in response or not response['statuses']:
        break

    metadata = response['search_metadata']
    statuses = response['statuses']
    max_id = metadata['max_id']
    min_id = statuses[-1]['id']
    total += metadata['count']

    # [3]
    for tweet in statuses:
        print('{created_at}|@{user[screen_name]}|{text}'.format_map(
            tweet).replace('\n', '\\n'))

    # [4]
    kwargs['max_id'] = min_id - 1
