from internet_mcp_server import mcp
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
    try:
        mcp.run(transport="stdio")
        logger.info("Internet Usage MCP server started")
    except Exception as e:
        logger.error(f"Failed to run server: {str(e)}")
    finally:
        sys.stdout.flush()