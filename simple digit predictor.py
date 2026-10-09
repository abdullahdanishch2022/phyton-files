import tensorflow as tf
from tensorflow.keras import layers, modles
import matplotlib.pyplot as plt


(x_train, x_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


model = models.sequential([
    layers.flatten(input_shape=28,28)),
    layers.dense(128,activation='relu'),
    layers.dense(10, activation='softmax')
])

model.compile(optimizer='adam',
    loss='sparse_catogorical_crossentropy',
    metrics=['accuracy'])

model.fit(x_train, y_train, espochs=5)

test_loss, test_acc=model.evaluate(x_test, y_test)
print(f"test accuracy: {test_acc}")

prdictions= model.predict(x_test)

plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"predicted: {predictions[0].argmax}")
plt.show()