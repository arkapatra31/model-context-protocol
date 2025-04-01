from mcp.server.fastmcp import FastMCP
from weather_tool import  get_weather_for_city
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("Weather Status")

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