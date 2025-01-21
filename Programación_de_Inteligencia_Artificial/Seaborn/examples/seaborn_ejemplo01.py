import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Simulación de datos de recomendaciones
data = pd.DataFrame({
    'user': ['A', 'B', 'C', 'D', 'E'],
    'recommended_items': [5, 3, 8, 2, 7],
    'click_rate': [0.8, 0.6, 0.9, 0.3, 0.7]
})

sns.barplot(data=data, x="user", y="recommended_items", palette="viridis")
plt.title("Items recomendados por usuario")
plt.show()