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
git clone https://github.com/your-username/AI-Powered-Chatbot.git



Backend
Navigate to the backend folder and install Python dependencies:

```
cd backend
```
```
pip install -r requirements.txt
```

# Frontend
# For the frontend, navigate to the frontend folder and install JavaScript dependencies:

```
cd frontend
```

```
npm install
```

3. Set Up Database
Install MySQL and create a database called chatbot_db.
Use the provided SQL schema to create tables (Products and Suppliers).
Populate the tables with sample data.

4. Run the Application
Start the Backend Server

```
uvicorn app:app --reload
```
```
Start the Frontend Server
```

```
cd frontend
```

```
npm start
```