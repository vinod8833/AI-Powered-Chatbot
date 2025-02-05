# AI-Powered Chatbot for Supplier and Product Information

This project is an AI-powered chatbot that helps users find information about products and suppliers. The chatbot uses natural language to answer queries and fetch data from a MySQL database. It also uses a machine learning model (LLM) to summarize the information.

## Features
- **Query Supplier & Product Information**: Ask questions like:
  - "Show me all products under brand X."
  - "Which suppliers provide laptops?"
  - "Give me details of product ABC."
- **Summarized Answers**: The chatbot uses AI to summarize the data in a simple way.
- **Database Integration**: Data is fetched from a MySQL database containing product and supplier information.

## Tech Stack
- **Frontend**: React, Material UI or Tailwind CSS
- **Backend**: Python, LangGraph, FastAPI/Flask
- **Database**: MySQL/PostgreSQL
- **AI Model**: Hugging Face's GPT-2/3 or LLaMA 2 for summarization

## Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/vinod8833/AI-Powered-Chatbot.git
```

```bash
cd backend
pip install -r requirements.txt
```

```bash
cd frontend
npm install

```

```bash
cd backend
uvicorn app:app --reload

```

```bash
cd frontend
npm start
```