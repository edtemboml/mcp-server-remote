export PROJECT_ID=<project-id>
export REGION=<region>
export SERVER_NAME=remote-mcp-server-1 #rename accordingly

#login to gcloud account and configure project
gcloud auth login
gcloud config set project $PROJECT_ID

#this will require appropriate permissions to create and upload to artifacts repos
gcloud artifacts repositories create remote-mcp-servers \
  --repository-format=docker \
  --location=$REGION \
  --description="Repository for remote MCP servers" \
  --project=$PROJECT_ID

#build and push 
gcloud builds submit --region=$REGION \
--tag $REGION-docker.pkg.dev/$PROJECT_ID/remote-mcp-servers/$SERVER_NAME:latest

#deploy to cloud run 
gcloud run deploy $SERVER_NAME \
  --image $REGION-docker.pkg.dev/$PROJECT_ID/remote-mcp-servers/$SERVER_NAME:latest \
  --region=$REGION \
  --no-allow-unauthenticated














