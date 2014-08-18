# -*- coding: utf-8 -*-

# Demonstration POST statuses/update_with_media
# See https://dev.twitter.com/docs/api/1.1/post/statuses/update_with_media

from twitter import *
from secret import twitter_instance
import base64

tw = twitter_instance()

with open("illvelo.png", "rb") as imagefile:
    params = {
        "status":"Test uploading an image file by using Python Twitter Tools.",
        "media[]":base64.b64encode(imagefile.read()), "_base64":True,
        #"media[]":imagefile.read(),
        }
    tw.statuses.update_with_media(**params)
