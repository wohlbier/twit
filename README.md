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