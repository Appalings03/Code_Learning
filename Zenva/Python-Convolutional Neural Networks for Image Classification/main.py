import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

print(len(x_train))
print(len(x_test))

# print(x_train[0])
# plt.imshow(x_train[0], cmap='gray')
# print(y_train[0])
# plt.imshow(x_test[0], cmap='gray')
# print(y_test[0])

from tensorflow.keras.layers import Conv2D, Flatten, Dense # type: ignore
from tensorflow.keras import Model # type: ignore

# Conv2D(filters, kernel_size, activation='relu')
# Flatten()
# Dense(neurons, activation)

class MNISTModel(Model):
    def __init__(self):
        super(MNISTModel, self).__init__()
        self.conv1 = Conv2D(32, 3, activation='relu')
        self.flatten = Flatten()
        self.dense1 = Dense(128, activation='relu')
        self.dense2 = Dense(10, activation='softmax')
        
    def call(self, x):
        x1 = self.conv1(x)
        x2 = self.flatten(x1)
        x3 = self.dense1(x2)
        return self.dense2(x3)

model = MNISTModel()
model()
loss_function = tf.keras.losses.SparseCategoricalCrossentropy()