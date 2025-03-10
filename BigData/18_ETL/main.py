import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore
import seaborn as sns

#! 1-2 Load the Excel file and scope
file_path = "Financial_Sample.xlsx"  # Update with the correct file path
df = pd.read_excel(file_path)

# Display the first few rows
print(df.head())
# print(df.info())
# print(df.describe())

df.columns = df.columns.str.strip()
print(df.columns.tolist())
df_filtered = df.copy()

#!0 outlayer detection usin z-score
def detect_outliers_zscore(column, threshold=3):
    z_scores = zscore(column)
    return column[abs(z_scores) > threshold]

# Apply to each column
for column in ['Sales', 'Units Sold', 'Profit']:
    outliers = detect_outliers_zscore(df_filtered[column])
    df_filtered = df_filtered[~df_filtered[column].isin(outliers)]
    print(f"Z-Score Outliers for {column}:")
    print(f"Number of Outliers: {len(outliers)}")
    print(outliers)

    print("-" * 60)

# Get unique values for each non-numeric column
for column in df.select_dtypes(include=['object', 'datetime64[ns]']).columns:
    unique_values = df_filtered[column].unique()
    print(f"Column: {column}")
    print(f"Unique Values: {unique_values}")
    print(f"Number of Unique Values: {len(unique_values)}")
    print("-" * 40)

print("Cantidad de valores en Discount Band",df_filtered['Discount Band'].value_counts(dropna=False))

#!3 Group by Segment and sum the Sales
sales_by_segment = df.groupby('Segment')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_segment.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Segment')
plt.xlabel('Segment')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#!4 Group by Country and sum the Sales
sales_by_country = df.groupby('Country')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_country.plot(kind='bar', color='lightgreen')
plt.title('Total Sales by Country')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#!5 Monthly Profit Trends by Year
plt.figure(figsize=(12, 6))
for year in df_filtered["Year"].unique():
    monthly_data = df_filtered[df_filtered["Year"] == year].groupby("Month Number")["Profit"].sum()
    plt.plot(monthly_data.index, monthly_data.values, marker="o", linestyle="-", label=str(year))

plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Monthly Profit Trends by Year")
plt.xticks(ticks=range(1, 13), labels=df_filtered["Month Name"].unique(), rotation=45)
plt.legend(title="Year")
plt.grid(True)
plt.show()

#!6 Group by Product and sum the Sales
sales_by_product = df.groupby('Product')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_product.plot(kind='bar', color='orange')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#!7 Group by Discount Band and sum the Sales
sales_by_discount = df.groupby('Discount Band')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_discount.plot(kind='bar', color='purple')
plt.title('Total Sales by Discount Band')
plt.xlabel('Discount Band')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#! Correlation matrix and heatmap
numeric_columns = [
    'Units Sold', 'Manufacturing Price', 'Sale Price', 'Gross Sales', 
    'Discounts', 'Sales', 'COGS', 'Profit'
]
correlation_matrix = df_filtered[numeric_columns].corr()
print("Correlation matrix:")
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix between Numeric Variables')
plt.tight_layout()
plt.show()