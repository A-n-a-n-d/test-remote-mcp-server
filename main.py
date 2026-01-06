import random
from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP(name="Remote Server - Demo2")

# create tool
@mcp.tool # <--- (Red arrow points here)
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll n_dice 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool # <--- (Red arrow points here)
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", host = "0.0.0.0", port = 8000)
