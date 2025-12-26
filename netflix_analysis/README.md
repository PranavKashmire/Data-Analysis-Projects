# Netflix Global Top 10 Performance Analysis

A data-driven analysis of Netflix's Global Top 10 viewership data, focusing on non-English film performance and data integrity assessments.

## 🚀 Project Overview
This project analyzes a dataset of Netflix's weekly Top 10 rankings to identify top-performing content and evaluate the impact of data anomalies on business metrics.

### Key Objectives:
- **Performance Tracking:** Identify the longest-running non-English films in the Top 10.
- **Viewership Modeling:** Estimate total views by normalizing viewing hours against content runtime.
- **Data Integrity:** Assess the impact of reporting outages on cumulative performance metrics.

## 🛠️ Tech Stack
- **Language:** Python 3.11
- **Libraries:** Pandas (Data Manipulation), NumPy (Numerical Analysis)
- **Data Source:** Netflix Global Top 10 (April - June 2022)
- **Environment:** Jupyter Notebook / Sandbox VM

## 📊 Key Findings
- **Top Performer:** *"Through My Window"* led the 'Films (Non-English)' category with **13 cumulative weeks** in the Top 10.
- **Estimated Reach:** Approximately **5.37 million views** calculated for the top performer based on 10.38M viewing hours.
- **Anomaly Detection:** Identified a critical reporting outage during the week of **May 22nd, 2022**, where all viewing hours were recorded as zero, necessitating data imputation for accurate performance modeling.

## 📂 Repository Structure
- `analysis_report.md`: Comprehensive technical report of findings.
- `netflix_analysis.py`: Python scripts used for data processing and estimation.
- `data/`: (Optional) Directory for raw data files.

---
*Developed as part of a Data Support Specialist technical exercise.*
