# 🎓 Graduation Rates Big Data Pipeline

This project demonstrates a complete big data pipeline to ingest, clean, transform, and store U.S. education expenditure and enrollment data using Apache NiFi, HDFS, Hive, Spark, and HBase.

---

## 📊 Project Overview

**Objective**:  
Build a distributed data pipeline that ingests raw education data from a GitHub-hosted CSV file, processes it using Hive and Spark, and stores the cleaned output in HBase for low-latency retrieval.

**Pipeline Components**:
- **Apache NiFi** – Data ingestion from GitHub
- **HDFS** – Distributed data storage
- **Apache Hive** – Data cleaning and transformation via SQL
- **Apache Spark** – Advanced processing and export formatting
- **Apache HBase** – NoSQL storage and key-based lookup

---

## 📁 Dataset

**Source**:  
[states_all.csv](https://raw.githubusercontent.com/CherylMachingura/hdfs/main/states_all.csv)

**Fields Used**:
- `STATE`
- `YEAR`
- `TOTAL_EXPENDITURE`
- `ENROLLMENT`
- `EXPENDITURE_PER_STUDENT`

---

## ⚙️ Technologies Used

- Hadoop HDFS
- Apache NiFi
- Apache Hive
- Apache Spark (PySpark)
- Apache HBase

---

## 🛠️ Step-by-Step Pipeline Instructions

### 1️⃣ NiFi Flow: GitHub → HDFS

**Processors**:
- `InvokeHTTP`  
  - URL: `https://raw.githubusercontent.com/CherylMachingura/hdfs/main/states_all.csv`
- `PutHDFS`  
  - Directory: `/data/education/raw/`
  - Hadoop Config: `core-site.xml`, `hdfs-site.xml`

---

### 2️⃣ Hive: Cleaning and Structuring Data

```sql
-- Create external table
CREATE EXTERNAL TABLE IF NOT EXISTS education_raw (
  STATE STRING,
  YEAR STRING,
  TOTAL_EXPENDITURE STRING,
  ENROLLMENT STRING,
  EXPENDITURE_PER_STUDENT STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",",
  "quoteChar" = "\""
)
STORED AS TEXTFILE
LOCATION '/data/education/raw/';

-- Create cleaned table
CREATE TABLE IF NOT EXISTS education_cleaned (
  year INT,
  state STRING,
  total_expenditure DOUBLE,
  enrollment INT,
  expenditure_per_student DOUBLE
)
STORED AS PARQUET;

-- Insert cleaned data
INSERT INTO education_cleaned
SELECT
  CAST(REGEXP_REPLACE(YEAR, '[^0-9]', '') AS INT),
  UPPER(STATE),
  CAST(REGEXP_REPLACE(TOTAL_EXPENDITURE, '[^0-9.]', '') AS DOUBLE),
  CAST(REGEXP_REPLACE(ENROLLMENT, '[^0-9]', '') AS INT),
  CAST(REGEXP_REPLACE(EXPENDITURE_PER_STUDENT, '[^0-9.]', '') AS DOUBLE)
FROM education_raw
WHERE YEAR IS NOT NULL
  AND STATE IS NOT NULL
  AND TOTAL_EXPENDITURE RLIKE '^[0-9.]+$'
  AND ENROLLMENT RLIKE '^[0-9]+$'
  AND EXPENDITURE_PER_STUDENT RLIKE '^[0-9.]+$';
