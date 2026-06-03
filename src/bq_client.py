"""Reusable BigQuery client helper."""
from google.cloud import bigquery


def get_client(project: str) -> bigquery.Client:
    """Return an authenticated BigQuery client."""
    return bigquery.Client(project=project)


def query_to_df(client: bigquery.Client, sql: str):
    """Run a SQL query and return results as a pandas DataFrame."""
    return client.query(sql).to_dataframe()
