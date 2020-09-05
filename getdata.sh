#!/bin/bash

if [ "$1" = "china" ]; then
    echo "getting china data"
    BUCKET="twitter-election-integrity/hashed/2020_05/china_052020"
    BASE="china_052020"
    NZ=17
elif [ "$1" = "russia" ]; then
    echo "getting russia data"
elif [ "$1" = "turkey" ]; then
    echo "getting turkey data"
else
    echo "need to specify china, russia, or turkey"
    exit 1
fi

f=Twitter_Elections_Integrity_Datasets_hashed_README.txt
if [ ! -f ./${f} ]; then
    echo "Getting ${f}"
    gsutil cp gs://twitter-election-integrity/hashed/2020_05/${f} .
fi

# check if exists already, ask for removal
if [ ! -d ${BASE} ]; then
    mkdir -p ${BASE}
fi
cd ${BASE}

# hashed users
f=${BASE}_users_csv_hashed.zip
if [ ! -f ./${f} ]; then
    gsutil cp gs://${BUCKET}/${f} .
    unzip ${f}
fi

# tweets and metadata
f=${BASE}_tweets_csv_hashed.zip
if [ ! -f ./${f} ]; then
    gsutil cp gs://${BUCKET}/${f} .
    unzip ${f}
fi

# media
# README
p=${BASE}_tweet_media_hashed
f=${BASE}_hashed_README.txt
if [ ! -f ./${f} ]; then
    gsutil cp gs://${BUCKET}/${p}/${f} .
fi

# files
for i in $(seq 1 $NZ); do
    if [ "$i" -lt "10" ]; then
        n=00$i
    elif [ "$i" -lt "100" ]; then
        n=0$i
    else
        n=0$i
    fi

    f=${BASE}_hashed_${n}.zip
    if [ ! -f ./${f} ]; then
        gsutil cp gs://${BUCKET}/${p}/${f} .
        unzip ${f}
    fi
done
