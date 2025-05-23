from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

podatci = pd.read_csv("occupancy_processed.csv")

X = podatci.loc[:, ['S3_Temp', 'S5_CO2']].to_numpy()
y = podatci['Room_Occupancy_Count'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

y_predicted = model.predict(X_test)

cm = confusion_matrix(y_test, y_predicted)
ConfusionMatrixDisplay(cm, display_labels=["Slobodna", "Zauzeta"]).plot(cmap="Oranges")
plt.title("Matrica zabune - Logistička regresija")
plt.grid(False)
plt.show()

print("Točnost modela:", accuracy_score(y_test, y_predicted))
print("Rezultati klasifikatora:\n")
print(classification_report(y_test, y_predicted, target_names=['Slobodna', 'Zauzeta']))
