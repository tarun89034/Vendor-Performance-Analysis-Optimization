# Data Directory

This directory contains the datasets used for the Vendor Performance Analysis project.

## Required Data Files

The following CSV files are required to run the analysis:

- `begin_inventory.csv` - Beginning inventory data
- `end_inventory.csv` - Ending inventory data
- `purchase_prices.csv` - Purchase price information
- `purchases.csv` - Purchase transaction data (~345 MB)
- `sales.csv` - Sales transaction data (~1.5 GB)
- `vendor_invoice.csv` - Vendor invoice information

## Setup Instructions

1. **Obtain the data files** from the project owner or data source
2. **Place all CSV files** in this `data/` directory
3. **Verify** that all 6 files are present before running the analysis notebooks

## Note

These data files are not included in the Git repository due to their large size (total ~2 GB). They are excluded via `.gitignore` to keep the repository lightweight and follow best practices for version control.

## Database

The analysis scripts will create an `inventory.db` SQLite database file in the project root directory. This file is also excluded from version control.
