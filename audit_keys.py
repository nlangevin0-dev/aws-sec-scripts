import boto3
from datetime import datetime, timezone

client = boto3.client('iam')

users = client.list_users()

for user in users['Users']:
    username = user['UserName']
    keys = client.list_access_keys(UserName=username)

    for key in keys['AccessKeyMetadata']:
        created = key['CreateDate']
        age = (datetime.now(timezone.utc) - created).days
        status = key['Status']
        key_id = key['AccessKeyId']

        if age > 90:
            print(f"[CRITICAL] {username} - {key_id} is {age} days old.")
        elif age > 45:
            print(f"[WARNING] {username} - {key_id} is {age} days old.")
        else:
            print(f"[OK] {username} - {key_id} is {age} days old.")

    
        if status == 'Active':
            last_used = client.get_access_key_last_used(AccessKeyId=key_id)
            last = last_used['AccessKeyLastUsed'].get('LastUsedDate', 'Never')
            print(f"    Last Used: {last}")