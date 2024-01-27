# Import des bibliothèques nécessaires
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import joblib


# Chargement du dataset depuis un fichier Excel
df = pd.read_excel('Datasets/Clothes_filtered.xlsx')

# Ajouter une ligne de données pour tester le modèle
#df = df.append({'Brand': 'Nike', 'Size': 'M', 'Status': 'Neuf avec étiquette', 'Type': 'Tshirt', 'Price': 30}, ignore_index=True)

# Transformation des données catégories en variables indicatrices
df = pd.get_dummies(df, columns=['Brand', 'Size', 'Status', 'Type'], drop_first=True)

print(df.head())

# Séparation des données en features (X) et target (y)
X = df.drop(['Price'], axis=1)  # Modification ici
y = df['Price']


# Séparation des données en ensemble d'entraînement et ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création et entraînement du modèle RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# Export du modèle
model_path = 'models/model.joblib'
joblib.dump(model, model_path)
print(f"Random Forest Model saved at {model_path}")


# Prédiction sur l'ensemble de test
predictions = model.predict(X_test)

print('Analyse des prédictionns sur l\'ensemble de test')
#print(predictions)
   

# afficher l'ecart le plus important
print(f"Plus grand écart : {max(abs(predictions - y_test).round(2))} €")

# afficher l'ecart le plus faible
print(f"Plus petit écart : {min(abs(predictions - y_test).round())} €")   


# Évaluation du modèle
mae = mean_absolute_error(y_test, predictions)
print(f"Erreur moyenne: {round(mae, 2)} €")