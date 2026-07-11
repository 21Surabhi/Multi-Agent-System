from config import client

def router_node(state):

    query = state["query"]
    history = state["messages"]

    messages = [
        {
            "role": "system",
            "content": """
            You are the routing agent of a travel multi-agent system.

            Your job is to choose exactly ONE agent.

            Available agents:

            booking
            - flight booking
            - hotel booking
            - travel reservations
            - airline recommendations

            destination
            - tourist attractions
            - places to visit
            - travel destinations
            - sightseeing

            budget
            - travel expenses
            - trip budgeting
            - cost estimation
            - cheap travel plans

            Consider the previous conversation as context before making your decision.

            Return ONLY one word:

            booking
            destination
            budget
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

    next_node = response.choices[0].message.content.strip().lower()

    if "booking" in next_node:
        next_node = "booking"

    elif "budget" in next_node:
        next_node = "budget"

    else:
        next_node = "destination"

    return {
        "query": query,
        "response": "",
        "next_node": next_node,
        "messages": history
    }


def route_decision(state):
    return state["next_node"]