# aws s3 cp data/creditcard/creditcard_part_1.csv  s3://ec2-spark-aws-files

import json
import snowflake.connector
import os 
import urllib.parse

user = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
account = os.getenv('ACCOUNT')
aws_key_id = os.getenv('AWS_KEY_ID')
aws_secret_key = os.getenv('SECRET_KEY')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse='compute_wh',
        database='TEST',
        schema='TEST'
    )
    cursor = conn.cursor()
    
    cursor.execute("""
CREATE OR REPLACE FILE FORMAT my_csv_format
    TYPE = 'CSV'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    FIELD_DELIMITER = ','
    SKIP_HEADER = 1; 
""")
    result = cursor.fetchall()
    print(result)

    cursor.execute(f"""
CREATE OR REPLACE STAGE my_s3_stage
  URL='s3://{bucket}/'
  CREDENTIALS=(AWS_KEY_ID='{aws_key_id}' AWS_SECRET_KEY='{aws_secret_key}')
  FILE_FORMAT = my_csv_format;
""")
    result = cursor.fetchall()
    print(result)

    cursor.execute(f"""
COPY INTO TEST.TEST.CREDIT_CARD
FROM @my_s3_stage/{key}
FILE_FORMAT = my_csv_format;
""")
    result = cursor.fetchall()
    print(result)
    
    cursor.execute("""
select count(*) from TEST.TEST.CREDIT_CARD
""")
    result = cursor.fetchall()

    conn.close()
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
