import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

podatci = pd.read_csv('occupancy_processed.csv')
X = podatci.loc[:, ['S3_Temp', 'S5_CO2']].values
y = podatci['Room_Occupancy_Count'].astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, shuffle=True, random_state=123
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train_scaled, y_train)

y_predicted = knn_model.predict(X_test_scaled)

cm = confusion_matrix(y_test, y_predicted)
ConfusionMatrixDisplay(cm, display_labels=["Slobodna", "Zauzeta"]).plot(cmap="Oranges")
plt.title("Matrica zabune KNN")
plt.grid(False)
plt.show()
e
print("Rezultati klasifikatora:\n")
print(classification_report(y_test, y_predicted, target_names=["Slobodna", "Zauzeta"]))
