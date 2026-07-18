## Overview

This project implements a Multi-Agent System using LangGraph, Groq LLM, and Streamlit.

The system routes the user's query to specialised agents based on the question. Each agent is responsible for a specific travel-related task, resulting in better responses.

The project currently consists of:

- Router Agent
- Destination Agent
- Booking Agent
- Budget Agent

The system also supports multi-turn conversation memory, allowing follow-up questions to retain context from previous interactions.

## Prerequisites

- Python
- LangGraph
- Streamlit
- Groq API Key

## How to create a Groq API Key

1. Go to the Groq website.
2. Sign in to your account.
3. Navigate to API Keys.
4. Generate a new API Key.
5. Create a '.env' file inside the project directory.
6. Store the key as:

GROQ_API_KEY="your_api_key"

The API key is securely loaded in 'config.py'.

## Project Structure

Multi Agent System

- agents – Contains the specialized agents responsible for handling destination, booking, and budget-related queries.
- router – Contains the routing logic that decides which agent should handle the user request.
- graph – Defines the LangGraph workflow and controls the execution between the router and the specialized agents.
- app.py – The main Streamlit application that interacts with the user and invokes the LangGraph.
