# tester.py

# Import des bibliothèques nécessaires
import pandas as pd
import joblib

# Chargement du modèle
model_path = 'models/model.joblib'
model = joblib.load(model_path)
print(f"Model loaded from {model_path}")

brand = input("Brand : ")
size = input("Size : ")
status = input("Status : ")
type = input("Type : ")



# Création d'un DataFrame à partir des données de test
df = pd.DataFrame([brand, size, status, type]).T
df.columns = ['Brand', 'Size', 'Status', 'Type']
df['Brand'] = df['Brand'].map({'Nike': 1, 'adidas': 2, 'Carhartt': 3, 'The North Face': 4, 'Tommy Hilfiger': 5, 'Lacoste': 6, 'Stüssy': 7, 'Napapijri': 8, 'Ralph Lauren': 9, 'Dickies': 10, 'Jack & Jones': 11, "Levi's": 12, 'Burberry': 13})
df['Size'] = df['Size'].map({
    'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5, 'XS': 6, '4XL': 7, 'Universel': 8,
    'XXXL': 9, '6XL': 10, 'W32 | FR 42': 11, 'W36 | FR 46': 12, 'W34 | FR 44': 13,
    'W31 | FR 40': 14, 'W30 | FR 40': 15, 'W33 | FR 42': 16, 'W24 | FR 34': 17,
    'W38 | FR 48': 18, 'W28 | FR 38': 19, 'W23 | FR 32': 20, 'W26 | FR 36': 21,
    'W40 | FR 50': 22, '2XL': 23, 'W29 | FR 38': 24, 'W27 | FR 36': 25,
    'W52 | FR 62': 26, 'W25 | FR 34': 27, 'W42 | FR 52': 28, 'W50 | FR 60': 29,
    'W48 | FR 58': 30, 'W44 | FR 54': 31, '3XL': 32, 'W35 | FR 44': 33,
    'W46 | FR 56': 34, '8XL': 35, 'W54 | FR 64': 36, '5XL': 37, '41 cm': 38,
    '40 cm': 39, '42 cm': 40, '38 cm': 41, '43 cm': 42
})
df['Status'] = df['Status'].map({"Neuf": 1, "Neuf sans étiquette": 2, "Très bon état": 3, "Bon état": 4, "Satifaisant": 5})
df['Type'] = df['Type'].map({"Coast": 1, "Pant": 2, "Sweet": 3, "Tshirt":4})  # Ajout de la colonne 'Type'

df = pd.get_dummies(df, columns=['Brand', 'Size', 'Status', 'Type'], drop_first=True)

# Utilisation du modèle pour faire des prédictions
predictions = model.predict(df)

# Affichage des prédictions
print("Predictions:")
for i, prediction in enumerate(predictions):
    print(f"Test {i+1}: Estimated Price = {prediction}")
