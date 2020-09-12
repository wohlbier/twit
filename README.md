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
      python \
      scipy \
      unzip
conda activate twit_env
```

```
./getdata.sh china
./getdata.sh russia
./getdata.sh turkey
```