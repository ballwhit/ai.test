import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

# Loading the trained model
model = load_model('mnist_model.h5')

# Loading data for prediction (example)
image_path = 'path_to_image.jpg' # Path to image to predict
image = tf.keras.preprocessing.image.load_img(image_path, color_mode='grayscale', target_size=(28, 28))
input_array = tf.keras.preprocessing.image.img_to_array(image)
input_array = np.expand_dims(input_array, axis=0)
input_array /= 255.0 # Data normalization

# Class prediction
predictions = model.predict(input_array)
predicted_class = np.argmax(predictions)

print(f'Predicted class: {predicted_class}')
