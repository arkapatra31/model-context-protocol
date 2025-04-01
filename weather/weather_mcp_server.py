from mcp.server.fastmcp import FastMCP
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("weather")

async def get_weather_for_city(city: str):
    """
    Fetches the weather for a given city using the FastMCP API.

    Args:
        city (str): The name of the city to fetch the weather for.

    Returns:
        str: The weather information for the specified city.
    """
    search = TavilySearchResults(max_results=1)
    response = await search.arun(f"What is the current weather in {city}")
    if response:
        return response[0]

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get the current weather for a given city.

    Args:
        city (str): The name of the city to get the weather for.

    Returns:
        str: A string describing the current weather in the city.
    """
    return await get_weather_for_city(city)

__all__ = [mcp]

if __name__ == "__main__":
    mcp.run(transport='stdio')