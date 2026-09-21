# Local Agent Prototype (Week 01)

A lightweight, local Python agent demonstrating deterministic tool dispatching and safe tool execution without framework overhead[cite: 1].

## Architecture & Data Flow

[User Request] ──> [Agent Loop (agent.py)] ──> [Tool Dispatch (tools.py)] ──> [Tool Execution] ──> [Observation Output]

### Explanation (Request -> Model/Router -> Tool -> Response)
1. **Request:** User passes CLI flags specifying a target tool and argument[cite: 1].
2. **Router:** `agent.py` matches the requested tool against `TOOL_MANIFEST`[cite: 1].
3. **Tool Execution:** `tools.py` runs `calculator()` or `json_lookup()` safely[cite: 1].
4. **Response:** Execution output or error message is returned as an observation[cite: 1].

## Available Tools
* `calculator`: Safely evaluates basic math (`+`, `-`, `*`, `/`) using AST parsing[cite: 1].
* `json_lookup`: Queries key-value pairs from `data.json`[cite: 1].

## Quickstart

```bash
# Test Calculator
python agent.py calculator "12 * 4"

# Test JSON Lookup
python agent.py json_lookup status