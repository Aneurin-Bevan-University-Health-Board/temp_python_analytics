FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

RUN apt-get update \\
    && apt-get install -y --no-install-recommends ca-certificates curl gnupg \\
    && curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \\
        | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg \\
    && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \\
        > /etc/apt/sources.list.d/google-cloud-sdk.list \\
    && apt-get update \\
    && apt-get install -y --no-install-recommends google-cloud-cli \\
    && rm -rf /var/lib/apt/lists/*