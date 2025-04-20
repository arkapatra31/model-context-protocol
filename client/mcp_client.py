import asyncio
import logging
import traceback
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("MCP Client")

async def main():
    # Define server parameters
    stderr_file = None
    try:

        server_params = StdioServerParameters(
            command="path\\to\\.venv\\Scripts\\python.exe",
            args=["path\\to\\weather\\__init__.py"],
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
            cwd="path\\to\\client\\"
        )
        logger.debug("Starting Weather MCP client")

        # Connect to server using stdio_client
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize session
                logger.debug("Initializing session")
                await session.initialize()
                logger.debug("Session initialized")

                # List available tools
                logger.debug("Sending ListToolsRequest")
                tools = await session.list_tools()
                logger.info(f"Available tools: {tools}")

                # Call the get_weather tool
                request = {"name": "get_weather", "arguments": {"city": "Kolkata"}}
                logger.debug(f"Sending CallToolRequest: {request}")
                try:
                    result = await asyncio.wait_for(
                        session.call_tool(**request),
                        timeout=10
                    )
                    #logger.info(f"CallToolResponse: {result}")
                    print(f"Response: {result.content}")
                except asyncio.TimeoutError:
                    logger.error("Timeout during CallToolRequest for get_weather")
                    print("Timeout during CallToolRequest for get_weather")

    except Exception as e:
        #logger.error(e)
        logger.error(traceback.format_exc())
    finally:
        pass

if __name__ == "__main__":
    asyncio.run(main())