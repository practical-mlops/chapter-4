import os
from minio import Minio
import argparse
from pathlib import Path


def push_config_to_minio(
    feature_store_path: str,
    bucket_name: str,
    minio_endpoint: str,
    access_key: str,
    secret_key: str,
    secure: bool = True,
):
    """
    Push feature store config YAML to MinIO bucket

    Args:
        feature_store_path: Path to feature_store.yaml file
        bucket_name: Name of the MinIO bucket
        minio_endpoint: MinIO server endpoint
        access_key: MinIO access key
        secret_key: MinIO secret key
        secure: Use HTTPS if True, HTTP if False
    """
    # Initialize MinIO client
    client = Minio(
        endpoint=minio_endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=secure,
    )

    # Create bucket if it doesn't exist
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print(f"Created bucket: {bucket_name}")

    # Upload the file
    file_path = Path(feature_store_path)
    if not file_path.exists():
        raise FileNotFoundError(
            f"Feature store config not found at: {feature_store_path}"
        )

    object_name = "feature_store.yaml"
    client.fput_object(
        bucket_name=bucket_name, object_name=object_name, file_path=str(file_path)
    )
    print(f"Successfully uploaded {object_name} to bucket {bucket_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Push feature store config to MinIO")
    parser.add_argument(
        "--feature-store-path", required=True, help="Path to feature_store.yaml"
    )
    parser.add_argument("--bucket-name", required=True, help="MinIO bucket name")
    parser.add_argument("--minio-endpoint", required=True, help="MinIO endpoint")
    parser.add_argument("--access-key", required=True, help="MinIO access key")
    parser.add_argument("--secret-key", required=True, help="MinIO secret key")
    parser.add_argument(
        "--insecure", action="store_true", help="Use HTTP instead of HTTPS"
    )

    args = parser.parse_args()

    push_config_to_minio(
        feature_store_path=args.feature_store_path,
        bucket_name=args.bucket_name,
        minio_endpoint=args.minio_endpoint,
        access_key=args.access_key,
        secret_key=args.secret_key,
        secure=not args.insecure,
    )
