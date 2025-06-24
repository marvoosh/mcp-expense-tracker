from mcp.server.fastmcp import FastMCP

mcp = FastMCP("expense-tracker")

@mcp.tool()
def say_hello_with_meaning(name: str) -> str:
    return "Hello world!"
