from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team

# ------------------ Tool 1: Technical Support Tool ------------------
class TechnicalSupportTool:
    __name__ = "TechnicalSupportTool"

    def __call__(self, query: str) -> str:
        responses = {
            "app crash": "Please try reinstalling the app and update your OS.",
            "login issue": "Try resetting your password using the 'Forgot Password' link.",
            "freezing": "Clear the app cache and restart your device.",
        }
        for keyword, response in responses.items():
            if keyword in query.lower():
                return response
        return "Please provide more details about the technical issue."

# ------------------ Tool 2: Sales Support Tool ------------------
class SalesTool:
    __name__ = "SalesTool"

    def __call__(self, query: str) -> str:
        responses = {
            "cost": "Our premium plan costs $49.99/month with 24/7 support.",
            "discount": "Yes! We are offering 20% off for new users this week.",
            "pricing": "We have Basic, Pro, and Premium plans starting at $9.99/month.",
        }
        for keyword, response in responses.items():
            if keyword in query.lower():
                return response
        return "Let me connect you to a sales representative for more details."

# ------------------ Tool 3: General Inquiry Tool ------------------
class GeneralInfoTool:
    __name__ = "GeneralInfoTool"

    def __call__(self, query: str) -> str:
        responses = {
            "hours": "We are open from 9 AM to 6 PM, Monday to Friday.",
            "location": "Our headquarters are located in San Francisco, CA.",
            "contact": "You can contact us at support@example.com or call 1800-123-456.",
        }
        for keyword, response in responses.items():
            if keyword in query.lower():
                return response
        return "Can you clarify your question? I'm here to help."

# ------------------ Agent 1: Technical Support Agent ------------------
tech_agent = Agent(
    name="Tech Support Agent",
    role="Handle technical issues",
    model=OpenAIChat(id="gpt-4o"),
    tools=[TechnicalSupportTool()],
    instructions="Use the technical support tool to answer user queries. Keep responses helpful and simple. Provide them direct answer using the tool, do not ask further questions. Provide short answer in less than two lines.",
    show_tool_calls=True,
    markdown=True,
)

# ------------------ Agent 2: Sales Agent ------------------
sales_agent = Agent(
    name="Sales Agent",
    role="Handle pricing and sales questions",
    model=OpenAIChat(id="gpt-4o"),
    tools=[SalesTool()],
    instructions="Use the sales tool to answer pricing and discount-related questions. Provide them direct answer using the tool, do not ask further questions. Provide short answer in less than two lines.",
    show_tool_calls=True,
    markdown=True,
)

# ------------------ Agent 3: General Inquiry Agent ------------------
general_agent = Agent(
    name="General Inquiry Agent",
    role="Answer general questions like hours, location, and contact info",
    model=OpenAIChat(id="gpt-4o"),
    tools=[GeneralInfoTool()],
    instructions="Use the general info tool to help with common inquiries. Provide them direct answer using the tool, do not ask further questions. Provide short answer in less than two lines.",
    show_tool_calls=True,
    markdown=True,
)

# ------------------ Router Team ------------------
router_team = Team(
    name="Customer Care Chatbot Agent",
    mode="route",
    members=[tech_agent, sales_agent, general_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions="Route the query to the correct agent based on whether it’s technical, sales, or general.",
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True,
)

# ------------------ Test Cases ------------------
# print("\n--- TEST 1: TECHNICAL ---")
# router_team.print_response("My app keeps freezing whenever I try to open settings.", stream=True)

# print("\n--- TEST 2: SALES ---")
# router_team.print_response("Do you have any ongoing discounts on the premium plan?", stream=True)

print("\n--- TEST 3: GENERAL INFO ---")
router_team.print_response("What are your business hours on weekdays?", stream=True)
