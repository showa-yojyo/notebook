#!/usr/bin/env python

# Demonstration GET users/profile_banner
# See https://dev.twitter.com/rest/reference/get/users/profile_banner

from secret import twitter_instance
from pprint import pprint

tw = twitter_instance()
response = tw.users.profile_banner(screen_name='showa_yojyo')
pprint(response['sizes'])
