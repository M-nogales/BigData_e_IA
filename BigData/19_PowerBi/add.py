import pandas as pd
import numpy as np

df = pd.read_csv('retail_ecommerce_sales_dataset.csv')
categorias_unicas = df['Product Category'].unique()

print("Categorías de productos únicas:")
print(categorias_unicas)

productos_por_categoria = {
    'Clothing': ['T-Shirt', 'Jeans', 'Dress', 'Jacket', 'Sweater'],
    'Beauty': ['Lipstick', 'Perfume', 'Face Cream', 'Shampoo', 'Mascara'],
    'Electronics': ['Smartphone', 'Headphones', 'Laptop', 'Smartwatch', 'Tablet']
}

# Rangos de stock por categoría (mínimo, máximo)
stock_por_categoria = {
    'Clothing': (50, 200),   # Ropa suele tener más stock
    'Beauty': (20, 100),     # Productos de belleza menos
    'Electronics': (5, 50)   # Electrónicos menos por ser más caros
}

# Función para asignar producto y stock
def asignar_producto_y_stock(categoria):
    producto = np.random.choice(productos_por_categoria.get(categoria, ['Unknown']))
    min_stock, max_stock = stock_por_categoria.get(categoria, (0, 10))
    stock = np.random.randint(min_stock, max_stock + 1)
    return producto, stock

# Aplicar la función y expandir en dos columnas
df[['Product Name', 'Stock']] = df['Product Category'].apply(
    lambda x: pd.Series(asignar_producto_y_stock(x))
)

# Mostrar el DataFrame actualizado
print(df.head())

# Guardar el nuevo dataset en un CSV
df.to_csv('retail_ecommerce_sales_with_products_and_stock.csv', index=False)
print("\nDataset guardado como 'retail_ecommerce_sales_with_products.csv'")