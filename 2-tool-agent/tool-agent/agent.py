from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="An agent that greets the user",
    instruction="""
    You are a helpfull assistant that can use the following tools:
    - google_search
    """,
    tools=[
        google_search
    ]
    )