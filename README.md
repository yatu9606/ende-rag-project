# Endee RAG Project

## Overview
This project demonstrates a Retrieval-Augmented Generation (RAG) system using **Endee** as the vector database.
The system performs semantic document retrieval and generates contextual responses using a Large Language Model (LLM).

## Use Case
The application enables:
- Uploading and processing documents
- Converting documents into vector embeddings using Endee
- Retrieving relevant document chunks based on a user query
- Generating accurate and contextual answers using an LLM (RAG pipeline)

This showcases a real-world semantic search and RAG use case where vector similarity search is critical.

## Tech Stack
- Python
- Endee (Vector Database)  
- LangChain
- OpenAI-compatible LLM
- FastAPI (for application interface)
## Architecture
1. Document ingestion
2. Embedding generation
3. Vector storage using Endee
4. Similarity search
5. Response generation using an LLM

## How to Run
```bash
git clone https://github.com/yatu9606/ende-rag-project.git
cd ende-rag-project
pip install -r requirements.txt
python app.py
