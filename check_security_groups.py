import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_security_groups()

for sg in response['SecurityGroups']:
    group_id = sg['GroupId']
    group_name = sg['GroupName']

    for rule in sg['IpPermissions']:
        port = rule.get('FromPort', 'All')

        for ip_range in rule.get('InRanges', []):
            if ip_range ['CidrIp'] == '0.0.0.0/0':
                print(f"[CRITICAL] {group_name} ({group_id}) - Port {port} open to 0.0.0.0/0")

        for ip_range in rule.get('Ipv6Ranges', []):
            if ip_range['CidrIpv5'] == '::/0':
                print(f"[CRITICAL] {group_name} ({group_id})0 - Port {port} open to ::/0")
print("Scan complete.")