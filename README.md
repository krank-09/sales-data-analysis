# Data-Analysis-Basic-
Module purpose
--------------
This script downloads a sales dataset, performs basic cleaning and type fixes,
computes summary statistics and aggregates, visualizes revenue trends, and
exports cleaned data and plots to files.

High-level workflow
-------------------
1. Download dataset using kagglehub.dataset_download and read into a pandas DataFrame.
2. Inspect the data (head, info, describe).
3. Clean the data:
    - Remove duplicate rows.
    - Drop rows missing essential 'Revenue' values.
    - Fill remaining missing values for categorical columns ('Country', 'State') with 'Unknown'.
4. Fix data types:
    - Convert 'Date' column to pandas datetime.
5. Compute numeric summaries using NumPy and pandas:
    - Identify transactions with revenue above the dataset mean.
    - Compute total and average revenue.
    - Aggregate revenue by product and by month.
6. Visualize:
    - Line chart of monthly revenue.
    - Bar chart of top 15 products by revenue.
    - Save plots to PNG files.
7. Export cleaned DataFrame to CSV.

Main variables created
----------------------
path (str)
     Filesystem path returned from kagglehub.dataset_download for the downloaded dataset.

df (pandas.DataFrame)
     The main DataFrame holding sales data after reading the CSV.

high_revenue (pandas.DataFrame)
     Subset of df where 'Revenue' > mean revenue.

total_revenue (float)
     Sum of the 'Revenue' column.

avg_revenue (float)
     Mean of the 'Revenue' column.

revenue_by_category (pandas.Series)
     Sum of revenue grouped by 'Product'.

monthly_revenue (pandas.Series)
     Sum of revenue grouped by month number (1-12), derived from df['Date'].

top_products (pandas.Series)
     Top 15 products by revenue, sorted descending, used for plotting.

Files produced
--------------
- monthly_revenue.png         : Line plot showing monthly revenue trend.
- revenue_by_product.png      : Horizontal bar plot of top 15 products by revenue.
- cleaned_sales_data.csv      : CSV export of the cleaned DataFrame.

Key libraries used and their roles
---------------------------------
- kagglehub
     Utility used here to download the dataset programmatically
     (kagglehub.dataset_download(dataset_identifier) -> path).

- pandas (imported as pd)
     Primary data structure and I/O:
     - pd.read_csv: read CSV into DataFrame.
     - DataFrame methods: drop_duplicates, dropna, fillna, to_datetime, groupby, to_csv, head, info, describe.
     - Series/DataFrame indexing and assignment (e.g., creating 'Month_Num').

- numpy (imported as np)
     Numeric operations and aggregates:
     - np.mean: compute mean of numeric arrays or Series.
     - np.sum: compute sum of numeric arrays or Series.
     Used here alongside pandas aggregates for clarity and compatibility.

- matplotlib.pyplot (imported as plt)
     Low-level plotting utility:
     - plt.figure: create a new figure with a specified size.
     - plt.title/xlabel/ylabel: add labels and titles.
     - plt.savefig: save the current figure to a file.
     - plt.show: display the figure (interactive contexts).

- seaborn (imported as sns)
     High-level statistical plotting built on matplotlib:
     - sns.lineplot: convenient line chart (used for monthly trend).
     - sns.barplot: horizontal bar chart (used for top products).
     - palette argument for color styling.

Important pandas / NumPy / plotting keywords and operations explained
--------------------------------------------------------------------
- import
     Brings modules into the script namespace so their functions/classes can be used.

- pd.read_csv(path)
     Reads a CSV file from the given path into a pandas DataFrame.

- DataFrame.drop_duplicates(inplace=True)
     Removes duplicate rows. inplace=True mutates the DataFrame rather than returning a copy.

- DataFrame.dropna(subset=[...], inplace=True)
     Drops rows where specified columns contain NA. Here used to enforce presence of 'Revenue'.

- DataFrame.fillna(mapping)
     Replaces NA values using a dictionary mapping column -> fill value.

- pd.to_datetime(series)
     Converts a column of strings (or other date-like formats) to pandas datetime dtype for time-based operations.

- DataFrame.groupby(keys)['Revenue'].sum()
     Groups rows by one or more keys and aggregates the 'Revenue' column by summation; returns a Series indexed by the grouping key(s).

- Series.dt.month
     Accessor to extract the month number from datetime Series (after conversion with to_datetime).

- np.mean and np.sum
     Compute mean and sum respectively. Can be applied directly to pandas Series (NumPy will operate on the underlying array).

- Boolean indexing: df[df['Revenue'] > np.mean(df['Revenue'])]
     Filters rows based on a condition, producing a new DataFrame subset.

- plt.figure(figsize=(w, h))
     Creates a new figure with width w and height h in inches.

- sns.lineplot / sns.barplot
     High-level functions for drawing line and bar charts. They accept pandas Series or arrays as data and integrate with matplotlib for labeling and saving.

- plt.savefig(filename)
     Writes the current figure to the given filename; save before calling plt.show() in non-interactive or scripted contexts to ensure the saved image is complete.

- DataFrame.to_csv(filename, index=False)
     Exports the DataFrame to CSV. index=False prevents writing row index as a separate column.

Assumptions & notes
-------------------
- The script assumes the dataset contains at least the following columns: 'Date', 'Revenue', 'Product', 'Country', 'State'.
- The kagglehub.dataset_download function is assumed to return a directory path (string) where "Sales_Data.csv" resides.
- Revenue aggregation assumes 'Revenue' is numeric; non-numeric strings would require conversion/cleaning prior to numeric operations.
- The script uses inplace operations; if immutability or pipeline-style transformations are preferred, remove inplace and reassign variables.
- For reproducibility and testing, consider parameterizing input/output paths and adding logging or command-line argument parsing.

Example usage
-------------
Run the script as a standalone module (e.g., python data_analysis.py) in an environment where kagglehub is configured and the required libraries are installed.

License / attribution
---------------------
This docstring documents the behavior of the script and the standard open-source libraries it uses (pandas, numpy, matplotlib, seaborn). 
