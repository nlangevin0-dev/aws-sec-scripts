A collection of scripts for auditing AWS account security with boto3

## Scripts

**list_iam_users.py** - Enums all IAM users and their creation dates.
**check_access_kets.py** - Lists all access keys with status and creation date.
**audit_keys.py** - Flags access keys by age
**check_s3_public.py** - Scans S3 buckets for public access via ACLs
**check_security_groups.py** - Identifies groups with rules open for 0.0.0.0/0.

## Requirements

- Python 3.x
- boto3
- AWS CLI configed with appropriate creds


## Usage 

Configure AWS CLI creds, then run any script:

aws configure
python3 audit_keys.py
