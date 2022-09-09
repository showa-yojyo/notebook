#!/usr/bin/env python

# Demonstration GET account/verify_credentials
# See https://dev.twitter.com/rest/reference/get/account/verify_credentials

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.account.verify_credentials(
    skip_status=True, email=True)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
