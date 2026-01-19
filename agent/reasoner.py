import boto3
import json
 
 
def analyze_waste(resource):
    bedrock = boto3.client(
        "bedrock-runtime",
        region_name="us-east-1"
    )
 
    prompt = f"""
You are a FinOps assistant.
 
Analyze the following unused AWS resource and respond ONLY in valid JSON.
 
Include:
- waste_reason
- severity (Low / Medium / High)
- estimated_monthly_waste_usd
- recommended_action
- confidence (0 to 1)
 
Resource details:
{json.dumps(resource, indent=2)}
"""
 
    body = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {"text": prompt}
                ]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 300,
            "temperature": 0.3
        }
    }
 
    response = bedrock.invoke_model(
        modelId="amazon.nova-micro-v1:0",
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json"
    )
 
    response_body = json.loads(response["body"].read())
 
    # Nova models return output here
    text = response_body["output"]["message"]["content"][0]["text"]
 
    return json.loads(text)
 
