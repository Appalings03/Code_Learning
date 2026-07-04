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

loss_function = tf.keras.losses.SparseCategoricalCrossentropy()
optimiser = tf.keras.optimizers.Adam()

train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.SparseTopKCategoricalAccuracy(name='train_accuracy')

test_loss = tf.keras.metrics.Mean(name='test_loss')
test_accuracy = tf.keras.metrics.SparseTopKCategoricalAccuracy(name='test_accuracy')

@tf.function
def train_step(inputs, outputs):
    with tf.GradientTape() as tape:
        predictions = model(inputs)
        loss = loss_function(outputs, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimiser.apply_gradients(zip(gradients, model.trainable_variables))
    train_loss(loss)
    train_accuracy(outputs, predictions)
    
@tf.function
def test_step(inputs, outputs):
    predictions = model(inputs)
    loss = loss_function(outputs, predictions)

    test_loss(loss)
    test_accuracy(outputs, predictions)
    
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

train_data = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32)

test_data = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

epochs = 5

for epoch in range(epochs):
    for train_inputs, train_labels in train_data:
        train_step(train_inputs, train_labels)
    for test_inputs, test_labels in test_data:
        test_step(test_inputs, test_labels)
    
    template = 'Epochs: {}\n Train: loss {}\n Train Accuracy: {}\n Test loss: {}\n Test Accuracy: {}'
    print(template.format(
        epoch + 1,
        train_loss.result(),
        train_accuracy.result(),
        test_loss.result(),
        test_accuracy.result(),
    ))
    
    train_loss.reset_state()
    train_accuracy.reset_state()
    test_loss.reset_state()
    test_accuracy.reset_state()
    