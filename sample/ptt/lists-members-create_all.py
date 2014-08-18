# -*- coding: utf-8 -*-

# Demonstration POST lists/members/create_all
# https://dev.twitter.com/docs/api/1.1/post/lists/members/create_all

from twitter import *
from secret import twitter_instance

tw = twitter_instance()

screen_names=(
    # ...
    )

tw.lists.members.create_all(
    owner_screen_name='showa_yojyo',
    slug='listname',
    screen_name=','.join(screen_names))
