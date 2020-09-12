#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import sparse

if __name__ == "__main__":

    # select columns of interest
    read_cols=[
        #'tweetid',
        'userid',
        #'user_display_name',
        #'user_screen_name',
        #'user_reported_location',
        #'user_profile_description',
        #'user_profile_url',
        #'follower_count',
        #'following_count',
        #'account_creation_date',
        #'account_language',
        #'tweet_language',
        #'tweet_text',
        #'tweet_time',
        #'tweet_client_name',
        #'in_reply_to_userid',
        #'in_reply_to_tweetid',
        #'quoted_tweet_tweetid',
        'is_retweet',
        'retweet_userid'
        #'retweet_tweetid',
        #'latitude',
        #'longitude',
        #'quote_count',
        #'reply_count',
        #'like_count',
        #'retweet_count',
        #'hashtags',
        #'urls',
        #'user_mentions'
    ]

    f = "/DATA/SDH/twitter/election-integrity/china_052020/china_052020_tweets_csv_hashed.csv"
    df = pd.read_csv(f, keep_default_na=False, usecols=read_cols)
    #'in_reply_to_userid': str, # will result in DtypeWarning: without this
    #'retweet_tweetid': str,    # will result in DtypeWarning: without this

    rt_cols = [
        'userid',
        'is_retweet',
        'retweet_userid'
    ]
    retweets = (df.loc[df['is_retweet'] == True]) \
        .groupby(rt_cols, as_index=False).size()

    #for i in range(len(retweets)):
    #    print(retweets.iloc[i])

    # node index is user index. get list of users from full dataset since
    # user can retweet a user that doesn't retweet.

    # id_u: node id to userid by finding unique userid
    id_u = list(df['userid'].unique())
    id_u = [''] + id_u # prepend user '' for empty retweet_userid's

    # u_id: dict k=userid, v=node id
    u_id = {k: v for v, k in enumerate(id_u)}

    # each retweet is an edge and size is the value
    r = np.zeros(len(retweets))
    c = np.zeros(len(retweets))
    d = np.zeros(len(retweets))

    for index, row in retweets.iterrows():
        r[index] = u_id[row['userid']]
        c[index] = u_id[row['retweet_userid']]
        d[index] = row['size']

    # csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
    adj = sparse.csr_matrix((d, (r, c)), (len(id_u),len(id_u)), dtype=np.int8)

    print(adj)
