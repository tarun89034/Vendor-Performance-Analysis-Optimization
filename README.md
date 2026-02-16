# Vendor Performance Analysis & Optimization

![Business Insights Infographic](file:///C:/Users/HP/.gemini/antigravity/brain/ba355bf5-91b5-4c2d-b4e8-89375659d7ed/business_insights_infographic_1766144593382.png)

## Overview
This project provides a comprehensive analysis of vendor performance, inventory health, and profitability across a massive scale of **12,261 unique brands** and **131 vendors**. Leveraging a robust data pipeline and statistical validation, we identify key market opportunities, cost-saving strategies through bulk purchasing, and actionable recommendations for supply chain optimization.

---

## System Architecture

Our data pipeline follows a structured ETL process to ensure data integrity and analytical depth:

![Project Architecture Diagram](file:///C:/Users/HP/.gemini/antigravity/brain/ba355bf5-91b5-4c2d-b4e8-89375659d7ed/project_architecture_diagram_1766144572195.png)

1.  **Data Ingestion**: Multi-source CSV ingestion into a local SQLite database (`inventory.db`) via `ingestion_db.py`.
2.  **Processing & Cleaning**: SQL-based transformation and data cleaning.
3.  **Analytical Engine**: Python-driven statistical analysis and insight generation within `report.md.ipynb`.
4.  **BI Presentation**: Final reporting and visualization via PowerBI (`vendor_performance_summary.pbix`).

---

## Key Visual Insights & Business Impact

### 1. Market Opportunities & High-Margin Brands
We identified **198 brands** that currently exhibit lower sales volume but maintain significantly higher profit margins. These represent immediate growth opportunities through:
*   Targeted marketing campaigns.
*   Strategic promotions to increase volume without sacrificing unit profitability.

### 2. Vendor Dependency Analysis
The analysis reveals a high concentration of dependency:
*   The **top 10 vendors contribute ~65.69%** of total purchases.
*   *Recommendation*: Diversify the vendor ecosystem to mitigate supply chain risks and increase bargaining power.

### 3. Cost Savings via Bulk Purchasing
Statistical analysis confirms that bulk purchasing strategies are highly effective:
*   Large quantity orders receive a **72% lower unit cost** ($10.78 vs. higher ad-hoc pricing).
*   *Action*: Realign procurement strategies to favor bulk orders for high-turnover items.

### 4. Inventory Health & Capital Optimization
*   **Total Unsold Inventory Capital**: $2.71M.
*   Identifying slow-moving inventory allows for better stock management, reducing storage costs and freeing up working capital.

---

## Technical Validation

### Hypothesis Testing
We performed statistical validation to compare profit margins between top-performing and low-sales vendors.
*   **Result**: The null hypothesis was rejected, confirming that different vendor segments operate under distinctly different profitability models, requiring tailored management strategies.

---

## Project Structure

*   `ingestion_db.py`: The ETL script responsible for loading raw data into the SQLite database.
*   `report.md.ipynb`: The primary analysis notebook containing data cleaning, visualizations, and statistical tests.
*   `vendor_performance_summary.pbix`: PowerBI dashboard for interactive performance tracking.
*   `inventory.db`: Local SQLite database storing the processed inventory and sales data.
*   `data/`: Directory containing raw CSV files (Inventory, Sales, Purchases).
*   `logs/`: Execution logs for the ingestion and processing scripts.

---

## Setup & Usage

### Prerequisites
*   Python 3.8+
*   SQLite3
*   PowerBI Desktop (for .pbix viewing)

### Installation
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install pandas sqlalchemy
    ```
3.  Run the data ingestion script:
    ```bash
    python ingestion_db.py
    ```
4.  Open `report.md.ipynb` in any Jupyter environment to view the detailed analysis.

---
*Developed as part of the Vendor Analytics Optimization Initiative.*
