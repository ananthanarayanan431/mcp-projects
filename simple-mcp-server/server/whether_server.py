
from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Server")

@mcp.tool()
async def get_whether(location:str)->str:
    """Get whether for particluar location"""

    return f"it's time for hyderabad! -{location}"

if __name__ == "__main__":
    mcp.run(transport="sse")