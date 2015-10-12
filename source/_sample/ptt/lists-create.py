#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST lists/create
# See https://dev.twitter.com/rest/reference/post/lists/create

from secret import twitter_instance

tw = twitter_instance()
tw.lists.create(name='listname', description='This is a temporary list')
