import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = kagglehub.dataset_download("jehanzaibbhatti/sales-data")
df = pd.read_csv(path + "/Sales_Data.csv")

print(df.head())
print(df.info())
print(df.describe())

# Clean data
df.drop_duplicates(inplace=True)
df.dropna(subset=['Revenue'], inplace=True)
df = df.fillna({'Country': 'Unknown', 'State': 'Unknown'})

# Fix data types
df['Date'] = pd.to_datetime(df['Date'])

# NumPy operations
high_revenue = df[df['Revenue'] > np.mean(df['Revenue'])]
print(f"\nHigh revenue transactions: {len(high_revenue)}")
print(high_revenue.head())

# Revenue stats
total_revenue = np.sum(df['Revenue'])
avg_revenue = np.mean(df['Revenue'])
print(f"\nTotal Revenue: {total_revenue}")
print(f"Average Revenue: {avg_revenue:.2f}")

# Revenue by product & monthly trends
revenue_by_category = df.groupby('Product')['Revenue'].sum()
print("\nRevenue by Product:\n", revenue_by_category)

df['Month_Num'] = df['Date'].dt.month
monthly_revenue = df.groupby('Month_Num')['Revenue'].sum()
print("\nMonthly Revenue:\n", monthly_revenue)

# Line chart: Monthly revenue trend
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_revenue, marker='o')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.savefig('monthly_revenue.png')   # Save BEFORE show()
plt.show()

# Bar chart: Top 15 products by revenue (much cleaner)
plt.figure(figsize=(14, 7))
top_products = revenue_by_category.sort_values(ascending=False).head(15)
sns.barplot(x=top_products.values, y=top_products.index, palette='Blues_r')
plt.title('Top 15 Products by Revenue', fontsize=16, fontweight='bold')
plt.xlabel('Revenue', fontsize=12)
plt.ylabel('Product', fontsize=12)
plt.tight_layout()
plt.savefig('revenue_by_product.png')
plt.show()

# Export cleaned data
df.to_csv('cleaned_sales_data.csv', index=False)
print("\nFiles saved: monthly_revenue.png, revenue_by_product.png, cleaned_sales_data.csv")