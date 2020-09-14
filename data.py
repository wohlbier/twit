#!/usr/bin/env python

from datetime import datetime
import numpy as np
import pandas as pd
import pathlib
from scipy import sparse
import torch
from torch_geometric.data import Data
from twutil import RetweetDataset

if __name__ == "__main__":

#     # read data
#
#     # select columns of interest
#     read_tweet_cols=[
#         #'tweetid',
#         'userid',
#         #'user_display_name',
#         #'user_screen_name',
#         #'user_reported_location',
#         #'user_profile_description',
#         #'user_profile_url',
#         #'follower_count',
#         #'following_count',
#         #'account_creation_date',
#         #'account_language',
#         #'tweet_language',
#         'tweet_text',
#         #'tweet_time',
#         #'tweet_client_name',
#         #'in_reply_to_userid',
#         #'in_reply_to_tweetid',
#         #'quoted_tweet_tweetid',
#         'is_retweet'
#         #'retweet_userid',
#         #'retweet_tweetid',
#         #'latitude',
#         #'longitude',
#         #'quote_count',
#         #'reply_count',
#         #'like_count',
#         #'retweet_count',
#         #'hashtags',
#         #'urls',
#         #'user_mentions'
#     ]
#     path = '/DATA/SDH/twitter/election-integrity/china_052020'
#     base = 'china_052020'
#     f = path + '/' +  base +  "_tweets_csv_hashed.csv"
#
#     # tweet dataframe
#     tdf = pd.read_csv(f, keep_default_na=False, usecols=read_tweet_cols)
#     #'in_reply_to_userid': str, # will result in DtypeWarning: without this
#     #'retweet_tweetid': str,    # will result in DtypeWarning: without this
#
#     # now get users
#     read_user_cols = [
#         'userid',
#         #'user_display_name',
#         #'user_screen_name',
#         #'user_reported_location',
#         #'user_profile_description',
#         #'user_profile_url',
#         'follower_count',
#         'following_count',
#         'account_creation_date',
#         'account_language'
#     ]
#     f = path + '/' +  base +  "_users_csv_hashed.csv"
#     # users dataframe
#     udf = pd.read_csv(f, usecols=read_user_cols)
#
#     # tweets
#
#     # add retweet_userid by taking [1] from tweet_text instead of using
#     # retweet_userid from data, which can be empty. Do the assignment
#     # only if is a retweet.
#     tdf['retweet_userid'] = np.where(tdf.is_retweet == True,
#                                      tdf.tweet_text.str.split(expand=True)[1],
#                                      '')
#     # remove @ in RT
#     tdf['retweet_userid'] = tdf['retweet_userid'].str.replace("@","")
#     # remove trailing : in RT
#     tdf['retweet_userid'] = tdf['retweet_userid'].str.replace(":","")
#
#     # retweets
#
#     # get retweets
#     retweets = tdf.loc[tdf['is_retweet'] == True]
#
#     # pick out unique retweets
#     rt_cols = [
#         'userid',
#         'is_retweet',
#         'retweet_userid'
#     ]
#     #retweets = (retweets.loc[retweets['is_retweet'] == True]) \
#     #    .groupby(rt_cols, as_index=False).size()
#     retweets = retweets.groupby(rt_cols, as_index=False).size()
#
#     # node index is user index. get list of users from full tdf dataset since
#     # user can retweet a user that doesn't retweet.
#
#     # id_u: node id to userid by finding unique userid & unique retweet_userid
#     id_u = list(pd.unique(tdf[['userid','retweet_userid']].\
#                           values.ravel('K')))
#     #  append users from udf, use set and list to get unique hashes
#     id_u = list(set(np.append(id_u, list(pd.unique(udf['userid'])))))
#     num_nodes = len(id_u)
#
#     # u_id: dict k=userid, v=node id
#     u_id = {k: v for v, k in enumerate(id_u)}
#
#     # each retweet is an edge and size is the value
#     r = np.zeros(len(retweets), dtype=np.int_)
#     c = np.zeros(len(retweets), dtype=np.int_)
#     d = np.zeros(len(retweets), dtype=np.int_)
#
#     for index, row in retweets.iterrows():
#         r[index] = u_id[row['userid']]
#         c[index] = u_id[row['retweet_userid']]
#         d[index] = row['size']
#
#     # make edges
#     edge_index = torch.from_numpy(np.transpose(np.column_stack((r,c))))
#     edge_adj = torch.from_numpy(d)
#
#     # add features
#     n_feat = len(read_user_cols) - 1
#     X = torch.zeros((num_nodes, n_feat))
#     y = torch.zeros(num_nodes)
#
#     for index, row in udf.iterrows():
#         node_idx = u_id[row['userid']]
#         X[node_idx,0] = row['follower_count']
#         X[node_idx,1] = row['following_count']
#         X[node_idx,2] = datetime.fromisoformat(row['account_creation_date']).\
#             timestamp()/1.0e9
#         l = row['account_language']
#         s = 0
#         for c in l:
#             s += ord(c)
#         X[node_idx,3] = s
#
# #    data = Data(x=X,edge_index=edge_index, edge_attr=edge_adj, y=y)
#
#     d = [Data(x=X,edge_index=edge_index)]
# #    data, slices = InMemoryDataset.collate(d)
#
# #    # fake some test, train, val masks
# #    dist = np.random.rand(num_nodes)
# #    t = 0.6 # training  0.0 < t < t+v < 1.0
# #    v = 0.2 # val
# #    data.train_mask = torch.from_numpy((dist<t))
# #    data.test_mask = torch.from_numpy((t<dist)&(dist<t+v))
# #    data.val_mask = torch.from_numpy((t+v<dist))

    dataset = RetweetDataset(root='./')
#    dataset = (data, slices)


#torch.save(dataset, 't.pt')

    # csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
    #adj = sparse.csr_matrix((d, (r, c)), (num_nodes,num_nodes), dtype=np.int8)

    #print(adj)
    #print(num_nodes)