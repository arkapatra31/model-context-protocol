from mcp.server.fastmcp import FastMCP
from weather_tool import get_weather_for_city
from dotenv import load_dotenv
import logging
import sys

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("weather_mcp_server")

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
    logger.debug(f"Processing get_weather tool with city: {city}")
    try:
        result = await get_weather_for_city(city)
        logger.debug(f"Query result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        return f"Error: {str(e)}"

__all__ = ['mcp']

if __name__ == "__main__":
    logger.info("Starting Weather MCP server with stdio transport")
    try:
        mcp.run(transport="stdio")
        logger.info("Weather MCP server started")
    except Exception as e:
        logger.error(f"Failed to run server: {str(e)}")
    finally:
        sys.stdout.flush()