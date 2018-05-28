#!/usr/bin/env python

# Demonstration POST account/update_profile
# See https://dev.twitter.com/rest/reference/post/account/update_profile

from secret import twitter_instance
from json import dump
import sys

tw = twitter_instance()

# [1]
response = tw.account.update_profile(
    name='プレハブ小屋',
    url='https://github.com/showa-yojyo',
    location='東京都区内',
    description='実は電子の世界の人で現実には存在しない。',
    profile_link_color='FF1493',
    include_entities=False,
    skip_status=True)

# [2]
dump(response, sys.stdout, ensure_ascii=False, indent=4, sort_keys=True)
