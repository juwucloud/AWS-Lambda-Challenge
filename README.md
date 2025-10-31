# AWS Lambda Challenge

## Topic
1. Create a Lambda function to count the number of words in a text file.

2. Configure an Amazon Simple Storage Service (Amazon S3) bucket to invoke a Lambda function when a text file is uploaded to the S3 bucket.

3. Create an Amazon Simple Notification Service (Amazon SNS) topic to report the word count in an email.

### Steps
1. Opened AWS and created an S3 Bucket.
2. Created a Lambda Function with Full S3 Access Role.
3. Wrote the PythonCode to count words in a file.
4. Go to S3 -> Properties -> Event notification for every .txt-file
6. Created a SNS Topic and subscribed to it 
7. Added the SNS Topic to the Environmental Variable
8. Used AI to adapt my PythonCode for getting the File and Counting words 
9. Tested the Lambda Function by uploading a .txt-file to 
10. Had to troubleshoot because of timeout -> set timeout to 15s
11. Uploaded again
10. Got an E-Mail ☑️
