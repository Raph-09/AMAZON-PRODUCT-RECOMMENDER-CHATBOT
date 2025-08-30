# How the chatbot works



<img width="481" height="401" alt="chatbot" src="https://github.com/user-attachments/assets/5bf495fd-299d-4eaf-bb93-c72af16a699e" />

## Project Documentation

## 1. Introduction

The **Amazon Chatbot** is an AI-powered e-commerce assistant designed to answer product-related queries using a Retrieval-Augmented Generation (RAG) approach. It leverages Amazon product reviews and titles to provide contextually relevant, concise, and helpful responses to user queries.

The system integrates **LangChain**, **HuggingFace embeddings**, **AstraDB vector store**, and **Groq LLM**, with a **Flask-based web interface**. It is containerized with Docker and supports continuous integration/deployment via GitHub Actions and DockerHub.

---

## 2. Project Architecture

### 🔹 Components Overview

1. **Data Processing Layer**

   * `Data_converter.py`: Converts product review data into a structured document format.
   * Input: `amazon_phone_data.csv`
   * Output: List of LangChain `Document` objects with metadata (product names).

2. **Vector Database Layer**

   * `data_ingestion.py`: Handles embedding generation and ingestion into AstraDB vector store.
   * Uses HuggingFace embeddings for document vectorization.
   * Provides option to load existing embeddings or ingest fresh data.

3. **RAG Chain Layer**

   * `rag_chain.py`: Constructs the retrieval-augmented generation (RAG) pipeline.
   * Incorporates conversation history for context-aware responses.
   * Uses `ChatGroq` model for inference.

4. **Application Layer**

   * `app.py`: Flask web application exposing REST endpoints.
   * `/` – Frontend (HTML interface).
   * `/get` – Query endpoint for chatbot responses.
   * `/metrics` – Prometheus-compatible metrics for monitoring.

5. **Deployment Layer**

   * `Dockerfile`: Defines containerization instructions.
   * **GitHub Actions**: Automates build and push to DockerHub.

6. **Utils (Support Layer)**

   * Custom logging and exception handling utilities.

---

## 3. Data Flow

1. **Input Data**: Amazon phone & accessories dataset (20,000 rows).
2. **Preprocessing**:

   * Extract `title_y` (product name) and `text` (review).
   * Convert to `Document` format with metadata.
3. **Embedding Generation**: HuggingFace embeddings transform text into dense vectors.
4. **Storage**: Vectors stored in AstraDB vector store under the `"amazon"` collection.
5. **Retrieval + Generation**:

   * User query → Retriever fetches top-3 similar documents.
   * Chat model processes context + query.
   * Response returned via Flask app.

---

## 4. Code Structure

```
amazon-chatbot/
│── amazon/
│   ├── data_converter.py        # Converts CSV data into Document objects
│   ├── data_ingestion.py        # Ingests/loads data into AstraDB vector store
│   ├── rag_chain.py             # Builds RAG pipeline with history-aware retrieval
│   ├── config.py                # Stores environment variables & configurations
│   ├── utils/                   # Logging & custom exceptions
│
│── app.py                       # Flask application entry point
│── Dockerfile                   # Docker container definition
│── requirements.txt             # Python dependencies
│── .github/workflows/ci.yml     # GitHub Actions CI/CD pipeline
│── amazon_phone_data.csv        # Dataset (20,000 rows)
│── templates/
│   └── index.html               # Frontend UI
```

---

## 5. Installation & Setup

### 🔹 Prerequisites

* Python 3.10+
* Docker & DockerHub account
* AstraDB account (for vector store)
* HuggingFace API key
* Groq API access

### 🔹 Steps

1. **Clone Repository**

```bash
git clone https://github.com/<your-repo>/amazon-chatbot.git
cd amazon-chatbot
```

2. **Set Environment Variables (`.env`)**

```bash
EMBEDDING_MODEL=<huggingface-model>
ASTRA_DB_API_ENDPOINT=<astra-endpoint>
ASTRA_DB_APPLICATION_TOKEN=<astra-token>
ASTRA_DB_KEYSPACE=<astra-keyspace>
RAG_MODEL=<groq-model>
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Locally**

```bash
python app.py
```

App available at: [http://localhost:5000](http://localhost:5000)

5. **Build & Run with Docker**

```bash
docker build -t amazon-chatbot .
docker run -p 5000:5000 amazon-chatbot
```

---

## 6. Usage

* Visit `/` to access chatbot UI.
* Send queries like:

  * *“Which phone has the best battery life?”*
  * *“Are the earphones durable?”*
* `/metrics` exposes monitoring data for Prometheus.

---

## 7. Continuous Integration & Deployment

* **GitHub Actions Workflow**:

  * Triggers on `push`/`pull_request`.
  * Runs linting, tests, and Docker build.
  * Pushes Docker image to DockerHub.

* **Deployment Options**:

  * Local Docker run.
  * Kubernetes / cloud-based deployment.

---

## 8. Logging & Error Handling

* Centralized logging for debugging.
* Custom exceptions in `utils` for structured error reporting.

---

## 9. Future Improvements

* Expand dataset beyond 20k rows.
* Fine-tune embeddings for domain-specific accuracy.
* Add user authentication & personalization.
* Deploy on cloud (AWS/GCP/Azure) with load balancing.
* Extend to multimodal chatbot (images + text).

