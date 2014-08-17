# -*- coding: utf-8 -*-

# Demonstration GET statuses/user_timeline
# See https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline

from twitter import *
from secret import twitter_instance

tw = twitter_instance()
stats = tw.statuses.user_timeline(screen_name='showa_yojyo', count=40)

for stat in stats:
    print('{created_at} {text}'.format(**stat))
