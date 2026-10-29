# Sales Data Analysis

A small pandas project: load a retail sales dataset from Kaggle, clean it, and look at where the revenue comes from.

- Removes duplicate rows and rows with no revenue, and fills missing country/state values with "Unknown"
- Totals revenue by product and by month
- Plots the monthly revenue trend and the top 15 products by revenue

## Run

```bash
pip install pandas numpy matplotlib seaborn kagglehub
python code.py
```

It downloads the [Sales Data](https://www.kaggle.com/datasets/jehanzaibbhatti/sales-data) dataset with `kagglehub`, saves the two charts as PNGs and writes `cleaned_sales_data.csv`.

This was one of my first data projects. Next I'd like to turn it into a notebook and add a short written summary of what the data shows.
