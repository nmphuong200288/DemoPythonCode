#Import boto3 library
import boto3
conn = boto3.client('rds', region_name='ap-northeast-2')
ec2 = boto3.client('ec2')
#Create a subnet
conn.create_db_subnet_group(
    DBSubnetGroupName='databasesubnet',
    DBSubnetGroupDescription='using-privatesubnet-rds',
    SubnetIds=[
        'subnet-0c9f389abf0e6614a',
        'subnet-064df2573ead56b0f',
    ],
    Tags=[
        {
            'Key': 'DatabaseRds',
            'Value': 'mysql8.0'
            
        },
    ]
)

#Create a security Group
response = ec2.create_security_group(
    GroupName='MyDBSecurityGroup', 
    Description='Description for MyDBSecurityGroup', 
    VpcId='vpc-0bafbe97c1d5315fa',
    )
security_group_id = response['GroupId']

ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 3306,
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'RDS Access from anywhere',
                },
            ],
            'ToPort': 3306,
        },
    ],
)

#Invoke create_db_instance method
database = conn.create_db_instance(

        AllocatedStorage=10,
        DBName="MYRDS",
        DBInstanceIdentifier="my-first-rds-instance",
        DBInstanceClass="db.t2.micro",
        Engine="mysql",
        MasterUsername="root",
        MasterUserPassword="pass1234",
        Port=3306,
        BackupRetentionPeriod=0,
        PubliclyAccessible=True,
        DBSubnetGroupName='databasesubnet',
        VpcSecurityGroupIds=[response['GroupId']],
        
        Tags=[
            {
                'Key': 'mydatabase',
                'Value': 'Mysql'
            },
        ],
        
    )
#print info of database 
print (database)
