import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Cargar datos combinados
df = pd.read_csv("data/merged_dataset.csv")

# Variables de entrada (clima + vegetación + topografía)
features = ["temp", "humidity", "wind", "precipitation", "ndvi"]
X = df[features]
y = df["fire_occurred"]  # 1 = incendio, 0 = no

# Entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, "model/fire_model.pkl")
