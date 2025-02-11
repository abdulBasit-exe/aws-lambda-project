import json
import boto3
import pandas as pd
import io

# Initialize S3 client
s3_client = boto3.client("s3")

# Define the output S3 bucket and fixed filename
OUTPUT_BUCKET = "s3bucketforlambdaproject"
OUTPUT_FILENAME = "valuable_insight.csv"  # Fixed filename to keep only one file

def lambda_handler(event, context):
    try:
        # Extract bucket and file details from the event
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        source_key = event['Records'][0]['s3']['object']['key']
        
        # Fetch the CSV file from S3
        response = s3_client.get_object(Bucket=source_bucket, Key=source_key)
        csv_data = response['Body'].read().decode('ISO-8859-1')  # Handle encoding issues
        
        # Load CSV into pandas DataFrame
        df = pd.read_csv(io.StringIO(csv_data))
        
        # Valuable Insight: Best-Selling Product Category
        best_category = df.groupby("Category")["Sales"].sum().idxmax()
        total_sales = df.groupby("Category")["Sales"].sum().max()

        # Create DataFrame for the insight
        insight_df = pd.DataFrame({
            "Best_Selling_Category": [best_category],
            "Total_Sales": [total_sales]
        })
        
        # Save insights to a CSV file
        output_csv = io.StringIO()
        insight_df.to_csv(output_csv, index=False)
        
        # Upload new CSV to S3 (overwriting previous file)
        s3_client.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=OUTPUT_FILENAME,
            Body=output_csv.getvalue(),
            ContentType="text/csv"
        )
        
        print(f"Insights saved to {OUTPUT_FILENAME} in {OUTPUT_BUCKET}")
        
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Insight extracted successfully!", "file": OUTPUT_FILENAME})
        }
    
    except Exception as e:
        print(f"Error processing file: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
