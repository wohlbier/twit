#!/usr/bin/env python

import csv
import datetime as dt
import numpy as np
import pandas as pd

def reduce_tweets(state, date):
    # select columns of interest
    read_tweet_cols=[
        'tweetid',
        'userid',
        'user_display_name',
        'user_screen_name',
        'user_reported_location',
        'user_profile_description',
        'user_profile_url',
        'follower_count',
        'following_count',
        'account_creation_date',
        'account_language',
        'tweet_language',
        'tweet_text',
        'tweet_time',
        'tweet_client_name',
        'in_reply_to_userid',
        'in_reply_to_tweetid',
        'quoted_tweet_tweetid',
        'is_retweet',
        'retweet_userid',
        'retweet_tweetid',
        'latitude',
        'longitude',
        'quote_count',
        'reply_count',
        'like_count',
        'retweet_count',
        'hashtags',
        'urls',
        'user_mentions'
    ]
    ct = {'in_reply_to_userid': str,
          'retweet_userid': str}

    base = state + '_052020'
    path = '/DATA/SDH/twitter/election-integrity' + '/' + base
    f = path + '/' +  base +  "_tweets_csv_hashed.csv"
    print('reading: ' + f)
    # tweet dataframe
    df = pd.read_csv(f, usecols=read_tweet_cols, dtype=ct,
                     parse_dates=['tweet_time'])

    df = df[df['tweet_time'] >= date]
    nf = path + '/' + base + "_tweets_csv_hashed_ge_" + date + ".csv"
    print("writing: " + nf)
    df.to_csv(nf, index=False, quoting=csv.QUOTE_ALL)

if __name__ == "__main__":
    # china:  23,787 users,     427,903 tweets
    # russia:  1,205 users,   4,373,218 tweets
    # turkey:  9,511 users, 120,253,807 tweets
    states = ['china', 'russia', 'turkey']
    for s in states:
        reduce_tweets(s, "2018-01-01")
