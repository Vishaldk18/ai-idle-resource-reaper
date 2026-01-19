import boto3
import json
 
client = boto3.client("bedrock", region_name="us-east-1")
 
response = client.list_foundation_models()
 
print("Available models:")
for m in response.get("modelSummaries", []):
    print(f"- {m['modelId']}")
