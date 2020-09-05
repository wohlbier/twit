#!/bin/bash

BUCKET="twitter-election-integrity/hashed/2020_05/china_052020/china_052020_tweet_media_hashed/"
FILES="china_052020_hashed_001.zip
china_052020_hashed_002.zip
china_052020_hashed_003.zip
china_052020_hashed_004.zip
china_052020_hashed_005.zip
china_052020_hashed_006.zip
china_052020_hashed_007.zip
china_052020_hashed_008.zip
china_052020_hashed_009.zip
china_052020_hashed_010.zip
china_052020_hashed_011.zip
china_052020_hashed_012.zip
china_052020_hashed_013.zip
china_052020_hashed_014.zip
china_052020_hashed_015.zip
china_052020_hashed_016.zip
china_052020_hashed_017.zip"

gsutil cp $BUCKET/china_052020_hashed_README.txt .

for f in $FILES
do
    echo $f
    gsutil cp gs://$BUCKET$f .
    unzip $f
done
