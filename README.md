# Project Setup Guide

## Prerequisites

Before you begin, ensure you have the following installed:

- **MongoDB**: Required for database operations.
- **Docker**: Required if you plan to host the Qdrant vector store locally.

## Setting Up the Environment

1. **Create a Virtual Environment**:
    ```bash
    python3 -m venv <environment_name>
    ```

2. **Activate the Virtual Environment**:
    ```bash
    source <environment_name>/bin/activate
    ```

3. **Install Dependencies**:
    After activating the environment, install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Optional: Hosting Qdrant Vector Store Locally with Docker

If you plan to host the Qdrant vector store locally, follow these steps:

1. **Pull the Qdrant Docker Image and Mount the Volume**:
    ```bash
    sudo docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
    ```

## Loading Nodes into MongoDB and Using Qdrant Vector Store

To load nodes into MongoDB and use the Qdrant vector store, run the following command:

```bash
python load.py
