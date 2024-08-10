CREATE OR REPLACE TABLE TEST.TEST.CREDIT_CARD (
    Time STRING,
    V1 STRING,
    V2 STRING,
    V3 STRING,
    V4 STRING,
    V5 STRING,
    V6 STRING,
    V7 STRING,
    V8 STRING,
    V9 STRING,
    V10 STRING,
    V11 STRING,
    V12 STRING,
    V13 STRING,
    V14 STRING,
    V15 STRING,
    V16 STRING,
    V17 STRING,
    V18 STRING,
    V19 STRING,
    V20 STRING,
    V21 STRING,
    V22 STRING,
    V23 STRING,
    V24 STRING,
    V25 STRING,
    V26 STRING,
    V27 STRING,
    V28 STRING,
    Amount STRING,
    Class STRING
);

CREATE OR REPLACE FILE FORMAT my_csv_format
    TYPE = 'CSV'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    FIELD_DELIMITER = ','
    SKIP_HEADER = 0;  -- Set this to 0 to ensure no rows are skipped (no header row)

    
-- Step 1: Create a stage in Snowflake
CREATE OR REPLACE STAGE my_s3_stage
  URL='s3://ec2-spark-aws-files/'
  CREDENTIALS=(AWS_KEY_ID='' AWS_SECRET_KEY='')
  FILE_FORMAT = my_csv_format;


-- Step 3: Copy data from S3 to Snowflake
COPY INTO TEST.TEST.CREDIT_CARD
FROM @my_s3_stage/creditcard.csv
FILE_FORMAT = my_csv_format;

-- Step 4: Verify the data load
SELECT * FROM TEST.TEST.CREDIT_CARD LIMIT 10;

