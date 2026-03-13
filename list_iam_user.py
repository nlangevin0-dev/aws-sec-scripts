import boto3

client = boto3.client('iam')

response = client.list_users()

for user in response['Users']:
    print(user['UserName'], user['CreateDate'])

    