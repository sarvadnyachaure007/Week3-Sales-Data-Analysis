from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sales_data.csv"


def main():
    # Load the CSV dataset.
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)

    print("WEEK 3: SALES DATA ANALYSIS")
    print("\nFirst five rows:")
    print(df.head().to_string(index=False))

    # Explore the dataset before cleaning.
    print("\nOriginal dataset shape:", df.shape)
    print("\nColumn data types:")
    print(df.dtypes)
    print("\nMissing values before cleaning:")
    print(df.isna().sum())

    # Convert numeric columns into numeric data types.
    for col in ["Quantity", "Unit_Price", "Total_Sales"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove exact duplicate records.
    duplicates_removed = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()

    # Fill missing sales using quantity multiplied by unit price.
    estimated_sales = df["Quantity"] * df["Unit_Price"]
    df["Total_Sales"] = df["Total_Sales"].fillna(estimated_sales)

    # Fill missing quantity and price with their respective medians.
    for col in ["Quantity", "Unit_Price"]:
        if df[col].isna().all():
            raise ValueError(f"No valid values available for {col}")
        df[col] = df[col].fillna(df[col].median())

    # Fill missing text fields with a clear label.
    df["Product"] = df["Product"].fillna("Unknown")
    df["Order_ID"] = df["Order_ID"].fillna("Unknown")
    df["Date"] = df["Date"].fillna("Unknown")

    # Recalculate revenue consistently.
    df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

    # Save the cleaned dataset.
    df.to_csv(BASE_DIR / "cleaned_sales_data.csv", index=False)

    # Calculate summary metrics.
    total_revenue = df["Total_Sales"].sum()
    average_sale = df["Total_Sales"].mean()
    highest_sale = df["Total_Sales"].max()
    lowest_sale = df["Total_Sales"].min()
    total_units = df["Quantity"].sum()

    # Group sales by product to identify the best performer.
    product_revenue = df.groupby("Product")["Total_Sales"].sum()
    product_units = df.groupby("Product")["Quantity"].sum()

    best_revenue_product = product_revenue.idxmax()
    best_units_product = product_units.idxmax()

    print("\nDATA CLEANING")
    print("Duplicate rows removed:", duplicates_removed)
    print("Rows after cleaning:", len(df))
    print("Missing values after cleaning:")
    print(df.isna().sum())

    print("\nSALES METRICS")
    print(f"Total revenue: Rs. {total_revenue:,.2f}")
    print(f"Average sale: Rs. {average_sale:,.2f}")
    print(f"Highest sale: Rs. {highest_sale:,.2f}")
    print(f"Lowest sale: Rs. {lowest_sale:,.2f}")
    print(f"Total units sold: {total_units:,.2f}")
    print("Best product by revenue:", best_revenue_product)
    print("Best product by units sold:", best_units_product)

    # Format the product revenue table for the report.
    product_table = product_revenue.rename(
        "Revenue (Rs.)"
    ).reset_index().to_markdown(index=False)

    # Generate the report automatically.
    report = f"""# Sales Data Analysis Report

## Project Overview
This project analyzes sample sales data using Python and pandas.

## Dataset
- Original rows: 16
- Records after duplicate removal: {len(df)}
- Duplicate rows removed: {duplicates_removed}
- Missing values after cleaning: {int(df.isna().sum().sum())}

## Key Metrics
| Metric | Result |
|---|---:|
| Total revenue | Rs. {total_revenue:,.2f} |
| Average sale | Rs. {average_sale:,.2f} |
| Highest sale | Rs. {highest_sale:,.2f} |
| Lowest sale | Rs. {lowest_sale:,.2f} |
| Total units sold | {total_units:,.2f} |

## Best-Selling Products
- Best product by revenue: **{best_revenue_product}**
- Best product by units sold: **{best_units_product}**

## Revenue by Product
{product_table}

## Cleaning Steps
1. Converted numeric fields to numeric types.
2. Removed duplicate records.
3. Filled missing sales from quantity and unit price.
4. Filled remaining missing quantities and prices with column medians.
5. Recalculated sales consistently.
6. Saved cleaned_sales_data.csv.

## Conclusion
The analysis calculates sales performance and identifies leading products.
All findings are based on the sample educational dataset.

## How to Run
Install dependencies using `python -m pip install -r requirements.txt`.
Run `python sales_analysis.py`.
"""

    (BASE_DIR / "analysis_report.md").write_text(
        report, encoding="utf-8"
    )

    print("\nReport created: analysis_report.md")
    print("Cleaned data created: cleaned_sales_data.csv")
    print("\nAnalysis completed successfully!")


if __name__ == "__main__":
    main()
