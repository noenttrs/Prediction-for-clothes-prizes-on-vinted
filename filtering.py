import pandas as pd

# Charger le dataset
dataset = pd.read_excel('Clothes.xlsx')

# Calculer la médiane par marque et état
moyenne_par_marque_etat = dataset.groupby(['Brand', 'Status', 'Size', 'Type'])['Price'].mean().reset_index()

# Calculer l'écart par rapport à la moyenne
dataset = dataset.merge(moyenne_par_marque_etat, on=['Brand', 'Status', 'Size', 'Type'], suffixes=('', '_average'))
dataset['Range'] = dataset['Price'] - dataset['Price_average']

# Définir une limite d'écart acceptable
limite_ecart = 10

# Filtrer les vêtements trop éloignés de la moyenne
vêtements_filtres = dataset[abs(dataset['Range']) < limite_ecart]

# Stocker les vêtements filtrés dans un fichier Excel

# afficher les differents status possibbles
print(dataset['Status'].unique())
print(dataset['Brand'].unique())
print(dataset['Size'].unique())

vêtements_filtres.to_excel('Clothes_filtered.xlsx', index=False)

