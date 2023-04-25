import matplotlib.pyplot as plt
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.layers import LSTM


def my_lstm_model(data_input):
    data = data_input
    model = 0
    # design network
    """
    model = Sequential()    
    model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2,
                        shuffle=False)
    # plot history
    plt.plot(history.history['loss'], label='train')
    plt.plot(history.history['val_loss'], label='test')
    plt.legend()
    plt.show()
    """
    return model
