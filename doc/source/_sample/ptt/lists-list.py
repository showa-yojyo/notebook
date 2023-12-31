#!/usr/bin/env python

# Demonstration GET lists/list
# See https://dev.twitter.com/rest/reference/get/lists/list

from secret import twitter_instance

tw = twitter_instance()

# [1]
response = tw.lists.list(screen_name='showa_yojyo')

# [2]
for item in response:
    print('{mode} {full_name} {description}'.format_map(item).replace('\n', '\\n'))
