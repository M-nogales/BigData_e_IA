import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore
import seaborn as sns

# Load the Excel file
file_path = "Financial_Sample.xlsx"  # Update with the correct file path
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()
print(df.columns.tolist())

# columns_to_check = ['Sales', 'Units Sold', 'Profit']

# # Calculate the mean and threshold for each column
# outliers = {}
# for column in columns_to_check:
#     mean = df[column].mean()
#     lower_threshold = mean - (0.3 * mean)
#     upper_threshold = mean + (0.3 * mean)
    
#     # Find outliers
#     column_outliers = df[(df[column] < lower_threshold) | (df[column] > upper_threshold)]
#     outliers[column] = column_outliers

#     # Print results
#     print(f"Outliers for {column}:")
#     print(f"Mean: {mean:.2f}")
#     print(f"Lower Threshold: {lower_threshold:.2f}")
#     print(f"Upper Threshold: {upper_threshold:.2f}")
#     print(f"Number of Outliers: {len(column_outliers)}")
#     print(column_outliers[['Segment', 'Country', 'Product', column]])
#     print("-" * 60)

# # Optionally, save outliers to a dictionary or DataFrame
# outliers_df = pd.concat(outliers.values(), keys=outliers.keys())

#! IQR 53-4-103
# def detect_outliers_iqr(column):
#     Q1 = column.quantile(0.25)
#     Q3 = column.quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     return column[(column < lower_bound) | (column > upper_bound)]

# # Apply to each column
# for column in ['Sales', 'Units Sold', 'Profit']:
#     outliers = detect_outliers_iqr(df[column])
#     print(f"IQR Outliers for {column}:")
#     print(f"Number of Outliers: {len(outliers)}")
#     print(outliers)
#     print("-" * 60)

#! Z-Score 13-4-16

def detect_outliers_zscore(column, threshold=3):
    z_scores = zscore(column)
    return column[abs(z_scores) > threshold]

# Apply to each column
for column in ['Sales', 'Units Sold', 'Profit']:
    outliers = detect_outliers_zscore(df[column])
    print(f"Z-Score Outliers for {column}:")
    print(f"Number of Outliers: {len(outliers)}")
    print(outliers)
    print("-" * 60)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Units Sold', y='Sales', data=df)
plt.title('Scatterplot of Units Sold vs Sales')
plt.show()

# Function to detect outliers using Z-score
def detect_outliers_zscore(column, threshold=3):
    z_scores = zscore(column)
    return column[abs(z_scores) > threshold]

# Create a plot for each column
for column in ['Sales', 'Units Sold', 'Profit']:
    # Calculate Z-scores and outliers
    z_scores = zscore(df[column])
    outliers = detect_outliers_zscore(df[column])
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot the original data
    plt.scatter(df.index, df[column], label='Data', color='blue', alpha=0.6)
    
    # Highlight outliers
    plt.scatter(outliers.index, outliers, label='Outliers', color='red', edgecolor='black', s=100)
    
    # Add Z-score thresholds
    threshold = 3
    mean = df[column].mean()
    std = df[column].std()
    upper_threshold = mean + threshold * std
    lower_threshold = mean - threshold * std
    
    plt.axhline(upper_threshold, color='green', linestyle='--', label=f'Upper Threshold ({upper_threshold:.2f})')
    plt.axhline(lower_threshold, color='orange', linestyle='--', label=f'Lower Threshold ({lower_threshold:.2f})')
    
    # Add labels and title
    plt.title(f'Z-Score Outlier Detection for {column}')
    plt.xlabel('Index')
    plt.ylabel(column)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()