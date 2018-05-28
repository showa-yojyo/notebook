#!/usr/bin/env python

# Demonstration GET users/suggestions/:slug
# See https://dev.twitter.com/rest/reference/get/users/suggestions/%3Aslug

from secret import twitter_instance
from json import dump
from urllib.parse import quote
import sys

tw = twitter_instance()

# [1]
response = tw.users.suggestions._id(_id=quote('政府'))

dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
