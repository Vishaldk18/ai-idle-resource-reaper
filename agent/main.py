import json
 
from discovery import (
    get_stopped_ec2_instances,
    get_unattached_ebs_volumes,
    get_unused_elastic_ips,
)
from reasoner import analyze_waste
from guardrails import evaluate_guardrails
 
 
def run_agent():
    """
    Main orchestration loop for AI Idle Resource Reaper
    """
 
    idle_resources = []
 
    # OBSERVE
    idle_resources.extend(get_stopped_ec2_instances())
    idle_resources.extend(get_unattached_ebs_volumes())
    idle_resources.extend(get_unused_elastic_ips())
 
    if not idle_resources:
        print("✅ No idle resources found.")
        return
 
    print("\n🤖 AI Idle Resource Reaper Report")
    print("=" * 60)
 
    for resource in idle_resources:
        print(f"\n🔍 Analyzing {resource['type']} → {resource['resource_id']}")
 
        try:
            # THINK (AI reasoning)
            analysis = analyze_waste(resource)
 
            # DECIDE (guardrails)
            guardrail_result = evaluate_guardrails(analysis)
 
            # FINAL OUTPUT (dry-run, explainable)
            final_report = {
                "resource": resource,
                "analysis": analysis,
                "guardrail": guardrail_result,
                "mode": "dry-run"
            }
 
            print(json.dumps(final_report, indent=2))
 
        except Exception as e:
            print("❌ Error while analyzing resource")
            print(str(e))
 
        print("-" * 60)
 
 
if __name__ == "__main__":
    run_agent()
