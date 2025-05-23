import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

podaci = pd.read_csv('occupancy_processed.csv')

X = podaci.loc[:, ['S3_Temp', 'S5_CO2']].to_numpy()  # ostavljeno točno ovako
y = podaci['Room_Occupancy_Count'].to_numpy()

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

skal = StandardScaler()
x_train = skal.fit_transform(x_train)  # koristim novu varijablu za skalirano
x_test = skal.transform(x_test)

model = DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)

y_pred = np.array(model.predict(x_test))

matrica = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(matrica)
disp.plot()
plt.title("Matrica zabune")
plt.show()

print("Izvještaj klasifikacije:\n")
print(classification_report(y_test, y_pred, target_names=["Slobodna", "Zauzeta"]))

plt.figure(figsize=(12, 6))
plot_tree(model, feature_names=["S3_Temp", "S5_CO2"], class_names=["Slobodna", "Zauzeta"], filled=True)
plt.title("Stablo odlučivanja")
plt.show()
