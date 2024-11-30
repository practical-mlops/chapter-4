from datetime import timedelta

from feast import FeatureView, Feature, ValueType, FileSource, Field
from feast.data_format import ParquetFormat
from feast.types import String
from entity import user
import os

demo_features_parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path="s3://feature-data-sets/demographic_features.parquet",
    s3_endpoint_override="http://localhost:9000",
)

relationship_features_parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path="s3://feature-data-sets/relationship_features.parquet",
    s3_endpoint_override="http://localhost:9000",
)

occupational_features_parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path="s3://feature-data-sets/occupational_features.parquet",
    s3_endpoint_override="http://localhost:9000",
)


demo_features = FeatureView(
    name="demographic",
    entities=[user],
    schema=[
        Field(name="Native_country", dtype=String),
        Field(name="Sex", dtype=String),
        Field(name="Race", dtype=String),
    ],
    ttl=timedelta(days=365),
    source=demo_features_parquet_file_source,
    tags={
        "authors": "Benjamin Tan <benjamin.tan@abc.random.com, Varun Mallya <varun.mallya@abc.random.com",
        "description": "User Demographics",
        "used_by": "Income_Calculation_Team",
    },
)

relationship_features = FeatureView(
    name="relationship",
    entities=[user],
    schema=[
        Field(name="Relationship", dtype=String),
        Field(name="Marital-Status", dtype=String),
    ],
    ttl=timedelta(days=365),
    source=relationship_features_parquet_file_source,
    tags={
        "authors": "Varun Mallya <varun.mallya@abc.random.com",
        "description": "User Relationship Info",
        "used_by": "Income_Calculation_Team",
    },
)

occupational_features = FeatureView(
    name="occupation",
    entities=[user],
    schema=[
        Field(name="Workclass", dtype=String),
        Field(name="Education", dtype=String),
        Field(name="Occupation", dtype=String),
    ],
    ttl=timedelta(days=365),
    source=occupational_features_parquet_file_source,
    tags={
        "authors": "Benjamin Tan <benjamin.tan@abc.random.com, Varun Mallya <varun.mallya@abc.random.com",
        "description": "User Occupation Information",
        "used_by": "Income_Calculation_Team",
    },
)
