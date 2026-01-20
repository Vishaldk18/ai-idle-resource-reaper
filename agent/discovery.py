import boto3
from datetime import datetime, timezone

EBS_COST_PER_GB = 0.08
EIP_MONTHLY_COST = 3.6

def days_between(start_time):
    now = datetime.now(timezone.utc)
    return (now - start_time).days

def get_stopped_ec2_instances():
    ec2 = boto3.client("ec2",region_name="Replace_With_AWS_Region")
    response = ec2.describe_instances(
          Filters=[
              {
                "Name":"instance-state-name",
                "Values":["stopped"]
              }
              ]
        )
    instances = []
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            stopped_time = instance.get("StateTransitionReason", "")
            instances.append({
                "type": "ec2",
                "resource_id": instance["InstanceId"],
                "note": "Stopped EC2 instance (EBS still incurs cost) "
            })
    return instances 
    
def get_unattached_ebs_volumes():
    ec2 = boto3.client("ec2",region_name="Replace_With_AWS_Region")
    response = ec2.describe_volumes(
            Filters=[
                {"Name": "status", "Values":["available"]}
            ]
        )
        
    volumes = []
        
    for volume in response["Volumes"]:
        unused_days = days_between(volume["CreateTime"])
        monthly_cost = round(volume["Size"] * EBS_COST_PER_GB, 2)
        volumes.append({
                "type":"ebs",
                "resource_id": volume["VolumeId"],
                "size_gb": volume["Size"],
                "unused_days": unused_days,
                "estimated_monthly_cost_used": monthly_cost
            })
    return volumes 
        
def get_unused_elastic_ips():
    ec2 = boto3.client("ec2",region_name="Replace_With_AWS_Region")
    response = ec2.describe_addresses()
            
    eips = []
            
    for address in response["Addresses"]:
        if "InstanceId" not in address:
                    eips.append({
                        "type": "eip",
                        "resource_id": address["AllocationId"],
                        "estimated_monthly_cost_usd":EIP_MONTHLY_COST
                    })
            
    return eips
            
idle_resources = []   
        
idle_resources.extend(get_stopped_ec2_instances())
idle_resources.extend(get_unattached_ebs_volumes())
idle_resources.extend(get_unused_elastic_ips())
        
if not idle_resources:
    print("No ideal resources found.")
else:
    print("Ideal resources detected:\n")
    for r in idle_resources:
        print(r)
