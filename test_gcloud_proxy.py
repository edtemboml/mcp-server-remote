import asyncio

from fastmcp import Client
from mcp.types import CallToolResult


async def safely_extract_text(result: CallToolResult) -> str:
    """Safely extract text with error handling"""
    
    try:
        if not result:
            return ""
        
        if not hasattr(result, 'content') or not result.content:
            return ""
        
        text_content = []
        
        for item in result.content:
            try:
                if hasattr(item, 'type') and item.type == 'text':
                    text_content.append(item.text)
                elif hasattr(item, 'text'):
                    text_content.append(item.text)
                else:
                    # Try to extract any string-like content
                    str_content = str(item)
                    if str_content and str_content != str(type(item)):
                        text_content.append(str_content)
            except Exception as e:
                print(f"Warning: Could not extract text from item: {e}")
                continue
        
        return '\n'.join(text_content)
        
    except Exception as e:
        print(f"Error extracting text from CallToolResult: {e}")
        return ""



async def test_server():
    # Test the MCP server using streamable-http transport.
    # Use "/sse" endpoint if using sse transport.
    async with Client("http://localhost:8080/mcp") as client:
        # List available tools
        tools = await client.list_tools()
        for tool in tools:
            print(f">>> Tool found: {tool.name}")
        # Call add tool
        print(">>>  Calling add tool for 1 + 2")
        result = await client.call_tool("add", {"a": 1, "b": 2})
        print(f"<<<  Result: {await safely_extract_text(result)}")
        # Call subtract tool
        print(">>>  Calling subtract tool for 10 - 3")
        result = await client.call_tool("subtract", {"a": 10, "b": 3})
        print(f"<<< Result: {await safely_extract_text(result)}")

if __name__ == "__main__":
    asyncio.run(test_server())