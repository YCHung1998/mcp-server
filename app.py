import io
import fastmcp

app = fastmcp.FastMCP("My mcp server test", version="1.0.0")

@app.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    app.run()