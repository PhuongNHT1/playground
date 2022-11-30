import boto3

# client = boto3.client('s3')

# Get bucket with name from S3
s3 = boto3.resource('s3')
bucket = s3.Bucket('d928904-phuong')

def listObjects():
    print('object 1')
    print('object 2')

listObjects()

