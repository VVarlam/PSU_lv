import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

for i in range(5, 10):
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Broj: {y_train[i]}")
    plt.axis('off')
    plt.show()

x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)

model = Sequential()
model.add(keras.Input(shape=(784,)))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

fit = model.fit(x_train_s, y_train_s, epochs=5, batch_size=32)

train_loss, train_accuracy = model.evaluate(x_train_s, y_train_s, verbose=0)
test_loss, test_accuracy = model.evaluate(x_test_s, y_test_s, verbose=0)
print(f"Točnost na trening skupu: {train_accuracy:.2f}")
print(f"Točnost na testnom skupu: {test_accuracy:.2f}")

y_test_pred = model.predict(x_test_s)
y_test_pred_classes = np.argmax(y_test_pred, axis=1)

conf_matrix = confusion_matrix(y_test, y_test_pred_classes)
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=range(10))
disp.plot()
plt.title("Matrica zabune - testni skup")
plt.show()

y_train_pred = model.predict(x_train_s)
y_train_pred_classes = np.argmax(y_train_pred, axis=1)

conf_matrix_train = confusion_matrix(y_train, y_train_pred_classes)
disp_train = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_train, display_labels=range(10))
disp_train.plot()
plt.title("Matrica zabune - trening skup")
plt.show()

netocno = np.where(y_test != y_test_pred_classes)[0]
for i in range(5):
    index = netocno[i]
    plt.imshow(x_test[index], cmap='gray')
    plt.title(f"Stvarno: {y_test[index]}, Predviđeno: {y_test_pred_classes[index]}")
    plt.axis('off')
    plt.show()
