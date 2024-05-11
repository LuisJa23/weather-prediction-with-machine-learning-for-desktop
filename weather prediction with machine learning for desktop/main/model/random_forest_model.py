
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv("../resources/weatherAUS_balanced_and_clean.csv")


# Dividir los datos en características (X) y etiquetas (y)
X = data.drop("RainToday", axis=1)
y = data["RainToday"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir los hiperparámetros para la búsqueda en la grilla
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Inicializar el modelo de Random Forest
rf_model = RandomForestClassifier(random_state=42)

# Configurar la búsqueda en la grilla
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)

# Entrenar el modelo utilizando la búsqueda en la grilla
grid_search.fit(X_train, y_train)

# Obtener los mejores hiperparámetros encontrados por la búsqueda en la grilla
best_params = grid_search.best_params_
print("Mejores hiperparámetros:", best_params)

# Utilizar los mejores hiperparámetros para entrenar el modelo final
best_rf_model = RandomForestClassifier(**best_params, random_state=42)
best_rf_model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
predictions = best_rf_model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, predictions)
print("Precisión del modelo:", accuracy)

# Mostrar la matriz de confusión
cm = confusion_matrix(y_test, predictions)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["No Rain", "Rain"], yticklabels=["No Rain", "Rain"])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
