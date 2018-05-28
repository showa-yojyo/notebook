#!/usr/bin/env python

# Demonstration GET users/search
# See https://dev.twitter.com/rest/reference/get/users/search

from secret import twitter_instance

tw = twitter_instance()

response = tw.users.search(
    q='bot',
    page=0,
    count=20,
    include_entities=False)

for i in response:
    print('''
{screen_name} | {name}
{location}
{url}
{description}

ツイート数 {statuses_count}
フォロー {friends_count} 人
フォロワー {followers_count} 人
'''.format_map(i))

