# MODEL CONTEXT PROTOCOL

A weather information service built using the Model Context Protocol (MCP) with FastMCP. This project enables users to query real-time weather information for any city using the Tavily search API.
poetry config virtualenvs.in-project true

## Configure Poetry to create virtual environment

### Configure Poetry to create virtual environments in the project directory
```
poetry config virtualenvs.in-project true
```

### Install dependencies
```
poetry install
```

### Update dependencies and lock file
```
poetry update --lock
```

## Features

- Get current weather information for any city
- Async API for efficient processing
- MCP-based protocol for standardized communication

## Project Structure

- `weather/weather_mcp_server.py`: Defines the FastMCP server with a weather tool
- `weather/weather_tool.py`: Contains utility functions for fetching weather data
- `weather/__init__.py`: Entry point that runs the MCP server