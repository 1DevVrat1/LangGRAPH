from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain.chat_models import ChatOpenAI
from tools import math_tool
from memory import SimpleMemory

# Initialize LLM
llm = ChatOpenAI(temperature=0.7, model="gpt-4")

# Tool calling function
def agent_step(state):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": add_messages(messages, response)}

# Tool node
def tool_node(state):
    last_msg = state["messages"][-1]
    if "calculate" in last_msg.content.lower():
        result = math_tool(last_msg.content)
        return {"messages": add_messages(state["messages"], result)}
    return state

# Create memory
memory = SimpleMemory()

# Define Graph
builder = StateGraph()
builder.add_node("agent", agent_step)
builder.add_node("tool", tool_node)

builder.set_entry_point("agent")
builder.add_edge("agent", "tool")
builder.add_edge("tool", END)

# Compile Graph
graph = builder.compile()

# Run
if __name__ == "__main__":
    input_message = {"messages": [{"role": "user", "content": "Can you calculate 12 * 8 for me?"}]}
    output = graph.invoke(input_message)
    print("Final Output:", output["messages"][-1].content)
