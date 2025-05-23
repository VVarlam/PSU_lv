import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

podatci = pd.read_csv('occupancy_processed.csv')

X = podatci.loc[:, ['S3_Temp', 'S5_CO2']].to_numpy()
y = podatci['Room_Occupancy_Count'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_predicted = np.array(model.predict(X_test))

cm = confusion_matrix(y_test, y_predicted)
ConfusionMatrixDisplay(cm, display_labels=["Slobodna", "Zauzeta"]).plot(cmap="Oranges")
plt.title("Matrica zabune - Decision Tree")
plt.grid(False)
plt.show()

print("Rezultati klasifikatora:\n")
print(classification_report(y_test, y_predicted, target_names=["Slobodna", "Zauzeta"]))

plt.figure(figsize=(12, 6))
plot_tree(model, feature_names=["S3_Temp", "S5_CO2"], class_names=["Slobodna", "Zauzeta"], filled=True)
plt.title("Stablo odlučivanja")
plt.show()
