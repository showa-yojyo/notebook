#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET lists/memberships
# https://dev.twitter.com/rest/reference/get/lists/memberships

from secret import twitter_instance

tw = twitter_instance()

# Comment 1
kwargs = dict(screen_name='showa_yojyo', cursor=-1)
response = tw.lists.memberships(**kwargs)

# Comment 2
lists = response['lists']
for item in lists:
    print('{full_name}, {description}'.format(**item))
