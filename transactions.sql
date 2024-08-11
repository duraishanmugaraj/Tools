CREATE OR REPLACE TABLE transactions (
    Timestamp STRING,
    From_Bank STRING,
    Account_org STRING,
    To_Bank STRING,
    Account_bnf STRING,
    Amount_Received STRING,
    Receiving_Currency STRING,
    Amount_Paid STRING,
    Payment_Currency STRING,
    Payment_Format STRING,
    Is_Laundering STRING,
    load_dt STRING,
    tran_dt STRING,
    load_id STRING
)
PARTITION BY (tran_dt, load_id);

CREATE OR REPLACE TABLE transactions_audit_log (
    load_dt STRING,
    tran_dt STRING,
    load_id STRING,
    processed_records STRING,
    status STRING 
);
