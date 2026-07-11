import streamlit as st
from graph.travel_graph import app

st.set_page_config(
    page_title="Multi Agent System",
    layout="centered"
)

st.title("Multi Agent System")
st.write("Interact with your multi-agent system for your queries!")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.messages:

    st.markdown(f"**You:** {message['query']}")
    st.markdown(f"**Selected Agent:** {message['agent']}")
    st.markdown("**Response:**")
    st.write(message["response"])

    st.divider()

query = st.chat_input("Ask your question")

if query:

    result = app.invoke(
        {
            "query": query,
            "response": "",
            "next_node": "",
            "messages": st.session_state.chat_history
        }
    )

    st.session_state.messages.append(
        {
            "query": query,
            "agent": result["next_node"],
            "response": result["response"]
        }
    )

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": query
        }
    )

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": result["response"]
        }
    )

    st.markdown(f"**You:** {query}")
    st.markdown(f"**Selected Agent:** {result['next_node']}")
    st.markdown("**Response:**")
    st.write(result["response"])

    st.divider()