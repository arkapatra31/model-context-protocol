from weather_mcp_server import mcp
import sys
import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("weather_init")

if __name__ == "__main__":
    logger.info("Initializing Weather MCP server")
    try:
        mcp.run(transport="stdio")
        logger.info("Weather MCP server started")
    except Exception as e:
        logger.error(f"Failed to run server: {str(e)}")
    finally:
        sys.stdout.flush()