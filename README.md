# Week 3: Sales Data Analysis

## Requirements
- Python 3.10 or newer
- pandas

## Installation on Windows
Open PowerShell in this folder and run:

    python -m pip install -r requirements.txt
    python sales_analysis.py

If the `python` command is unavailable, use `py` instead.

## Project Files
- sales_analysis.py: main analysis program
- sales_data.csv: sample sales dataset
- requirements.txt: Python dependencies
- analysis_report.md: generated report
- cleaned_sales_data.csv: generated cleaned dataset
- tests/test_sales_analysis.py: automated tests

## Analysis
The program handles missing values, removes duplicate rows,
calculates sales metrics, and ranks products by revenue.

## Testing
Run:

    python -m unittest discover -s tests -v

## Submission
Capture genuine screenshots of the terminal output, cleaned CSV,
and generated report before submitting to GitHub.
