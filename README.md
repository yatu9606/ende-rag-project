# Endee-Based Semantic Search Project

## Project Overview
This project implements a **Semantic Search system** using **Endee** as the vector database.  
It demonstrates how textual data can be converted into vector embeddings and searched using **semantic similarity** instead of traditional keyword matching.

The project is developed as part of the **Endee Labs project-based evaluation**, where vector search is the core AI/ML component.

---

## Problem Statement
Keyword-based search systems fail to understand the meaning and context of user queries.  
This results in poor search accuracy when different words are used to express the same idea.

This project solves the problem by using:
- Vector embeddings
- Similarity-based retrieval
- A vector database (Endee)

---

## Use Case
- Semantic document search  
- Knowledge retrieval systems  
- Foundation for Retrieval Augmented Generation (RAG)  
- AI assistants and recommendation systems  

---

## Solution Approach
1. Input documents are read from a text file  
2. Documents are converted into vector embeddings using Sentence Transformers  
3. Embeddings are stored in an Endee-based vector store  
4. User queries are embedded using the same model  
5. Cosine similarity is used to retrieve the most relevant documents  

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
This allows Endee to be used effectively within a Python-based AI/ML application.

---

## Project Structure
