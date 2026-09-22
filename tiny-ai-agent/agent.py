import sys # (for command-line argument parsing)
from tools import TOOL_MANIFEST, get_greeting


def run_agent(tool_name: str, argument: str):
    """
    Executes a registered tool and returns the result.
    """

    print(f"[Agent Loop] Received tool request: '{tool_name}' with argument: '{argument}'")

    if tool_name not in TOOL_MANIFEST:
        print(f"[Agent Loop] Error: Tool '{tool_name}' is not registered.")
        return

    tool_func = TOOL_MANIFEST[tool_name]
    observation = tool_func(argument)

    print(f"[Agent Loop] Execution Result: {observation}")


if __name__ == "__main__":

    # Default greeting when the agent starts
    print(get_greeting("Karim"))

    print("Type 'exit' to close the agent.")
    print()

    # Keep the agent running
    while True:

        user_input = input("Agent > ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        # Expected format:
        # tool_name argument
        parts = user_input.split(" ", 1)

        if len(parts) < 2:
            print("Usage: <tool_name> <argument>")
            continue

        tool_name = parts[0]
        argument = parts[1]

        run_agent(tool_name, argument)
