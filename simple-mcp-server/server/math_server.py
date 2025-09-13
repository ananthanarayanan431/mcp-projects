
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)->int:
    """Add Two Numbers"""

    return a + b


@mcp.tool()
def multiply(a:int, b:int)->int:
    """Multiply any two number"""

    return a*b

@mcp.tool()
def sub(a:int, b:int)->int:
    """Substract any two numbers"""

    return abs(a-b)

if __name__ == "__main__":
    mcp.run(transport="stdio")