from __future__ import annotations
"""
Minimal MCP Server Library
============================
Standalone MCP JSON-RPC implementation over stdin/stdout.
No pip dependencies required.

Implements:
    - initialize handshake
    - tools/list
    - tools/call
    - Proper JSON-RPC 2.0 framing
"""

import sys
import json
import inspect
from typing import Any, Callable


def tool(name: str, description: str):
    """Decorator to register a method as an MCP tool."""
    def decorator(func):
        func._mcp_tool = True
        func._mcp_name = name
        func._mcp_description = description
        return func
    return decorator


class MCPServer:
    """Base class for MCP servers. Subclass and add @tool methods."""

    def __init__(self, name: str, description: str, version: str = "1.0.0"):
        self._name = name
        self._description = description
        self._version = version
        self._tools = {}
        self._discover_tools()

    def _discover_tools(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, '_mcp_tool'):
                self._tools[attr._mcp_name] = {
                    "func": attr,
                    "name": attr._mcp_name,
                    "description": attr._mcp_description,
                    "schema": self._extract_schema(attr),
                }

    def _extract_schema(self, func) -> dict:
        """Extract JSON Schema from function signature."""
        sig = inspect.signature(func)
        properties = {}
        required = []
        for param_name, param in sig.parameters.items():
            if param_name == "self":
                continue
            prop = {}
            annotation = param.annotation
            if annotation == str or annotation == inspect.Parameter.empty:
                prop["type"] = "string"
            elif annotation == int:
                prop["type"] = "integer"
            elif annotation == float:
                prop["type"] = "number"
            elif annotation == bool:
                prop["type"] = "boolean"
            elif annotation == list:
                prop["type"] = "array"
                prop["items"] = {"type": "string"}
            elif annotation == dict:
                prop["type"] = "object"
            else:
                prop["type"] = "string"

            if param.default == inspect.Parameter.empty:
                required.append(param_name)
            properties[param_name] = prop

        return {
            "type": "object",
            "properties": properties,
            "required": required,
        }

    def _handle_message(self, msg: dict) -> dict:
        method = msg.get("method", "")
        msg_id = msg.get("id")
        params = msg.get("params", {})

        if method == "initialize":
            return self._respond(msg_id, {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": self._name,
                    "version": self._version,
                },
            })

        if method == "notifications/initialized":
            return None  # notification, no response

        if method == "tools/list":
            tools = []
            for t in self._tools.values():
                tools.append({
                    "name": t["name"],
                    "description": t["description"],
                    "inputSchema": t["schema"],
                })
            return self._respond(msg_id, {"tools": tools})

        if method == "tools/call":
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            if tool_name not in self._tools:
                return self._error(msg_id, -32602, "Unknown tool: %s" % tool_name)
            try:
                result = self._tools[tool_name]["func"](**arguments)
                content = json.dumps(result, default=str) if not isinstance(result, str) else result
                return self._respond(msg_id, {
                    "content": [{"type": "text", "text": content}],
                })
            except Exception as e:
                return self._error(msg_id, -32603, str(e))

        if method == "ping":
            return self._respond(msg_id, {})

        return self._error(msg_id, -32601, "Unknown method: %s" % method)

    def _respond(self, msg_id, result):
        return {"jsonrpc": "2.0", "id": msg_id, "result": result}

    def _error(self, msg_id, code, message):
        return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": code, "message": message}}

    def run(self):
        """Run the MCP server over stdin/stdout."""
        sys.stderr.write("[%s] MCP server started (%d tools)\n" % (self._name, len(self._tools)))
        sys.stderr.flush()

        buf = ""
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                buf += line
                # Try to parse accumulated buffer as JSON
                try:
                    msg = json.loads(buf)
                    buf = ""
                except json.JSONDecodeError:
                    continue

                response = self._handle_message(msg)
                if response is not None:
                    sys.stdout.write(json.dumps(response) + "\n")
                    sys.stdout.flush()
            except KeyboardInterrupt:
                break
            except Exception as e:
                sys.stderr.write("[%s] Error: %s\n" % (self._name, e))
                sys.stderr.flush()
