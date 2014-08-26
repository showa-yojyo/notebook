#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST lists/members/destroy
# https://dev.twitter.com/docs/api/1.1/post/lists/members/destroy

from secret import twitter_instance

tw = twitter_instance()

tw.lists.members.destroy(
    owner_screen_name='showa_yojyo',
    slug='listname',
    screen_name='showa_yojyo') # デモコードなので自分自身決め打ち
