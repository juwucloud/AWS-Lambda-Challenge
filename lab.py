import boto3
import json
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns = boto3.client('sns')

    # Get SNS topic ARN from environment variable
    topic_arn = os.environ['SNS_TOPIC_ARN']

    # Extract bucket and file name from the event
    record = event['Records'][0]
    bucket_name = record['s3']['bucket']['name']
    file_key = record['s3']['object']['key']

    # Download the file from S3 to the /tmp directory
    local_path = f"/tmp/{os.path.basename(file_key)}"
    s3.download_file(bucket_name, file_key, local_path)

    # Counting the words
    def wordcount(textfile):
        c = 0
        with open(textfile, 'r') as file:
            data = file.read()
            w = data.split()
            c += len(w)
        return c

    # Run wordcount on the local file
    count = wordcount(local_path)

    # Prepare and send the SNS message
    message = f"The file '{file_key}' in bucket '{bucket_name}' contains {count} words."
    sns.publish(
        TopicArn=topic_arn,
        Subject="Wordcount Report",
        Message=message
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': message})
    }
