# twit

number of tweets:
china:     427903
russia:   4373218
turkey: 120253807

```
conda create -n twit_env -c conda-forge \
      gsutil \
      numpy \
      pandas \
      pip \
      python \
      scipy \
      unzip
conda activate twit_env

CUDA=cpu
pip install torch-scatter==latest+${CUDA} torch-sparse==latest+${CUDA} -f https://pytorch-geometric.com/whl/torch-1.6.0.html
pip install torch-geometric
```

```
./getdata.sh china
./getdata.sh russia
./getdata.sh turkey
```



Datasets released in June 2020

China (May 2020) - 23750 Accounts
Account Information (1 MB)
Tweet Information (73.2 MB)
Media (31 GB, 17 archives)

Turkey (May 2020) - 7340 Accounts
Account Information (533 KB)
Tweet Information (5 GB)
Media (821 GB, 391 archives)

Russia (May 2020) - 1152 Accounts
Account Information (85 KB)
Tweet Information (353 MB)
Media (108 GB, 54 archives)

Datasets released in April 2020

Egypt (February  2020) - 2541 Accounts
Account Information (191 KB)
Tweet Information (1 GB)
Media (575 GB, 204 archives)

Honduras (February  2020) - 3104 Accounts
Account Information (178 KB)
Tweet Information (137 MB)
Media (75 GB, 34 archives)

Indonesia (February  2020) - 795 Accounts
Account Information (57 KB)
Tweet Information (207 MB)
Media (58 GB, 21 archives)

Serbia (February  2020) - 8558 Accounts
Account Information (470 KB)
Tweet Information (5.7 GB)
Media (2.3 TB, 981 archives)

SA_EG_AE (February  2020) - 5350 Accounts
Account Information (388 KB)
Tweet Information (4.2 GB)
Media (977 GB, 330 archives)

Datasets released in March 2020

Ghana / Nigeria (March 2020) - 71 Accounts
Account Information (18 KB)
Tweet Information (27 MB)
Media (17 GB, 6 archives)

Datasets released in December 2019

Saudi Arabia (October 2019) - 5,929 Accounts
Account Information (512 KB)
Tweet Information (4.3 GB)
Media (1.3 TB)

Datasets released in September 2019

China (July 2019, set 3) - 4,301 Accounts
Account Information (258 KB)
Tweet Information (913 MB)
Media (604 GB, 224 archives)

Saudi Arabia (April 2019) - 6 Accounts
Account Information (1 KB)
Tweet Information (38 KB)
Media (357 MB, 1 archives)

Ecuador (April 2019) - 1,019 Accounts
Account Information (57 KB)
Tweet Information (85 MB)
Media (173 GB, 56 archives)

United Arab Emirates (March 2019) - 4,248 Accounts
Account Information (355 KB)
Tweet Information (227 MB)
Media (680 GB, 304 archives)

Spain (April 2019) - 259 Accounts
Account Information (20 KB)
Tweet Information (7 MB)
Media (16 GB, 9 archives)

United Arab Emirates / Egypt (April 2019) - 271 Accounts
Account Information (20 KB)
Tweet Information (30 MB)
Media (45 GB, 19 archives)

Datasets released in August 2019

China (July 2019, set 1) - 744 Accounts
Account Information (41 KB)
Tweet Information (158 MB)
Media (85 GB, 32 archives)

China (July 2019, set 2) - 196 Accounts
Account Information (14 KB)
Tweet Information (169 MB)
Media (40 GB, 17 archives)

Datasets released in June 2019

Catalonia (June 2019) - 130 accounts
Account information
Tweet information (1.5MB)
Media (2.74GB, 3 archives)

Iran (June 2019, set 1) - 1,666 accounts
Account information
Tweet information (316MB)
Media (258GB, 111 archives)

Iran (June 2019, set 2) - 248 accounts
Account information
Tweet information (318MB)
Media (183GB, 29 archives)

Iran (June 2019, set 3) - 2,865 accounts
Account information
Tweet information (46MB)
Media (55GB, 18 archives)

Russia (June 2019) - 4 accounts
Account information
Tweet information (260KB)
Media (72MB, 2 archives)

Venezuela (June 2019) - 33 accounts
Account information
Tweet information (64MB)
Media (24GB, 13 archives)

Datasets released in January 2019

Iran (January 2019) - 2,320 accounts
Account information
Tweet information (717MB)
Media (202GB, 89 archives)

Bangladesh (January 2019) - 15 accounts
Account information
Tweet information (2.6MB)
Media (77MB, 3 archives)

Russia (January 2019) - 416 accounts
Account information
Tweet information (120MB)
Media (63.7GB, 8 archives)

Venezuela (January 2019, set 1) - 1,196 accounts
Account information
Tweet information (1GB)
Media (359GB, 75 archives)

Venezuela (January 2019, set 2) - 764 accounts
Account information
Tweet information (136MB)
Media (81GB, 37 archives)

Datasets released in October 2018

Internet Research Agency (October 2018) - 3,613 accounts
Account information
Tweet information (1.2GB)
Media (274GB, 300 archives)

Iran (October 2018) - 770 accounts
Account information
Tweet information (168MB)
Media (65.7GB, 52 archives)
