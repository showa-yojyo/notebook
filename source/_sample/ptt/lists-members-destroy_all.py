#!/usr/bin/env python

# Demonstration POST lists/members/destroy_all
# https://dev.twitter.com/rest/reference/post/lists/members/destroy_all

from secret import twitter_instance

tw = twitter_instance()

screen_names=(
    # ...
    )

tw.lists.members.destroy_all(
    owner_screen_name='showa_yojyo',
    slug='listname',
    screen_name=','.join(screen_names))
