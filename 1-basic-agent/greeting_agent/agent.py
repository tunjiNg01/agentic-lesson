from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="An agent that greets the user",
    instruction="""
    You are a helpfull assistant that ask for the user name, 
    and greets them with their name
    """)