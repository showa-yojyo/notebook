#!/usr/bin/env python

# Demonstration GET statuses/retweets_of_me
# See https://dev.twitter.com/rest/reference/get/statuses/retweets_of_me

from secret import twitter_instance

tw = twitter_instance()
response = tw.statuses.retweets_of_me(
    trim_user=True,
    include_entities=False,
    include_user_entities=False,)

for tweet in response:
    print('{retweet_count}|{text}'.format(**tweet).replace('\n', '\\n'))
