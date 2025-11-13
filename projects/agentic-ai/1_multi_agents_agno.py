

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.team import Team

# Simulated inventory lookup tool
class InventoryTool:
    __name__ = "InventoryTool"
    
    def __call__(self, product_name: str) -> str:
        inventory = {
            "iPhone 15": "In stock (Ships in 2 days)",
            "AirPods Pro": "Out of stock (Available in 2 weeks)",
            "MacBook Air M3": "Low stock (Only 3 left!)",
        }
        return inventory.get(product_name, "Product not found in inventory.")

# Agent 1: Handles customer FAQs and policy questions
faq_agent = Agent(
    name="FAQ Agent",
    role="Answer customer questions using web search",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Answer e-commerce related queries using web search. Use Best Buy store if someone is asking about electronics. Include source if possible.",
    show_tool_calls=True,
    markdown=True,
)

# Agent 2: Checks product stock availability
inventory_agent = Agent(
    name="Inventory Agent",
    role="Check inventory for a given product",
    model=OpenAIChat(id="gpt-4o"),
    tools=[InventoryTool()],
    instructions="Only respond with inventory status of the product.",
    show_tool_calls=True,
    markdown=True,
)

# Multi-agent team coordination
support_team = Team(
    mode="coordinate",
    members=[faq_agent, inventory_agent],
    model=OpenAIChat(id="gpt-4o"),
    success_criteria="A complete and helpful customer support response with product stock status and policy explanation.",
    instructions=["Be polite", "Include product availability and any relevant policies"],
    show_tool_calls=True,
    markdown=True,
)

# Sample query
support_team.print_response(
    "Is the iPhone 15 in stock? Also, what's your return policy on electronics?",
    stream=True
)

