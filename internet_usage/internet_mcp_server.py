import asyncio
from mcp.server.fastmcp import FastMCP
from internet_usage_resource import register_resources

# Initialize the FastMCP server
mcp: FastMCP = FastMCP("Internet Usage")

# Register resources with the FastMCP server
register_resources(mcp)

__all__ = [mcp]

# Start the FastMCP server
if __name__ == "__main__":
    mcp.run(transport="stdio")