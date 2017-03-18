#!/usr/bin/env python

# Demonstration GET lists/show
# See https://dev.twitter.com/rest/reference/get/lists/show

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()

response = tw.lists.show(
    owner_screen_name='showa_yojyo',
    slug='bot')
pprint(response)
