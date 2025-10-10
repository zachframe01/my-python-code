"""Small example to read orders.csv using the real pandas package.

This file replaces the previous local `pandas.py` which shadowed the installed
pandas library. To run:
    python read_orders.py

It prints the first few rows of `orders.csv` if the file exists.
"""

import sys

try:
    import pandas as pd
except Exception as e:
    print("Error importing pandas:", e)
    print("If you don't have pandas installed, install it with: pip install pandas")
    sys.exit(1)

CSV_PATH = "orders.csv"

try:
    df = pd.read_csv(CSV_PATH)
except FileNotFoundError:
    print(f"File not found: {CSV_PATH}")
    sys.exit(1)
except Exception as e:
    print("Failed to read CSV:", e)
    sys.exit(1)

print("Loaded orders.csv successfully. DataFrame info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())
