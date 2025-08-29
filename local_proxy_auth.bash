#Install gcloud sdk and run this script
## to connect from a local machine to the Cloud Run Server.
## Use the provided url and port in the mcp.json file (or similar), as shown in the .vscode folder if using VSCODE a MCP Client
gcloud run services proxy mcp-server --region=us-central1