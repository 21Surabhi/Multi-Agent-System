## Overview

This project implements a Multi-Agent AI System using LangGraph, Groq LLM, and Streamlit.

The system routes the user's query to specialised agents based on the question. Each agent is responsible for a specific travel-related task, resulting in better responses.

The project currently consists of:

- Router Agent
- Destination Agent
- Booking Agent
- Budget Agent

The system also supports multi-turn conversation memory, allowing follow-up questions to retain context from previous interactions.


## How the Multi-Agent System works

1. The user inserts a query.
2. The query is then sent to Langgraph.
3. The router analyzes the request.
4. Based on the query, the router selects the most appropriate agent.
5. The selected agent generated the response using Groq LLM.
6. The response generated is sent to the user.
7. The conversation history is saved so that queries can use context.

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

Multi-Agent System

- agents – Contains the specialized agents responsible for handling destination, booking, and budget-related queries.
- router – Contains the routing logic that decides which agent should handle the user request.
- graph – Defines the LangGraph workflow and controls the execution between the router and the specialized agents.
- app.py – The main Streamlit application that interacts with the user and invokes the LangGraph.


## How the router works  

Refer to [router.py](router/router.py)

1. The router receives the user query and conversation history.
2. A routing-specific system prompt is created describing the responsibilities of each agent.
3. The current conversation history is appended to the prompt.
4. The current user query is added.
5. The complete prompt is sent to the Groq LLM.
6. The LLM returns only one routing decision:
   - destination
   - booking
   - budget
7. LangGraph maps execution to the selected agent.

# How the Destination Agent Works

Refer to [destination_agent.py](agent/destination_agent.py)

1. LangGraph invokes the Destination Agent.
2. The current query is extracted
3. Previous conversation history is retrieved.
4. A destination-specific system prompt is created.
5. Previous conversation is appended.
6. The latest user query is added.
7. Groq suggests destinations.
8. Response generated is sent to Langgraph.


# How the Booking Agent Works

Refer to [booking_agent.py](agent/booking_agent.py)

1. LangGraph invokes the Booking Agent.
2. The current query is extracted.
3. Previous conversation history is retrieved.
4. A booking-specific system prompt is created.
5. Previous conversation is appended.
6. The latest user query is added.
7. Groq generates booking recommendations.
8. The response is returned to LangGraph.


# How the Budget Agent Works

Refer to [budget_agent.py](agent/budget_agent.py)

1. LangGraph invokes the Budget Agent.
2. The current query is extracted.
3. Previous conversation history is retrieved.
4. A budget-specific system prompt is created.
5. Previous conversation is appended.
6. The latest user query is added.
7. Groq estimates travel expenses.
8. The generated response is returned to Langgraph.

# How Conversation Memory Works

Refer to [app.py](app.py)

The project maintains two separate conversation histories.

### UI History

st.session_state.messages

This stores:

- User Query
- Selected Agent
- Agent Response

This history is displayed on the Streamlit interface.

### LLM Conversation History

st.session_state.chat_history

This stores conversation using the following format:

- role
- content

This history is passed to LangGraph every time a new query is submitted, allowing agents to understand previous interactions.


# How LangGraph Maintains State

Refer to [travel_graph.py](graph/travel_graph.py)

The graph maintains the following state variables.

- query
- response
- next_node
- messages
