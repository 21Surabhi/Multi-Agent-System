from config import client

def destination_node(state):

    query = state["query"]
    history = state["messages"]

    messages = [
        {
            "role": "system",
            "content": """
            You are a Travel Destination Expert.

            Your responsibility is to help users discover suitable travel destinations based on their interests.

            You should:
            - Recommend destinations and tourist attractions.
            - Suggest famous landmarks and activities.
            - Share useful travel tips.
            - Mention the best time to visit whenever relevant.
            - Keep your answers informative and easy to understand.

            If the user asks a broad question, suggest multiple destinations with a short description for each.
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