from config import client

def booking_node(state):

    query = state["query"]
    history = state["messages"]

    messages = [
        {
            "role": "system",
            "content": """
            You are a Travel Booking Expert.

            Your responsibility is to assist users with booking-related travel queries.

            You should:
            - Recommend flights and airlines.
            - Suggest hotels based on user preferences.
            - Help with travel reservations.
            - Ask for missing details such as destination, travel dates, number of travellers, or budget before making recommendations.
            - Provide clear and practical booking guidance.

            If the user has already mentioned details such as destination, dates, or budget earlier in the conversation, use that information instead of asking again.
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