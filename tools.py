from langchain.schema import AIMessage

def math_tool(text):
    try:
        expression = text.lower().split("calculate")[1].strip()
        result = eval(expression)
        return AIMessage(content=f"The result is {result}")
    except Exception as e:
        return AIMessage(content=f"Error in calculation: {str(e)}")
