#!/usr/bin/env python

# Demonstration POST lists/members/destroy
# https://dev.twitter.com/rest/reference/post/lists/members/destroy

from secret import twitter_instance

tw = twitter_instance()

tw.lists.members.destroy(
    owner_screen_name='showa_yojyo',
    slug='listname',
    screen_name='showa_yojyo')
