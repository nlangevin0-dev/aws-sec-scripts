import boto3

s3 = boto3.client('s3')

buckets = s3.list_buckets()

for bucket in buckets['Buckets']:
    name = bucket['Name']

    try:
        acl = s3.get_bucket_acl(Bucket=name)
        for grant in acl['Grants']:
            grantee = grant['Grantee']
            if grantee.get('URI') and 'AllUsers' in grantee['URI']:
                print(f"[CRITICAL] {name} - PUBLIC access via ACL")
            elif grantee.get('URI') and 'AuthenitcatedUsers' in grantee['URI']:
                print(f"[WARNING] {name} - Accessible to any AWS authenticated user")
    except Exception as e:
        print(f"[ERROR] {name} - {e}")


    try:
        policy_satus = s3.get_bucket_policy_status(Bucket=name)
        if policy_statis['PolicyStatus']['IsPublic']:
            print(f"[CRITICAL] {name} - PUBLIC access via bucket policy")
    except s3.exceptions.from_code('NoSuchBucketPolicy'):
        pass
    except Exception as e:
        pass
print("Scan complete.")     
