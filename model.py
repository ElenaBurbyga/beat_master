from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, LSTM, Conv1D, MaxPooling1D, Flatten, Bidirectional, BatchNormalization, Activation
from keras.utils import np_utils


def build_bidirectional_lstm(input_window_len, n_feature, output_shape, dropout=0.2, neurons_per_layer=None):
    
    model = Sequential()
    model.add(LSTM(input_window_len, input_shape=(input_window_len, n_feature), dropout=dropout, return_sequences=True))
    model.add(Dropout(dropout))
    model.add(Bidirectional(LSTM(100, input_shape=(input_window_len, n_feature), dropout=dropout, recurrent_dropout=dropout)))
    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(output_shape, activation='softmax'))
    model.add(Activation('softmax'))
    model.add(BatchNormalization())
    model.add(Dropout(dropout))
    model.add(Dense(output_shape, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam')
    
    return model

def build_lstm(input_window_len, n_feature, output_shape, dropout=0.2, neurons_per_layer=None):
    
    model = Sequential()
    model.add(LSTM(input_window_len, input_shape=(input_window_len, n_feature), return_sequences=True))
    model.add(Dropout(dropout))
    model.add((LSTM(512, return_sequences=True)))
    model.add(Dropout(dropout))
    model.add((LSTM(512, return_sequences=True)))
    model.add(Dropout(dropout))
    model.add(Flatten())
    model.add(Dense(output_shape, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics = ['accuracy'])
    
    return model