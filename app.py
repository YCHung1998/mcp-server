import io
import fastmcp
from core.solver import Solver24

app = fastmcp.FastMCP("My mcp server test", version="1.1.0")
# fastmcp run app.py:app --transport http --port 8000  
# {file_name}:{FastMCP_name}
# app.py:app

@app.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@app.tool
def solve24(n1: int, n2: int, n3: int, n4: int) -> str:
    """Solve 24 game"""
    cards = [n1, n2, n3, n4]
    target = 24
    solver = Solver24(cards, target)
    if solver.solve():
        return solver.result
    else:
        return "No solution found"


if __name__ == "__main__":
    app.run()
