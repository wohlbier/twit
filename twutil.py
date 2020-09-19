from datetime import datetime
import numpy as np
import pandas as pd
import torch
from torch_geometric.data import Data, InMemoryDataset
from torch_geometric.utils import degree

class RetweetDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(RetweetDataset, self).__init__(root, transform, pre_transform)
        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        # these aren't correct
        return ['china_052020_tweets_csv_hashed.csv',
                'china_052020_users_csv_hashed.csv']

    @property
    def processed_file_names(self):
        return ['rt.pt']

    def download(self):
        # Download to `self.raw_dir`, which is root + '/raw'
        print('already dl')

    def process(self):

        def read_tweets(states):
            # select columns of interest
            read_tweet_cols=[
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
            t = {'userid': str, 'is_retweet': bool, 'retweet_userid': str}
            li = []
            for s in states:
                base = s + '_052020'
                p = '/DATA/SDH/twitter/election-integrity' + '/' + base
                f = p + '/' +  base +  "_tweets_csv_hashed.csv"
                #f = p + '/' +  base +  "_tweets_csv_hashed_ge_2016-01-01.csv"
                #f = p + '/' +  base +  "_tweets_csv_hashed_ge_2018-01-01.csv"
                print('reading: ' + f)
                # tweet dataframe
                df = pd.read_csv(f, usecols=read_tweet_cols, dtype=t)
                df['state'] = s
                li.append(df)
            return pd.concat(li, axis=0, ignore_index=True)

        def read_users(states):
            read_user_cols = [
                'userid',
                #'user_display_name',
                #'user_screen_name',
                #'user_reported_location',
                #'user_profile_description',
                #'user_profile_url',
                'follower_count',
                'following_count',
                'account_creation_date',
                'account_language'
            ]
            t = {'userid': str}
            li = []
            for s in states:
                base = s + '_052020'
                p = '/DATA/SDH/twitter/election-integrity' + '/' + base
                f = p + '/' +  base +  "_users_csv_hashed.csv"
                print('reading: ' + f)
                # tweet dataframe
                df = pd.read_csv(f, usecols=read_user_cols, dtype=t)
                df['state'] = s
                li.append(df)
            return pd.concat(li, axis=0, ignore_index=True)

        # china:  23,787 users,     427,903 tweets
        # russia:  1,205 users,   4,373,218 tweets
        # turkey:  9,511 users, 120,253,807 tweets
        #states = ['china']
        #states = ['russia']
        #states = ['turkey']
        #states = ['china','russia']
        states = ['china','russia','turkey']
        # tweet dataframe
        tdf = read_tweets(states)

        # users dataframe
        udf = read_users(states)

        # retweets. remove rows where retweet_userid == ''
        retweets = tdf.loc[((tdf['is_retweet'] == True)
                            & (tdf['retweet_userid'] != ''))]

        # pick out unique retweets
        rt_cols = [
            'userid',
            'is_retweet',
            'retweet_userid'
        ]
        # add number of instances
        retweets = retweets.groupby(rt_cols, as_index=False).size()

        # node index is user index. get list of users from udf. Retweets
        # of users not in udf are not in the graph.
        id_u = list(pd.unique(udf['userid']))
        num_nodes = len(id_u)

        # u_id: dict k=userid, v=node id
        u_id = {k: v for v, k in enumerate(id_u)}

        # each retweet is an edge and size is the value
        r = np.zeros(len(retweets), dtype=np.int_)
        c = np.zeros(len(retweets), dtype=np.int_)
        d = np.zeros(len(retweets), dtype=np.int_)

        print("Number of retweets: " + str(len(retweets)))
        print("Number of users:    " + str(num_nodes))
        # go through all retweets
        for index, row in retweets.iterrows():
            r[index] = u_id[row['userid']]
            c[index] = u_id[row['retweet_userid']]
            d[index] = row['size']

        # make edges
        edge_index = torch.from_numpy(np.transpose(np.column_stack((r,c))))
        edge_adj = torch.from_numpy(d)

        # add features
        n_feat = len(udf.columns) - 2 # 'userid', 'state'
        print('n_feat: ' + str(n_feat))
        X = torch.zeros((num_nodes, n_feat))
        y = torch.zeros((num_nodes),dtype=torch.long)

        # other feature vectors from tweets
        # number of tweets
        # number of retweets
        # number of quotes (per tweet)
        # number of replies (per tweet)
        # number of likes (per tweet)
        # bag of words for tweet text

        sv = {k: v for v, k in enumerate(states)}
        for index, row in udf.iterrows():
            node_idx = u_id[row['userid']]
            y[node_idx] = sv[row['state']]
            X[node_idx,0] = row['follower_count']
            X[node_idx,1] = row['following_count']
            X[node_idx,2] = datetime.\
                fromisoformat(row['account_creation_date']).timestamp()/1.0e9
            l = row['account_language']
            s = 0
            for c in l:
                s += ord(c)
            X[node_idx,3] = s

        d = Data(x=X, edge_index=edge_index, edge_attr=edge_adj, y=y)
        d.num_nodes = num_nodes

        # test, train, val masks
        dist = np.random.rand(num_nodes)
        t = 0.6 # training  0.0 < t < t+v < 1.0
        v = 0.2 # val
        d.train_mask = torch.from_numpy((dist<t))
        d.test_mask = torch.from_numpy((t<dist)&(dist<t+v))
        d.val_mask = torch.from_numpy((t+v<dist))

        # Read data into huge `Data` list.
        data_list = [d]

        if self.pre_filter is not None:
            data_list = [data for data in data_list if self.pre_filter(data)]

        if self.pre_transform is not None:
            data_list = [self.pre_transform(data) for data in data_list]

        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])
