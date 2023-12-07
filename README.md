# Example of a Neural Network for Handwritten Number Recognition

This repository is a simple neural network built using TensorFlow and Keras libraries for handwritten digit recognition using the MNIST dataset.

## Repository Structure

- **src/:** Directory with source code.
   - **train_neural_network.py:** Script for training a neural network on the MNIST dataset.
   - **predict_neural_network.py:** Script for prediction using a trained model.

- **data/:** Directory with data and additional information.
   - **README.md:** Additional information about the data.

- **mnist_model.h5:** The file in which the trained neural network model is saved.

- **README.md:** The main README file with a description of the project, its structure and instructions.

- **requirements.txt:** File with a list of dependencies.

## Usage

1. Run `train_neural_network.py` to train the neural network.

     ```bash
     python train_neural_network.py
     ```

2. Run `predict_neural_network.py` to make predictions using the trained model.

     ```bash
     python predict_neural_network.py
     ```

## Dependencies

To install dependencies run:

```bash
pip install -r requirements.txt
```

## Additional Information
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
