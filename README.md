# Python Analytics Template

Starter project for Python analytics work at ABUHB. Includes a devcontainer pre-configured with GCP tooling (BigQuery, GCS, Vertex AI, Secret Manager).

---

## Quick Start

1. Click **Use this template** → create your repo
2. Open in GitHub Codespaces (or VS Code with Dev Containers extension)
3. Authenticate with GCP (see [GCP Login](#gcp-login) below)
4. Start coding in `src/`

---

## Folder Structure

```
.
├── .devcontainer/       # Codespaces / Dev Container config
├── src/                 # Your Python source code
├── notebooks/           # Jupyter notebooks for exploration
├── tests/               # Unit tests
├── data/                # Local sample data (gitignored)
├── scripts/             # Utility/run scripts
├── requirements.txt     # Python dependencies
└── .env.example         # Environment variable template
```

---

## GCP Login

### Option 1 — Application Default Credentials (recommended for Codespaces)

```bash
gcloud auth application-default login
```

This opens a browser flow and stores credentials locally. All GCP client libraries pick these up automatically.

### Option 2 — Service Account Key (CI / non-interactive)

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
```

Never commit service account keys. Add to `.gitignore` and use Secret Manager or GitHub Secrets instead.

### Option 3 — Workload Identity (Cloud Run / GKE)

No credentials needed — the runtime service account is used automatically.

### Verify your auth

```bash
gcloud auth list
gcloud config get-value project
```

---

## GCP Services

### BigQuery

```python
from google.cloud import bigquery

client = bigquery.Client(project="your-gcp-project")

query = """
    SELECT *
    FROM `your-project.your_dataset.your_table`
    LIMIT 100
"""

df = client.query(query).to_dataframe()
```

### Cloud Storage (GCS)

```python
from google.cloud import storage

client = storage.Client()
bucket = client.bucket("your-bucket-name")
blob = bucket.blob("path/to/file.csv")
blob.download_to_filename("local_file.csv")
```

### Secret Manager

```python
from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()
name = "projects/your-project/secrets/your-secret/versions/latest"
response = client.access_secret_version(request={"name": name})
value = response.payload.data.decode("UTF-8")
```

### Vertex AI

```python
from google.cloud import aiplatform

aiplatform.init(project="your-gcp-project", location="europe-west2")
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in your values. Never commit `.env`.

```bash
cp .env.example .env
```

---

## Running Tests

```bash
pytest tests/
```
