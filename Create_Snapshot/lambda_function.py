#Import library boto3
import boto3
#Declare region that you want use it
region = 'ap-southeast-2'
#Define a lambda_handler function and function called when lambda event is triggered
def lambda_handler(event, lambda_context):
    #Create an object ec2 and maybe using it to access to ec2 resources
    ec2 = boto3.resource("ec2", region_name=region)
    for vol in ec2.volumes.all():   #Iterate over all the ec2 volumes 
        volume = ec2.Volume(vol.id)  #Get id of volume and stored it in the volume variable.
        desc = 'This is a snapshot of {}'.format(volume)
        print("Creating Snapshot of the following Volume : ", volume)
        volume.create_snapshot(Description=desc) # Using create_snapshot method to create snapshot
