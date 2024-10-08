select * from COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.CDC_POLICY_MEASURES;
COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.DEMOGRAPHICS

CREATE OR REPLACE DATABASE test;
USE DATABASE test;
CREATE OR REPLACE SCHEMA test;
USE SCHEMA test;

describe table COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.DEMOGRAPHICS;

-- Create or replace the table named 'demographics_test'
CREATE OR REPLACE TABLE demographics_test (
    ISO3166_1 VARCHAR(16777216),
    ISO3166_2 VARCHAR(16777216),
    FIPS VARCHAR(16777216),
    LATITUDE FLOAT,
    LONGITUDE FLOAT,
    STATE VARCHAR(16777216),
    COUNTY VARCHAR(16777216),
    TOTAL_POPULATION NUMBER(38,0),
    TOTAL_MALE_POPULATION NUMBER(38,0),
    TOTAL_FEMALE_POPULATION NUMBER(38,0)
);

SELECT * FROM TEST.TEST.DEMOGRAPHICS_TEST;