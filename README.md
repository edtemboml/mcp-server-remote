# MCP Server with Streamable HTTP

A Model Context Protocol (MCP) server implementation using streamable HTTP transport.

## Features

- Streamable HTTP transport
- Sample tools: add numbers and send greetings
- Inventory/overstock items endpoint
- Easy to extend with new tools, resources and prompts if supported by your client.

## Prerequisites

- Python 3.13+
- uv package manager (recommended) or pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/edtemboml/mcp-server-remote.git
cd mcp-server-remote
```

2. Create and activate a virtual environment:
```bash
# Using uv (recommended)
uv venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate # Linux/Mac

# OR using standard venv
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate # Linux/Mac
```

3. Install dependencies:
```bash
uv add fastmcp
uv add mcp[cli]
uv add asyncio
```

## Deploy to Google Cloud Run (Alternative)

You can deploy the server to Google Cloud Run for a managed, scalable deployment:

1. Install the Google Cloud SDK and authenticate or use Cloud Shell:
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

2. Configure deployment settings in `gcloud_infra.bash`:
```bash
# Edit these variables in gcloud_infra.bash
export PROJECT_ID="your-project-id"
export REGION="your-region"      # e.g., us-central1
export SERVICE_NAME="mcp-server"
```

3. Deploy to Cloud Run:
```bash
# Make the script executable
chmod +x gcloud_infra.bash
# Deploy
./gcloud_infra.bash
```

The deployment script will:
- Build and push the Docker image
- Deploy to Cloud Run with appropriate settings
- Output the service URL

## Alternatively - Deploy Server Locally

1. Start the server:
```bash
uv run streamable_server.py
# OR
python streamable_server.py
```

## Available Tools and Resources (Note: some clients do not support resources)

- `inventory://items/overstock` - Get list of overstock items
- Tool: `add(a: int, b: int)` - Add two numbers
- Tool: `say_hello(name: str)` - Send a greeting to someone

## Development

To add new tools or resources:

1. Open `streamable_server.py`
2. Add new tools using the `@mcp.tool()` decorator
3. Add new resources using the `@mcp.resource()` decorator

See https://modelcontextprotocol.io/docs/getting-started/intro

Example:
```python
@mcp.tool()
def your_new_tool(param: type) -> return_type:
    """Tool description."""
    return result
```

## License

MIT License