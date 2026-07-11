from typing import TypedDict
from langgraph.graph import StateGraph, END

from router.router import router_node, route_decision
from agents.destination_agent import destination_node
from agents.booking_agent import booking_node
from agents.budget_agent import budget_node


class TravelState(TypedDict):
    query: str
    response: str
    next_node: str
    messages: list


graph = StateGraph(TravelState)

graph.add_node("router", router_node)
graph.add_node("destination", destination_node)
graph.add_node("booking", booking_node)
graph.add_node("budget", budget_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "destination": "destination",
        "booking": "booking",
        "budget": "budget"
    }
)

graph.add_edge("destination", END)
graph.add_edge("booking", END)
graph.add_edge("budget", END)

app = graph.compile()