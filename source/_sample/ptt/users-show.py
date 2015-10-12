#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET users/show
# See https://dev.twitter.com/rest/reference/get/users/show

from secret import twitter_instance

tw = twitter_instance()

# Comment 1
response = tw.users.show(screen_name='showa_yojyo', entities=1)

# Comment 2
print('''
{screen_name} | {name}
{location}
{url}
{description}

ツイート数 {statuses_count}
フォロー {friends_count} 人
フォロワー {followers_count} 人
'''.format(**response))
