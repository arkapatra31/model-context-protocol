# MODEL CONTEXT PROTOCOL

A service built using the Model Context Protocol (MCP) with FastMCP. This project enables users to query real-time weather information for any city using the Tavily search API, as well as access internet usage data by country.

## Setup

### Configure Poetry to create virtual environment

```bash
poetry config virtualenvs.in-project true
```

### Install dependencies

```bash
poetry install
```

### Update dependencies

```bash
poetry update --lock
```

### Features
Get current weather information for any city
Query internet usage data by country
Async API for efficient processing
MCP-based protocol for standardized communication
MongoDB integration for internet usage data

### Project Structure

#### Weather Service
```
➡️weather/weather_mcp_server.py: Defines the FastMCP server with a weather tool
➡️weather/weather_tool.py: Contains utility functions for fetching weather data
➡️weather/__init__.py: Entry point that runs the MCP server
```
#### Internet Usage Service
```
➡️internet_usage/internet_mcp_server.py: Defines the FastMCP server for internet usage data
➡️internet_usage/internet_usage_resource.py: Contains resource definitions and MongoDB connection
➡️internet_usage/__init__.py: Entry point for the internet usage service

📃Resources
The internet usage service provides the following resources:
1️⃣list://resources: Lists all available resources
2️⃣internet-usage://{country}: Retrieves internet usage data for a specific country
```

### Create .env file

```
# Weather service
TAVILY_API_KEY=your_tavily_api_key_here

# Internet usage service
MONGODB_URI=your_mongodb_connection_string
MONGO_DB_NAME=your_database_name
MONGO_DB_COLLECTION=your_collection_name
```

### Usage

#### Weather Service
```
1. Create the MCP server configuration
2. From a MCP Client (Claude Desktop), search for Current weather in <city_name>
```

#### Internet Usage Service
```
1. Create the MCP server configuration
```
```bash
mcp dev .<entry-point internet-usage>
```
