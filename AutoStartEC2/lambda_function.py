import json
import boto3

region = 'ap-southeast-2'

def lambda_handler(event, lambda_context):
    ec2_client = boto3.client("ec2", region_name=region)
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": 'tag:startec2',
            "Values": ['yes'],
        }
    ]).get("Reservations")
    

    #for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            ec2_client.start_instances(InstanceIds=[instance_id])
            print(f"Instances Started " + str(instance_id))
