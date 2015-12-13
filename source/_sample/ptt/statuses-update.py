#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Demonstration POST statuses/update
# See https://dev.twitter.com/rest/reference/post/statuses/update

from secret import twitter_instance

tw = twitter_instance()

# [1]
mytext = 'PTT を利用したツイートのデモ。明示的 URL エンコード処理なし'

if len(mytext) > 140:
    print('mytext exceeds 140 characters.')

# [2]
tw.statuses.update(status=mytext)

# [3]
tweet = 'Demonstrate POST statuses/upadte with media_ids.'
mid = 675725940782071809
tw.statuses.update(status=tweet, media_ids=mid)
