<<<<<<< HEAD
# 🏥 Silent Scalper - Hospital Data Pipeline

This AWS cloud project helps hospitals securely upload and process files like reports or records. Files uploaded to an S3 bucket automatically trigger a Lambda function, which stores the data in DynamoDB. It also includes CloudWatch monitoring and SNS for alerting.

## 🔧 AWS Services Used
- S3 (file upload)
- Lambda (processing)
- DynamoDB (storage)
- CloudWatch (logs)
- SNS (notifications)

## 🏥 Real-World Use Case

1. Hospital uploads patient file to a secure S3 bucket.
2. Lambda processes file and stores it in DynamoDB.
3. If something fails,or any critical issue occur an alert is sent via SNS.
4. System is monitored by using  CloudWatch.
5. Optional: Use API Gateway to let apps access this system securely.


=======
# silent-scalper
>>>>>>> 48991a79e3e5df83cb7cca320aa74a67ef36bd27
