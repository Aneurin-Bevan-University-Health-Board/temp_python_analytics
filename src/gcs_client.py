"""Reusable GCS helper."""
from google.cloud import storage


def download_blob(bucket_name: str, blob_name: str, destination: str) -> None:
    """Download a GCS blob to a local file."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(destination)
    print(f"Downloaded gs://{bucket_name}/{blob_name} -> {destination}")


def upload_blob(bucket_name: str, source_file: str, destination_blob: str) -> None:
    """Upload a local file to GCS."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(source_file)
    print(f"Uploaded {source_file} -> gs://{bucket_name}/{destination_blob}")
