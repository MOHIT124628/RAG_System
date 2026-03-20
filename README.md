## Overview

This project implements a Retrieval-Augmented Generation (RAG) system that combines information retrieval with large language models (LLMs) to generate accurate and context-aware answers.

Instead of relying only on pre-trained knowledge, the system retrieves relevant data from a knowledge base and uses it to generate better responses.

## Features

1.Semantic search for retrieving relevant documents
2.Context-aware answer generation using LLM
3.Custom knowledge base support
4.Faster and more accurate responses
5.Combines retrieval + generation pipeline

## Tech Stack

1.Python
2.FAISS/Vector Store
3.Numpy
4.SentenceTransformers
5.LLM(Gemini)

## RAG pipeline

 User Query
     ↓
 Embedding
     ↓
Vector Search (FAISS)
     ↓
Relevant Context
     ↓
    LLM
     ↓
Final Answer