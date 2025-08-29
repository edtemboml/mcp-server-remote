from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Server", port=3001 )


@mcp.resource('inventory://items/overstock')
def get_overstock_items():
    "Returns a list of overstock items."
    return ["Rice", "Eggs", "Milk", "Hamburgers", "Pasta", "Tomato Sauce", "Bread", "Butter"]


@mcp.tool()
def add(a: int, b: int) -> int:
    "Adds two numbers together."
    return a + b

@mcp.tool()
def say_hello(name: str) -> str:
    "Sends a greeting to the specified name."
    return f"Hello, {name}! What can I do for you today?"




if __name__ == "__main__":
    mcp.run(transport="streamable-http")