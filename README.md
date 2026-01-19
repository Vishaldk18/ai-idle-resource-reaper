# 🤖 AI Idle Resource Reaper
Agentic FinOps System using AWS & Amazon Bedrock
 
---
 
## 📌 Overview
 
AI Idle Resource Reaper is an Agentic AI-powered FinOps tool that detects unused AWS resources, estimates their cost impact, and generates explainable cleanup recommendations using Amazon Bedrock.
 
The system is designed with safety in mind and operates in dry-run mode, ensuring no destructive actions are performed automatically.
 
---
 
## 🎯 Problem Statement
 
In AWS environments, unused resources such as:
 
- Unattached EBS volumes
- Unused Elastic IPs
- Stopped EC2 instances
 
often remain unnoticed and continue to incur unnecessary cloud costs.
 
While basic scripts can identify these resources, they usually lack:
- Cost awareness
- Contextual reasoning
- Safety controls
 
---
 
## 💡 Solution
 
This project implements an agentic workflow that:
 
1. Discovers idle AWS resources
2. Enriches them with cost estimates
3. Uses AI to analyze why the resource is wasteful
4. Applies guardrails before recommending actions
 
---
 
## 🧠 Agentic Workflow
 
OBSERVE → THINK → DECIDE → RECOMMEND
 
| Step | Description |
|------|------------|
| Observe | Discover unused AWS resources |
| Think | Analyze waste using Amazon Bedrock |
| Decide | Apply safety guardrails |
| Recommend | Output dry-run recommendations |
 
---
 
## 🛠 Tech Stack
 
### AWS Services
- EC2
- EBS
- Elastic IP
- IAM
- Amazon Bedrock
 
### AI
- Amazon Bedrock text generation model
 
### Backend
- Python 3
- boto3
 
---
 
## 🗂 Project Structure
 
ai-idle-resource-reaper/
├── agent/
│   ├── discovery.py     # Discover idle AWS resources
│   ├── reasoner.py      # AI-based waste analysis
│   ├── guardrails.py    # Safety checks and validation
│   └── main.py          # Agent orchestration
├── prompts/
│   └── waste_analysis.txt
├── requirements.txt
└── README.md
 
---
 
## 🔍 Resources Detected
 
The agent currently detects:
 
- Stopped EC2 instances
- Unattached EBS volumes
- Unused Elastic IPs
 
Each resource is enriched with:
- Unused duration
- Estimated monthly cost
- Resource metadata
 
---
 
## 💰 Cost Estimation Logic
 
| Resource | Estimated Cost |
|---------|----------------|
| Unattached EBS | $0.08 per GB per month |
| Elastic IP | ~$3.60 per month |
| Stopped EC2 | $0 (EBS still incurs cost) |
 
These values are estimates used for decision-making.
 
---
 
## 🧠 AI Reasoning
 
For each idle resource, the AI generates:
 
- Reason for waste
- Severity level (Low / Medium / High)
- Estimated monthly waste
- Recommended cleanup action
- Confidence score
 
### Example AI Output
 
{
  "waste_reason": "Unattached EBS volumes incur storage costs without providing value",
  "severity": "Medium",
  "estimated_monthly_waste_usd": 0.4,
  "recommended_action": "Delete after confirming no backups are required",
  "confidence": 0.86
}
 
---
 
## 🛑 Guardrails
 
The system applies safety checks before accepting AI recommendations:
 
- Confidence must be greater than or equal to 0.7
- High severity cases require human approval
- No destructive actions are executed automatically
 
All recommendations operate in dry-run mode.
 
---
 
## ▶️ How to Run
 
1. Install dependencies
 
pip install -r requirements.txt
 
2. Configure AWS credentials
 
aws configure
 
3. Run the agent
 
python agent/main.py
 
---
 
## 📤 Sample Output
 
{
  "resource": {
    "type": "ebs",
    "resource_id": "vol-09b01eafd02abc140",
    "unused_days": 12,
    "estimated_monthly_cost_usd": 0.4
  },
  "analysis": {
    "waste_reason": "Unattached EBS volume is unused",
    "severity": "Medium",
    "recommended_action": "Delete after confirmation",
    "confidence": 0.86
  },
  "guardrail": {
    "allowed": true,
    "reason": "Safe to recommend (dry-run only)"
  },
  "mode": "dry-run"
}
 
---
 
## 🧹 Cleanup
 
After testing, clean up AWS resources to avoid charges:
 
- Delete unattached EBS volumes
- Release unused Elastic IPs
- Terminate test EC2 instances
- Remove temporary IAM permissions
 
---
 
## 🚀 Future Improvements
 
- Slack or SNS notifications
- Auto-tagging idle resources
- Multi-region scanning
- Budget-aware recommendations
- Approval-based cleanup actions
