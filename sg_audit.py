import boto3
import logging 
logging.basicConfig(level=logging.INFO)

def main():
    ec2 = boto3.client('ec2')

    try:
        response = ec2.describe_security_groups()
        logging.info("Fetched security group list successfully.")
        for sg in response['SecurityGroups']:
            print(f"Security Group Name: {sg['GroupName']}")
            print(f"Security Group ID: {sg['GroupId']}")
            print(f"IP Permissions: {sg['IpPermissions']}")
            for rule in sg['IpPermissions']:
                port = rule.get('FromPort', 'All')
                protocol = rule.get('IpProtocol', 'All')
                for ip_range in rule.get('IpRanges', []):
                    cidr = ip_range['CidrIp']
                    print(f"  Port: {port} | Protocol: {protocol} | Source: {cidr}")
                    if cidr == '0.0.0.0/0':
                        print("  ⚠ ALERT: Open to the internet!")
    except Exception as e:
        logging.error(f"An error occurred while fetching security groups: {e}")        
            
if __name__ == "__main__":
    main()