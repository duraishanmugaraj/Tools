import json
import urllib.parse
import boto3
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
from datetime import datetime
import os 

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print(bucket)
    print(key)
    
    try:
        # Download the PDF file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        file_content = response['Body'].read()
        
        # Decrypt the PDF
        reader = PdfReader(BytesIO(file_content))
        reader.decrypt('PDF PASSWORD')  # Replace 'your_password' with the actual password
        
        # Extract text from the first page of the PDF
        page = reader.pages[0]
        text = page.extract_text()
        
        # Find the "Pay Period Jun,2024" text and extract "Jun,2024"
        pay_period = None
        lines = text.split('\n')
        for idx,line in enumerate(lines):
            if "Pay Period" in line:
                pay_period = lines[idx+1]
                break
        
        if not pay_period:
            raise ValueError("Pay Period not found in the PDF")
        
        # Create a new PDF writer
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        
        # Save the decrypted PDF to a BytesIO object
        decrypted_pdf = BytesIO()
        writer.write(decrypted_pdf)
        decrypted_pdf.seek(0)
        
        # Generate a new filename with the extracted pay period
        new_key = f"payslip/{pay_period.replace(',', '_')}_payslip.pdf"
        
        # Upload the decrypted PDF back to S3
        s3.put_object(Bucket=bucket, Key=new_key, Body=decrypted_pdf)
        
        print(f"Decrypted PDF saved to {new_key}")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'PDF decrypted and uploaded successfully {bucket} {key}')
        }
    except Exception as e:
        print(e)
        print(f'Error processing object {key} from bucket {bucket}. Make sure they exist and your bucket is in the same region as this function.')
        raise e
