from config import client

def budget_node(state):

    query = state["query"]
    history = state["messages"]

    messages = [
        {
            "role": "system",
            "content": """
            You are a Travel Budget Expert.

            Your responsibility is to help users plan affordable trips.

            You should:
            - Estimate travel costs.
            - Suggest budget-friendly destinations.
            - Recommend affordable hotels and transport.
            - Provide an approximate breakdown of expenses.
            - Share money-saving travel tips whenever possible.

            If the user has already shared details such as destination, duration of the trip, number of travellers, or budget in previous messages, use that information while answering instead of asking for it again.
            """
        }
    ]

  
    messages.extend(history)


    messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    return {
        "query": query,
        "response": response.choices[0].message.content,
        "next_node": state["next_node"],
        "messages": history
    }