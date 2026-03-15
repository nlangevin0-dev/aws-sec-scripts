import boto3
import logging
logging.basicConfig(level=logging.INFO)


def main():

    try:
        iam = boto3.client('iam')

        response = iam.list_users()

        for users in response['Users']:
            mfa = iam.list_mfa_devices(UserName=users['UserName'])
            has_mfa = len(mfa['MFADevices']) > 0
            print(users['UserName'])
            print(users['CreateDate'])
            print(f"Has MFA: {has_mfa}")

            keys = iam.list_access_keys(UserName=users['UserName'])
            for key in keys['AccessKeyMetadata']:
                print(f"Access Key: {key['AccessKeyId']}")
                print(f"Status: {key['Status']}")
                print(f"Created: {key['CreateDate']}")
            
        logging.info(f"IAM audit completed successfully.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()