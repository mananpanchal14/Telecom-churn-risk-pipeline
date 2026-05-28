# Telecom-churn-risk-pipeline

## Project Overview
This project builds an end-to-end telecom churn analysis and risk segmentation pipeline using MySQL, Python, Pandas and Matplotlib. The workflow integrates database connectivity, feature engineering, churn analysis, customer risk scoring, validation and automated visual reporting into a single executable Python pipeline.

## Business Problem
- Telecom companies face significant revenue loss due to customer churn. Identifying high-risk customers early allows businesses to take proactive retention actions such as targeted offers, service improvements and support interventions.
- The objective of this project is to analyze customer churn behavior and develop a business-driven risk segmentation framework to identify customers with high probability of churn.

 ## Objectives
- Load telecom churn data into MySQL database
- Connect Python with MySQL using SQLAlchemy
- Extract relevant customer data using SQL queries
- Perform feature engineering using Pandas
- Identify major churn-driving factors
- Build an evidence-based churn risk scoring framework
- Validate risk segmentation against actual churn behavior
- Generate automated visual reports using Matplotlib
- Build an automated end-to-end analytical pipeline using Python

## Tech Stack
- Python
- Pandas
- Matplotlib
- MySQL
- SQLAlchemy
- PyMySQL
- PyCharm

## Workflow Architecture
MySQL Database -> SQL Query Extraction -> Python SQLAlchemy Connection -> Pandas Data Processing -> Feature Engineering -> Risk Score Creation -> Risk Segmentation -> Validation -> Matplotlib Visualizations -> Automated Python Pipeline

## Key Steps Performed
### 1. Database Integration
- Loaded telecom churn dataset into MySQL database
- Created database tables and established SQL connectivity using SQLAlchemy and PyMySQL

### 2. SQL Data Extraction
- Queried only required customer variables from MySQL using SQL queries
- Imported queried data directly into Pandas DataFrames using pd.read_sql()

### 3. Feature Engineering
Created business-oriented analytical features such as:
- `tenure_group`
- `charge_group`
- `risk_score`
- `risk_category`
  
### 4. Churn Driver Analysis
Analyzed the impact of:
- Contract type
- Monthly charges
- Internet service type
- Payment method
- Tech support availability
- Online backup availability
- Customer tenure
  
### 5. Risk Scoring Framework
  Built an evidence-based churn risk scoring framework by assigning weighted scores to major churn-driving factors based on observed churn rate differences.

### 6. Validation
Validated the effectiveness of the risk framework by comparing:
- Churn rates across risk categories
- Average risk scores of churned vs non-churned customers

### 7. Automated Visualization
Generated automated charts using Matplotlib to visualize:
- Churn rate by risk category
- Churn rate by tenure group
- Churn rate by monthly charge group

## Key Insights
- Customers on month-to-month contracts exhibited significantly higher churn rates compared to long-term contract customers.
- Customers with shorter tenure periods (0–12 months) showed the highest churn probability, indicating that early customer retention is critical.
- Customers with high and very high monthly charges demonstrated materially higher churn rates compared to low-charge customers.
- Fiber optic internet users showed higher churn behavior relative to other internet service categories.
- Lack of tech support and online backup services was associated with increased churn probability.
- Electronic check users exhibited higher churn rates compared to customers using other payment methods.
- The final risk segmentation framework successfully differentiated customer groups by churn probability:
  - Low Risk → ~4% churn
  - Medium Risk → ~21% churn
  - High Risk → ~57% churn
 
## Risk Segmentation Framework

Customers were segmented into three business-oriented churn risk categories:

| Risk Category | Churn Rate |
|---------------|------------|
| Low Risk | ~4% |
| Medium Risk | ~21% |
| High Risk | ~57% |

The framework demonstrated that customers classified as High Risk exhibited materially higher churn probability compared to Low Risk customers.
 
## Visualizations
The pipeline automatically generates the following visual reports using Matplotlib:
1. Churn Rate Across Risk Categories
2. Churn Rate by Customer Tenure
3. Churn Rate by Monthly Charge Group

Generated charts are automatically saved as PNG files during pipeline execution.

## Project Structure
- telecom_churn_pipeline.py → Main automated churn analysis pipeline
- README.md → Project documentation and workflow explanation
- risk_category_churn.png → Churn rate visualization across risk categories
- tenure_churn.png → Churn rate visualization by customer tenure
- charge_group_churn.png → Churn rate visualization by monthly charge groups

## How to Run the Project
1. Install Required Libraries
pip install pandas matplotlib sqlalchemy pymysql

2. Configure MySQL Connection
Update your MySQL credentials inside:

create_engine(
    "mysql+pymysql://username:password@localhost/database_name"
)

3. Run the Pipeline
python telecom_churn_pipeline.py
The pipeline will automatically:
- Connect to MySQL database
- Extract telecom churn data
- Perform feature engineering
- Build customer risk scores
- Validate risk segmentation
- Generate churn visualizations
- Save charts as PNG files
