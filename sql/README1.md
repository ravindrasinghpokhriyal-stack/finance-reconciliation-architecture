# Unified Payment Data Platform

## Overview

This project builds a **unified payment data platform** for three independent product squads (Cards, Transfers, Bill Payments) in a neobanking environment.

Each squad originally maintained its own schema, causing inconsistencies in analytics, reporting, and downstream processing.

This solution introduces:

* A **canonical payment event model**
* A **Python-based ingestion and transformation pipeline**
* A **schema validation framework**
* A **versioned data contract**
* A **migration strategy across squads**
* A **data quality monitoring dashboard**

The goal is to enable scalable, reusable, and governed payment data across the organization.

---

# 🧩 Problem Statement

The organization had three independent payment systems:

* Cards Transactions
* Bank Transfers
* Bill Payments

Each system had:

* Different schema definitions
* Different status values
* Different timestamp formats
* No shared data model

This created:

* Heavy downstream transformation logic
* Inconsistent reporting
* Poor data reliability
* Difficult cross-product analytics

---

# 🏗️ Solution Architecture

## High-Level Flow

```
Cards CSV       \
Transfers CSV -----> ETL Pipeline ---> Canonical Payment Model ---> Parquet Output
Bills CSV       /
```

## Components

### 1. Extract Layer

Reads raw CSV files from each squad.

### 2. Transform Layer

Maps each source schema into a **canonical payment schema**.

### 3. Validation Layer

Ensures schema compliance using strict rules (Pydantic-based validation).

### 4. Storage Layer

Stores clean data in **Parquet format** for analytics consumption.

---

# 📊 Canonical Data Model

## Core Fields

| Field            | Description                    |
| ---------------- | ------------------------------ |
| event_id         | Unique transaction identifier  |
| payment_type     | card / transfer / bill_payment |
| customer_id      | Customer reference             |
| amount           | Transaction amount             |
| currency         | ISO currency                   |
| event_timestamp  | UTC timestamp                  |
| payment_method   | VISA / ACH / BILLER            |
| status           | SUCCESS / FAILED / PENDING     |
| source_system    | Origin system                  |
| contract_version | Schema version                 |

---

# 🔄 Data Contract & Versioning

## Versioning Strategy

* **v1**: Base canonical schema for all payments
* **v2 (future)**: Extended schema with additional attributes like merchant_name

### Example Evolution

**v1**

```
event_id, amount, currency, status
```

**v2**

```
event_id, amount, currency, status, merchant_name
```

## Migration Strategy

* Backward compatible changes supported via default values
* New fields introduced without breaking existing pipelines
* Version tagging ensures safe evolution

---

# 🚀 How to Run the Pipeline

## 1. Clone Repository

```bash
git clone https://github.com/<your-username>/payment-unification-pipeline.git
cd payment-unification-pipeline
```

## 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Pipeline

```bash
python src/pipeline.py
```

## Output:

```
output/unified_payments.parquet
output/errors.json
```

---

# 🧪 Data Quality Monitoring (Bonus)

A Jupyter Notebook-based monitoring system was built to track:

## Metrics

* Schema Compliance Rate
* Data Freshness (latency tracking)
* Transaction Volume Trends
* Null Value Rates
* Squad-level data quality

## Notebook

```
notebooks/data_quality_dashboard.ipynb
```

## Example Outputs

* Daily transaction trend visualization
* Null rate distribution per column
* Schema compliance score
* Anomaly detection in volume drops

---

# 📈 Key Design Decisions

## 1. Canonical Schema First Approach

A single unified schema ensures downstream systems do not need per-squad logic.

## 2. Parquet as Storage Format

Chosen for:

* Fast analytics queries
* Compression efficiency
* Compatibility with modern data platforms

## 3. Validation at Ingestion

Invalid records are rejected early to prevent downstream corruption.

---

# 🔀 Architecture & Migration Strategy

A phased rollout approach was designed:

## 30 Days

* Schema finalization
* Contract definition
* Alignment across squads

## 60 Days

* Pilot migration (Bill Payments first)
* Dual-write strategy implementation
* Validation framework rollout

## 90 Days

* Full adoption across all squads
* Legacy pipeline deprecation
* Governance model activation

---

# 📊 Data Quality Dashboard

The monitoring system tracks:

### 1. Schema Compliance

Ensures all required fields exist in every record.

### 2. Data Freshness

Measures delay between event creation and ingestion.

### 3. Volume Anomalies

Detects sudden drops in transaction activity.

### 4. Null Rates

Identifies missing or incomplete data fields.

### 5. Squad-Level Quality

Compares data quality across product teams.

---

# 📌 Assumptions

* All timestamps are in UTC
* Event IDs are unique globally
* Currency follows ISO-4217 standard
* Source data is batch delivered
* No duplicate records in raw input

---

# ⚖️ Trade-offs

* Excluded real-time streaming for simplicity
* Focused on batch processing pipeline
* Simplified governance model for assignment scope
* Deferred advanced observability tools

---

# 📦 Tech Stack

* Python 3.9+
* Pandas
* PyArrow
* Pydantic
* Jupyter Notebook
* Parquet

---

# 📂 Project Structure

```
payment-unification/
│
├── data/
├── docs/
├── notebooks/
├── output/
├── src/
├── schemas/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🎯 Business Impact

* Unified payment analytics across all squads
* Reduced transformation duplication
* Improved data reliability
* Faster onboarding of new payment products
* Strong governance via versioned contracts

---

# 🚀 Future Improvements

* Airflow orchestration
* Real-time streaming ingestion (Kafka)
* Great Expectations validation suite
* Data lineage tracking
* Cloud-based data lake integration
