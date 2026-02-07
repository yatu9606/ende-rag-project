# Endee RAG Project

## Overview
This project demonstrates a Retrieval-Augmented Generation (RAG) system using Endee as the vector database.
The system allows semantic retrieval of documents and generates contextual responses using an LLM.

## Use Case
Example:
- Upload documents
- Convert them into vector embeddings using Endee
- Retrieve relevant chunks based on user query
- Generate answers using an LLM (RAG pipeline)

## Tech Stack     
- Python
- Endee (Vector Database)
- LangChain / OpenAI / HuggingFace (mention what you used)
- FastAPI / Streamlit (if used)

## Architecture
1. Document ingestion
2. Embedding generation
3. Vector storage using Endee
4. Similarity search
5. Response generation

## How to Run
```bash
git clone https://github.com/yatu9606/ende-rag-project.git
cd ende-rag-project
pip install -r requirements.txt
python app.py
