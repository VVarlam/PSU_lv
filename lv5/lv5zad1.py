import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Učitavanje skupa podataka
data_path = 'occupancy_processed.csv'
data = pd.read_csv(data_path)
print(f"Ukupno primjera u skupu podataka: {len(data)}")

# Definicija značajki i ciljne varijable
features = ['S3_Temp', 'S5_CO2']
label = 'Room_Occupancy_Count'
class_labels = {0: 'Slobodna', 1: 'Zauzeta'}

# Pretvorba podataka u NumPy nizove
X = data[features].values
y = data[label].values

# Vizualizacija podataka - dijagram raspršenja
plt.figure(figsize=(8, 6))
for class_val in np.unique(y):
    plt.scatter(
        X[y == class_val, 0],
        X[y == class_val, 1],
        label=class_labels[class_val],
        alpha=0.7
    )

plt.xlabel('Temperatura (S3_Temp)')
plt.ylabel('CO2 razina (S5_CO2)')
plt.title('Dijagram raspršenja: Zauzetost prostorije')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Ispis raspodjele po klasama
unique, counts = np.unique(y, return_counts=True)
print("Raspodjela po klasama:")
for value, count in zip(unique, counts):
    print(f" - {class_labels[value]}: {count} primjera")
