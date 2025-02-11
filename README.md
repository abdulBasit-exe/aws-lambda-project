## Project Overview
This project automates the processing of CSV files using AWS Lambda and S3. When a CSV file is uploaded to an S3 bucket, Lambda extracts valuable insights and saves the results back to S3. Logs are stored in AWS CloudWatch.

## Architecture
- **Amazon S3 (Source Bucket)** - Stores uploaded CSV files.
- **AWS Lambda** - Processes the file and extracts insights.
- **Amazon S3 (Output Bucket)** - Stores the generated insights.
- **Amazon CloudWatch Logs** - Captures Lambda execution logs.

## Steps to Run the Project
1. **Upload CSV File**: Upload a CSV file to the designated S3 bucket.
2. **Lambda Execution**: S3 triggers Lambda, which processes the file.
3. **Insight Generation**: Lambda extracts insights and saves a new file.
4. **Output Storage**: The processed file is stored in the S3 output bucket.

## Screenshots
### Lambda Function Setup ![Screenshot from 2025-02-12 01-33-48](https://github.com/user-attachments/assets/dbd25db9-562a-47d8-87b5-e2e20a668568)

### S3 Bucket (Before Uploading Data)![Screenshot from 2025-02-12 01-41-27](https://github.com/user-attachments/assets/13bfc441-177c-4ca5-817a-33a6f19c4dc7)

### S3 Bucket (After Processing with Generated Insights) ![Screenshot from 2025-02-12 01-44-11](https://github.com/user-attachments/assets/e939074f-bb3e-42e1-86ae-464cdaf0c402)

### CloudWatch logs (After Lambda function Trigger) ![Screenshot from 2025-02-12 01-44-27](https://github.com/user-attachments/assets/0ab39b64-4e3a-4b1f-8f40-70c8876f61a0)

## Outcome
- A CSV file containing valuable insights is saved in the S3 output bucket.
- Logs can be checked in AWS CloudWatch.

## Notes
- Ensure proper IAM permissions for Lambda to access S3.
- Verify S3 event triggers for Lambda execution.
