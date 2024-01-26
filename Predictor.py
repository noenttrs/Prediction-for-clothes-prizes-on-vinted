import pandas as pd
import joblib

class ClothesPricePredictor:
    def __init__(self, model_path='models/model.joblib'):
        self.model_path = model_path
        self.model = joblib.load(model_path)

    def preprocess_input(self, brand, size, status, cloth_type):
        # Charger le DataFrame original
        df = pd.read_excel('Datasets/Clothes_filtered.xlsx')

        # Supprimer la colonne 'Price' si elle existe
        if 'Price' in df.columns:
            df = df.drop(['Price'], axis=1)

        # Récupérer le prix moyen de la marque, du type de vêtement et de la taille
        price_average, range = df[(df['Brand'] == brand) & (df['Type'] == cloth_type) & (df['Size'] == size)][['Price_average', 'Range']].values[0]

        # Ajouter une nouvelle ligne avec les entrées de l'utilisateur
        new_row = {'Brand': brand, 'Size': size, 'Status': status, 'Type': cloth_type, 'Price_average': price_average, 'Range': range}
        df.loc[len(df)] = new_row

        # Transformer les données catégoriques en variables numériques
        df.columns = ['Brand', 'Size', 'Status', 'Type', 'Price_average', 'Range']
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
        df['Status'] = df['Status'].map({"Neuf avec étiquette": 1, "Neuf sans étiquette": 2, "Très bon état": 3, "Bon état": 4, "Satifaisant": 5})
        df['Type'] = df['Type'].map({"Coast": 1, "Pant": 2, "Sweet": 3, "Tshirt":4})  # Ajout de la colonne 'Type'


        # Transformer les données catégoriques en variables indicatrices
        df = pd.get_dummies(df, columns=['Brand', 'Size', 'Status', 'Type'], drop_first=True)

        # Récupérer la dernière ligne du DataFrame (nouvelle entrée utilisateur)
        user_input = pd.DataFrame(df.iloc[-1].values)

        return user_input

    def predict_price(self, brand, size, status, cloth_type):
        # Prétraiter les entrées
        df = self.preprocess_input(brand, size, status, cloth_type).T

        # Faire des prédictions
        predictions = self.model.predict(df)

        return predictions[0]

# Exemple d'utilisation de la classe ClothesPricePredictor
if __name__ == "__main__":
    predictor = ClothesPricePredictor()

    # Entrées de l'utilisateur
    brand = input("Brand : ")
    size = input("Size : ")
    status = input("Status : ")
    cloth_type = input("Type : ")

    # Prédiction du prix
    predicted_price = predictor.predict_price(brand, size, status, cloth_type)
    print(f"Estimated Price: {predicted_price} €")
