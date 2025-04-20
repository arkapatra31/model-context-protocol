import asyncio
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
load_dotenv()

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

__all__ = [
    get_weather_for_city
]

if __name__ == "__main__":
    # Example usage
    city = "Kolkata"
    weather_info = asyncio.run(get_weather_for_city(city))
    print(weather_info)