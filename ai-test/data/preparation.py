import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Loading MNIST data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Data preparation
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Create mnist.npz file
np.savez('mnist.npz', x_train=train_images, y_train=train_labels, x_test=test_images, y_test=test_labels)
