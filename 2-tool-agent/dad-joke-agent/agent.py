from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

# New resource discovered:
# - get_current_time
def get_current_time():
    
    """
     Get the current time in the format "YYYY-MM-DD HH:MM:SS".
    """
    return {
      "current_time":  datetime.now().strftime("%Y-%m-%d %H:%M:%S")        
    }

root_agent = Agent(
    name="dad-joke-agent",
    model="gemini-2.0-flash",
    description="An agent that tells jokes",
    instruction="""
    You are a helpfull assistant that can use the following tools:
    - get_current_time
    """,
    tools=[
        get_current_time
    ]
    )