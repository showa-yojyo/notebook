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
else:
    try:
        # [2]
        tw.statuses.update(status=mytext)
    except twitter.TwitterHTTPError as e:
        print(e)
