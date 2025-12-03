import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(command="mcp", args=["run", "demo_server.py"], env=None)


def extract_content(payload):
    """Best-effort to pull text from MCP responses."""
    if hasattr(payload, "contents"):
        contents = payload.contents
        if contents:
            first = contents[0]
            if hasattr(first, "text"):
                return first.text
            if isinstance(first, dict) and "text" in first:
                return first["text"]
            return str(first)
    if hasattr(payload, "content"):
        return payload.content
    return str(payload)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
          print("2) Initialize session")
          await session.initialize()
            # TODO: list resources and print their URIs
          print("3) Discover resources and tools")
          resources = await session.list_resources()
          print("Resources:")
          for resource in resources.resources:
              print(f"3.1) - {resource.uri}")   

            # TODO: list tools and print their names
          print("Tools:")
          tools = await session.list_tools()
          for tool in tools.tools:
                    print(f"3.2) - {tool.name}: {tool.inputSchema.get('properties', {})}")

            # TODO: read greeting://hello and print the content
          greeting = await session.read_resource("greeting://hello")
          print(f"4) read greeting://hello = {extract_content(greeting)}")

            # TODO: call add with a=1, b=7 and print the result
          result = await session.call_tool("add", arguments={"a": 1, "b": 7})
          print(f"5) add(1,7) = {extract_content(result)}")

if __name__ == "__main__":
    asyncio.run(run())