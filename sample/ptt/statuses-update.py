# -*- coding: utf-8 -*-

# Demonstration POST statuses/update
# See https://dev.twitter.com/docs/api/1.1/post/statuses/update

from twitter import *
from secret import twitter_instance

tw = twitter_instance()

# Comment 1
mytext = 'PTT を利用したツイートのデモ。明示的 URL エンコード処理なし'

if len(mytext) > 140:
    print('mytext exceeds 140 characters.')
else:
    try:
        # Comment 2
        tw.statuses.update(status=mytext)
    except twitter.TwitterHTTPError as e:
        print(e)
