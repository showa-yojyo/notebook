#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST saved_searches/create
# See https://dev.twitter.com/rest/reference/post/saved_searches/create

from secret import twitter_instance

tw = twitter_instance()

# ちなみに OR は多用しないほうがよい。
tw.saved_searches.create(query='イルベロ OR イルマティックエンベロープ')
