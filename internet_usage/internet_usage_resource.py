import os
from dotenv import load_dotenv
from pymongo import MongoClient
from mcp.server.fastmcp import FastMCP

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client.get_database(name=os.getenv("MONGO_DB_NAME"))
collection = db.get_collection(name=os.getenv("MONGO_DB_COLLECTION"))

def register_resources(mcp: FastMCP):
    """
    Register resources with the FastMCP server.
    """
    # List available resources
    @mcp.resource("list://resources")
    def list_resources():
        """
        List all resources.
        """
        return {
            "resources": [
                {
                    "uri": "internet-usage://{country}",
                    "name": "Internet Usage by Country",
                    "description": "Internet Usage by Country",
                    "mime_type": "application/json"
                }
            ]
        }

    @mcp.resource("internet-usage://{country}")
    def get_internet_usage(country: str):
        """
        Get entire internet usage by country.
        """
        # Exclude the "_id" field from the response
        return collection.find_one({"Country Name": country}, {"_id": 0})

__all__ = [register_resources]