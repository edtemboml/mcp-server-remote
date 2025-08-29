#Install gcloud sdk and run this script
## to connect from a local machine to the Cloud Run Server.
## Use the provided url and port in the mcp.json file (or similar), as shown in the .vscode folder if using VSCODE as your MCP Client
export SERVER_NAME=<SERVER_NAME> #same as in gcloud_infra.bash
export REGION=<region> #same as in gcloud_infra.bash
gcloud run services proxy $SERVER_NAME --region=$REGION
