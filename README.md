# Endee-Based Semantic Search System

## Project Overview
This project implements a **Semantic Search system** using **Endee** as the vector database.  
It demonstrates how textual data can be converted into vector embeddings and retrieved using **semantic similarity** instead of traditional keyword-based search.

The project is developed as part of the **Endee Labs project-based evaluation**, where vector search is the core AI/ML component.

---

## Problem Statement
Traditional keyword-based search systems fail to understand the meaning and context of user queries.  
This leads to inaccurate results when the same idea is expressed using different words.

This project solves the problem using:
- Vector embeddings
- Similarity-based retrieval
- A vector database (Endee)

---

## Use Case
- Semantic document search  
- Knowledge retrieval systems  
- Foundation for Retrieval-Augmented Generation (RAG)  
- AI assistants and recommendation systems  

---

## Solution Approach
1. Load text documents from a file  
2. Convert documents into vector embeddings using Sentence Transformers  
3. Store embeddings in an Endee-based vector store  
4. Convert user queries into embeddings  
5. Retrieve top-k relevant documents using cosine similarity  

---

## Technology Stack
- Python 3.10  
- Endee (Vector Database – conceptual integration)  
- SentenceTransformers  
- all-MiniLM-L6-v2 embedding model  
- PyTorch (CPU-only)  
- NumPy  
- Scikit-learn  

---

## Endee Integration
Endee is a **C++-based vector database engine**.  
For this project, a **Python adapter layer** is implemented to represent Endee’s vector storage and similarity search concepts.  
This allows Endee to be used effectively within a Python-based AI/ML workflow.

---

## Project Structure
ende-rag-project/
│── endee/
│ └── vector_store.py # Python adapter for Endee
│
│── data/
│ └── documents.txt # Input text documents
│
│── ingest.py # Converts text into embeddings
│── query.py # Semantic search logic
│── app.py # End-to-end execution
│
│── requirements.txt
│── README.md

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ende-rag-project.git
cd ende-rag-project
2. Create and activate virtual environment
py -3.10 -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

How to Run

Run the full semantic search pipeline:

python app.py


The application will:

Ingest documents

Store embeddings in the vector store

Allow interactive semantic search

Example Queries
What is Endee?
Explain semantic search
What is RAG?
Why are vector databases important?
How do embeddings work?

Sample Output
Top Results:
1. Semantic search retrieves documents based on meaning rather than keywords.
2. Vector databases are essential for modern AI systems.

Future Enhancements

Full Retrieval-Augmented Generation (RAG) using LLMs

Support for PDF and CSV ingestion

REST API using FastAPI

Persistent vector storage

Agentic AI workflows