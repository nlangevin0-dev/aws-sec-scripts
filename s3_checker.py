import boto3
import logging
logging.basicConfig(level=logging.INFO) 


def main():
    s3 = boto3.client('s3')

    try:
        ## Gets a list of all S3 buckets in the account and prints their names and creation dates
        response = s3.list_buckets()
        logging.info("Fetched S3 bucket list successfully.")
        public_count = 0
        for bucket in response['Buckets']:
            print(f"Bucket Name: {bucket['Name']}")
            print(f"Creation Date: {bucket['CreationDate']}")
            acl_response = s3.get_bucket_acl(Bucket=bucket['Name'])
            for grant in acl_response['Grants']:
                grantee = grant['Grantee']
                permission = grant['Permission']
                if grantee.get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                    print("This bucket is publicly accessible.")
                    public_count += 1
                elif grantee.get('URI') == 'http://acs.amazonaws.com/groups/global/AuthenticatedUsers':
                    print("This bucket is accessible to all authenticated AWS users.")
                    public_count += 1
        print(f"Total buckets: {len(response['Buckets'])}")
        print(f"Public buckets: {public_count}")

    except Exception as e:
        logging.error(f"An error occurred while fetching S3 buckets: {e}")

if __name__ == "__main__":
    main()