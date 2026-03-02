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
def solve24(n1: str, n2: str, n3: str, n4: str) -> str:
    """Solve 24 game. Supports numbers (1-10) and card symbols (A, J, Q, K)."""
    cards = [n1, n2, n3, n4]
    target = 24
    solver = Solver24(cards, target)
    solutions = solver.solve()
    if solutions:
        return f"Found solutions: {', '.join(solutions)}"
    else:
        return f"No solution found for cards: {', '.join(map(str, cards))}"


if __name__ == "__main__":
    app.run()
    # print(solve24("A", "A", "A", "A"))  # no solution
    # print(solve24("Q", "K", "A", "A"))  # no solution
