#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration GET application/rate_limit_status
# See https://dev.twitter.com/rest/reference/get/application/rate_limit_status

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
resource_families = ('lists,' 'users', 'statuses', 'search')
csv = ','.join(resource_families)

# [2]
response = tw.application.rate_limit_status(resources=csv)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4)
