from   fastmcp import FastMCP
import asyncio
import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("Server")

@mcp.resource('inventory://items/overstock')
def get_overstock_items():
    "Returns a list of overstock items."
    return ["Rice", "Eggs", "Milk","Candy","Lettuce",  "Hamburgers", "Pasta", "Tomato Sauce", "Bread", "Butter"]

@mcp.tool()
def add(a: int, b: int) -> int:
    """Use this to add two numbers together.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The sum of the two numbers.
    """
    logger.info(f">>> Tool: 'add' called with numbers '{a}' and '{b}'")
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Use this to subtract two numbers.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The difference of the two numbers.
    """
    logger.info(f">>> Tool: 'subtract' called with numbers '{a}' and '{b}'")
    return a - b


@mcp.tool()
def say_hello(name: str) -> str:
    "Sends a greeting to the specified name."
    return f"Hello, {name}! What can I do for you today?"


if __name__ == "__main__":

    asyncio.run(mcp.run_async(transport="streamable-http", 
                              host="0.0.0.0", 
                              port=os.getenv("REMOTE-MCP-SERVER-PORT", 8080)
                              )
    )