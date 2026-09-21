import ast #(for safe evaluation of expressions)
import json #(for JSON database lookup)
import operator #(for safe arithmetic operations)

# 1. Greeting Function
def get_greeting(name: str) -> str:
    """Returns a personalized greeting."""
    return f"Hello, {name}! Welcome to the agent system."

# 2. Safe Calculator Function
def calculator(expression: str) -> str:
    """Safely evaluates basic arithmetic expressions (+, -, *, /)."""
    allowed_operators = {
        ast.Add: operator.add, 
        ast.Sub: operator.sub,
        ast.Mult: operator.mul, 
        ast.Div: operator.truediv
    }
    try:
        node = ast.parse(expression, mode='eval')
        def _eval(n):
            if isinstance(n, ast.Expression):
                return _eval(n.body)
            elif isinstance(n, ast.BinOp):
                return allowed_operators[type(n.op)](_eval(n.left), _eval(n.right))
            elif isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
                return n.value
            raise ValueError("Invalid mathematical operation.")
        return f"Result: {_eval(node)}"
    except Exception as e:
        return f"Calculator error: {str(e)}"

# 3. Local JSON Lookup Function
def json_lookup(key: str, filepath: str = "data.json") -> str:
    """Retrieves value for a specific key from local JSON database."""
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        val = data.get(key)
        if val is not None:
            return f"Found '{key}': {val}"
        return f"Key '{key}' not found in database."
    except Exception as e:
        return f"Database lookup error: {str(e)}"

# 4. Safe Tool Dispatch Table (Defined AFTER functions)
TOOL_MANIFEST = {
    "calculator": calculator,
    "json_lookup": json_lookup,
    "get_greeting": get_greeting,
}

