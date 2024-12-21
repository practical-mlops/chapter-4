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
export AWS_ENDPOINT_URL=http://localhost:9000
```
Also ensure you are port forwarding to MinIO and Redis.

You can run Feast materialization by running the following command
```
START_TIME="2022-09-16T00:00:00"
END_TIME="2023-09-17T00:00:00"
feast materialize $START_TIME $END_TIME
```
**Please ensure you have run Feast Materialization before continuing to further chapters**  

Once feast apply and feast materialize have run you can try retrieving historicalfeatures by running feast_retrieval/retrieve_features.py, and online features by running feast_retrieval/retrieve_online_features.py.   

Can also try `feast serve` and `feast ui` commands  

To move the feature store yaml to Minio please run the following command  
```
python scripts/push_feature_store_config_to_minio.py --bucket-name=feature-registry --minio-endpoint=localhost:9000 --access-key=minio --secret-key=minio123 --insecure --feature-store-path feast/feature_store.yaml
```