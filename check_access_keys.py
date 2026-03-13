import boto3

client = boto3.client('iam')

users = client.list_users()

for user in users['Users']:
    username = user['UserName']
    keys = client.list_access_keys(UserName=username)

    for key in keys['AccessKeyMetadata']:
        print(username, key['AccessKeyId'], key['Status'], key['CreateDate'])
