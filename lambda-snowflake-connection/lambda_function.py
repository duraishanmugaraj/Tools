import json
import snowflake.connector
import os 

user = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
account = os.getenv('ACCOUNT')


def lambda_handler(event, context):
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse='compute_wh',
        database='US_ZIP_CODE_CROSSWALK_HUDUPS',
        schema='zipcode_crosswalk'
    )
    cursor = conn.cursor()
    cursor.execute("""
select *, row_number() over(partition by state order by total_population) as rank
from COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.DEMOGRAPHICS order by state,total_population
""")
    result = cursor.fetchall()
    conn.close()
    return {
        'statusCode': 200,
        'body': json.dumps(len(result))
    }
