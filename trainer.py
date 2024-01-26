# Import des bibliothèques nécessaires
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import joblib


# Chargement du dataset depuis un fichier Excel
df = pd.read_excel('Datasets/Clothes_filtered.xlsx')

# Transformation des données catégoriques en variables numériques
df['Brand'] = df['Brand'].map({
    'Nike': 1, 'adidas': 2, 'Carhartt': 3, 'The North Face': 4, 'Tommy Hilfiger': 5, 
    'Lacoste': 6, 'Stüssy': 7, 'Napapijri': 8, 'Ralph Lauren': 9, 'Dickies': 10, 
    'Jack & Jones': 11, "Levi's": 12, 'Burberry': 13})
df['Size'] = df['Size'].map({
    'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5, 'XS': 6, '4XL': 7, 'Universel': 8,
    'XXXL': 9, '6XL': 10, 'W32 | FR 42': 11, 'W36 | FR 46': 12, 'W34 | FR 44': 13,
    'W31 | FR 40': 14, 'W30 | FR 40': 15, 'W33 | FR 42': 16, 'W24 | FR 34': 17,
    'W38 | FR 48': 18, 'W28 | FR 38': 19, 'W23 | FR 32': 20, 'W26 | FR 36': 21,
    'W40 | FR 50': 22, '2XL': 23, 'W29 | FR 38': 24, 'W27 | FR 36': 25,
    'W52 | FR 62': 26, 'W25 | FR 34': 27, 'W42 | FR 52': 28, 'W50 | FR 60': 29,
    'W48 | FR 58': 30, 'W44 | FR 54': 31, '3XL': 32, 'W35 | FR 44': 33,
    'W46 | FR 56': 34, '8XL': 35, 'W54 | FR 64': 36, '5XL': 37, '41 cm': 38,
    '40 cm': 39, '42 cm': 40, '38 cm': 41, '43 cm': 42})
df['Status'] = df['Status'].map({"Neuf avec étiquette": 1, "Neuf sans étiquette": 2, "Très bon état": 3, "Bon état": 4, "Satifaisant": 5})
df['Type'] = df['Type'].map({"Coast": 1, "Pant": 2, "Sweet": 3, "Tshirt":4})  # Ajout de la colonne 'Type'

# Transformation des données catégoriques en variables indicatrices
df = pd.get_dummies(df, columns=['Brand', 'Size', 'Status', 'Type'], drop_first=True)


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

print('Prédiction sur l\'ensemble de test')
print(predictions)


bests = []  # liste des meilleurs prédictions   
for i in range(len(predictions)):
    print(f"Prédiction : {predictions[i].round(1)} - Valeur attendue : {y_test.iloc[i]} - Différence : {predictions[i] - y_test.iloc[i].round(2)}")
    if(predictions[i] - y_test.iloc[i].round(2) > 5):
        if(len(bests) < 5):
            bests.append(predictions[i].round(1))
        else:
            bests.append(predictions[i].round(1))
            bests.sort()
            bests.pop(0)
        
print(bests)    

# afficher l'ecart le plus important
print(f"Plus grand écart : {max(abs(predictions - y_test).round(2))} €")

# afficher l'ecart le plus faible
print(f"Plus petit écart : {min(abs(predictions - y_test).round())} €")   


# Évaluation du modèle
mae = mean_absolute_error(y_test, predictions)
print(f"Erreur moyenne: {round(mae, 2)} €")