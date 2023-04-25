import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense

import numpy as np


def FCN_keras_model(xTrain, xTest, yTrain, yTest):
    # flatten the input and output
    n_input = np.shape(xTrain)[1] * np.shape(xTrain)[2]
    xTrain = np.reshape(xTrain, (np.shape(xTrain)[0], n_input))
    n_output = np.shape(yTrain)[1] * np.shape(yTrain)[2]
    yTrain = np.reshape(yTrain, (np.shape(yTrain)[0], n_output))

    xTest = np.reshape(xTest, (np.shape(xTest)[0], n_input))
    yTest = np.reshape(yTest, (np.shape(yTest)[0], n_output))

    # define multi-layer perceptron model
    model = Sequential()
    
    #Input layer
    model.add(Dense(279, activation='sigmoid', input_shape=(n_input,)))
    
    #Hidden layers
    model.add(Dense(162, activation='sigmoid'))
    model.add(Dense(45, activation='sigmoid'))
    
    #Output layer
    model.add(Dense(n_output, activation='linear'))
    
    #Optimizer and learning rate
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=3e-5), loss='mse')

    # fit the keras model on the dataset
    history =model.fit(xTrain, yTrain, epochs=170 ,batch_size=72, 
                       verbose=1, validation_data=(xTest, yTest))

    # save the trained model
    filepath = 'FCN_model.h5'
    model.save(filepath)

    # load trained model
    model = keras.models.load_model('FCN_model.h5')

    # Training and validation loss plot
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model train vs validation loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper right')

    return model

if DATA_DRIVEN_PREDICTION:
    FCN_model =  FCN_keras_model(xTrain_data, xTest_data, yTrain_data, yTest_data)