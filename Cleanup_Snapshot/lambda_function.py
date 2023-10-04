import boto3
import dateutil.tz
from datetime import datetime, timedelta, timezone

region = 'ap-southeast-2'

def lambda_handler(event, lambda_context):
    ec2 = boto3.resource("ec2", region_name=region)
    current_date = datetime.now(tz=timezone.utc)
    ho_chi_minh_tz=dateutil.tz.gettz('Asia/Ho_Chi_Minh')
    currentdata_gmt7=current_date.astimezone(ho_chi_minh_tz)
    #diff_date = current_date - timedelta(hours=2)  # timedelta function can be use to date manipulations
    snapshots = ec2.snapshots.filter(OwnerIds=['self'])
    currendata_gmt7_str=currentdata_gmt7.strftime('%Y-%m-%d %H:%M:%S')
    diff_date = currentdata_gmt7 - timedelta(minutes = 43)
    print(diff_date)
    for snapshot in snapshots:
        snapshot_start_time = snapshot.start_time
         
        if diff_date > snapshot_start_time:
            
            try:
                snapshot.delete()
                print("Deleting Snapshot id: ", snapshot.snapshot_id)
            
            except Exception as e:
                print("Current Snapshot is in use: ", snapshot.snapshot_id)
