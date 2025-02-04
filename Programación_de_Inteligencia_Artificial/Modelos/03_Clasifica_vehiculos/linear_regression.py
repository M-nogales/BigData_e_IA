import pandas as pd
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('Dataset_Vehiculos.csv')

print('df.head(): ', df.head())

print('df.describe(): ', df.describe())
print('df.info(): ', df.info())

df['Mileage'] = df['Mileage'].fillna(df['Mileage'].median())

df = pd.get_dummies(df, columns=['FuelType', 'Transmission'], drop_first=True)

# Visualize the distribution of the target variable (Price)
plt.boxplot(df['Price'])
plt.title('Boxplot of Price')
plt.show()

# Remove outliers (example: removing data points beyond 1.5 * IQR)
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Price'] >= (Q1 - 1.5 * IQR)) & (df['Price'] <= (Q3 + 1.5 * IQR))]


# Features
X = df.drop(columns=['ID', 'Price'])
# Target
y = df['Price']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and test sets
# 20% of the data will be used for testing, 80% for training
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


# Model training
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predictions
y_pred = regressor.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Results
print(f"🔹 MSE (Error Cuadrático Medio): {mse:.2f}")
print(f"🔹 MAE (Error Absoluto Medio): {mae:.2f}")
print(f"🔹 R² (Coeficiente de Determinación): {r2:.2f}")

# Report
print("\n")

# comparation metrics
def metrics_result_comparation(mse, mae, r2, model):
    metrics = ['MSE', 'MAE', 'R²']
    values = [mse, mae, r2]
    
    # Create a bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(metrics, values, color=['blue', 'green', 'red'])
    
    # Add value labels on top of bars
    for i, v in enumerate(values):
        plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontsize=12, fontweight='bold')
    
    # Labels and title
    plt.ylim(0, max(values) + 0.1)
    plt.ylabel('Score')
    plt.title(f'Model metrics - {model}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

metrics_result_comparation(mse, mae, r2, model = 'Lineal Regression')