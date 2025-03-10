import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore
import seaborn as sns

# Load the Excel file and scope
file_path = "Financial_Sample.xlsx"  # Update with the correct file path
df = pd.read_excel(file_path)

# Display the first few rows
print(df.head())
# print(df.info())
# print(df.describe())

df.columns = df.columns.str.strip()
print(df.columns.tolist())
df_filtered = df.copy()

# outlayer detection usin z-score
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



# Sales and profit distribution
plt.figure(figsize=(12, 5))
# Sales Histogram
plt.subplot(1, 2, 1)
plt.hist(df_filtered["Sales"], bins=30, color="skyblue", edgecolor="black")
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

# Profit Histogram
plt.subplot(1, 2, 2)
plt.hist(df_filtered["Profit"], bins=30, color="lightcoral", edgecolor="black")
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# sales over time
sales_over_time = df.groupby('Date')['Sales'].sum()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sales_over_time.index, sales_over_time.values, marker='o', linestyle='-')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Group by Month Name and sum the Sales
sales_by_month = df.groupby('Month Name')['Sales'].sum()

# Sort by month order (optional)
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]
sales_by_month = sales_by_month.reindex(month_order)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sales_by_month.index, sales_by_month.values, marker='o', linestyle='-', color='red')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Group by Segment and sum the Sales
sales_by_segment = df.groupby('Segment')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 8))
plt.pie(sales_by_segment, labels=sales_by_segment.index, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'violet'])
plt.title('Sales Distribution by Segment')
plt.tight_layout()
plt.show()

# Group by Year and sum the Sales
sales_by_year = df.groupby('Year')['Sales'].sum()

# Plot
plt.figure(figsize=(8, 5))
sales_by_year.plot(kind='bar', color='teal')
plt.title('Total Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Group by Segment and Country, then sum the Sales
sales_by_segment_country = df.groupby(['Segment', 'Country'])['Sales'].sum().unstack()

# Plot
sales_by_segment_country.plot(kind='bar', stacked=False, colormap='viridis')
plt.title('Sales by Segment and Country')
plt.xlabel('Segment')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend(title='Country')
plt.tight_layout()
plt.show()