from mcp.server.fastmcp import FastMCP
from internet_usage_resource import register_resources
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
logger = logging.getLogger("internet_mcp_server")

load_dotenv()


# Initialize the FastMCP server
mcp: FastMCP = FastMCP("Internet Usage")

# Register resources with the FastMCP server
register_resources(mcp)

__all__ = [mcp]

# Start the FastMCP server
if __name__ == "__main__":
    try:
        mcp.run(transport="stdio")
        logger.info("Internet Usage MCP server started")
    except Exception as e:
        logger.error(f"Failed to run server: {str(e)}")
    finally:
        sys.stdout.flush()