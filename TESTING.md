# Testing Guide

Run automated tests with:

    python -m unittest discover -s tests -v

Tests cover CSV loading, required columns, revenue arithmetic,
and duplicate detection.

Manual checks:
1. Run the main analysis script.
2. Confirm the metrics appear in the terminal.
3. Confirm analysis_report.md is created.
4. Confirm cleaned_sales_data.csv is created.
5. Confirm missing values are handled.
