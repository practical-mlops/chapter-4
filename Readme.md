# Design a Machine Learning System (From Scratch) Chapter 4
## Getting Started

Setup a virtual envrionment by running

```
python3.10 -m venv myvenv
source myvenv/bin/activate
```

Install all the requirements by running
```
pip install -r requirements.txt
```
### Mlflow

Deploy MLFlow and MinIO(part of Kubeflow) by following instructions in the appendix. At the time of writing this book we are using mlflow version 2.6.0

Please create an empty bucket in MinIO called mlflow-datasets

Port forward to mlflow service before running the notebook data_exploration_and_model_training.ipynb



## Feast
Install MinIO and Redis as specified in the Appendix  
Please replace the redis password in feature_store.yaml with your redis password  
Also move the datasets in feast/feature_data to minio bucket feature-data-sets  

Before running the feast apply command please set the following environment variables
```
export AWS_SECRET_ACCESS_KEY=minio123 
export AWS_ACCESS_KEY_ID=minio
export FEAST_S3_ENDPOINT_URL=http://localhost:9000
export S3_ENDPOINT_URL=http://localhost:9000
```
Also ensure you are port forwarding to MinIO and Redis.

Once feast apply has run you can try retrieving features by running feast_retrieval/retrieve_features.py. Can also try `feast serve` and `feast ui` commands

