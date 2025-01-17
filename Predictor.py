import json
import pandas as pd
import joblib
from http.server import BaseHTTPRequestHandler, HTTPServer

class ClothesPricePredictor:
    def __init__(self, model_path='models/model.joblib'):
        self.model_path = model_path
        self.model = joblib.load(model_path)

    def preprocess_input(self, brand, size, status, cloth_type, price):
        # Charger le DataFrame original
        df = pd.read_excel('Datasets/Clothes_filtered.xlsx')

        price = float(price)

        # Récupérer le prix moyen de la marque, du type de vêtement et de la taille
        price_average = df[(df['Brand'] == brand) & (df['Type'] == cloth_type) & (df['Size'] == size)][['Price_average']].values[0]

        # Ajouter une nouvelle ligne avec les entrées de l'utilisateur
        new_row = {'Brand': brand, 'Size': size, 'Price': 0, 'Status': status, 'Type': cloth_type, 'Price_average': price_average[0], 'Range': price_average[0] - price}
        df.loc[len(df)] = new_row

        # Transformer les données catégoriques en variables indicatrices
        df = pd.get_dummies(df, columns=['Brand', 'Size', 'Status', 'Type'], drop_first=True)

        df = df.drop(['Price'], axis=1)

        # Récupérer la dernière ligne du DataFrame (nouvelle entrée utilisateur)
        user_input = df.drop(df.index[:-1])

        return user_input

    def predict_price(self, brand, size, status, cloth_type, price):
        # Prétraiter les entrées
        df = self.preprocess_input(brand, size, status, cloth_type, price)

        # Faire des prédictions
        predictions = self.model.predict(df)

        return round(predictions[0], 2)

