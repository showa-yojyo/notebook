# -*- coding: utf-8 -*-

# Demonstration POST lists/create
# See https://dev.twitter.com/docs/api/1.1/post/lists/create

from twitter import *
from secret import twitter_instance

tw = twitter_instance()
tw.lists.create(name='listname', description='This is a temporary list')
