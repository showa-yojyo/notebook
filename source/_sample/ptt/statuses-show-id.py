#!/usr/bin/env python

# Demonstration GET statuses/show/:id
# See https://dev.twitter.com/rest/reference/get/statuses/show/%3Aid

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()
response = tw.statuses.show(
    _id=653256646810955776,
    trim_user=True,
    include_my_reteet=True,
    include_entities=False,)

pprint(response)
