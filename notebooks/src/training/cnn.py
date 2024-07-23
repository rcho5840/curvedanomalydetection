import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

def cnn(X_train, y_train, X_val, y_val, epochnumber):
    model = Sequential()
    model.add(Conv2D(32, (3,3), activation = 'relu', input_shape = (256,256,3)))
    model.add(MaxPooling2D((2,2)))
    model.add(Conv2D(64, (3,3), activation = 'relu'))
    model.add(MaxPooling2D((2,2)))
    model.add(Conv2D(64, (3,3), activation = 'relu'))
    model.add(Flatten())
    model.add(Dense(64, activation = 'relu'))
    model.add(Dense(1, activation = 'sigmoid'))

    model.compile(optimizer = 'adam', loss = tf.losses.BinaryCrossentropy(), metrics = ['accuracy'])
    model.summary()
        
    logdir = 'logs'
    callback = tf.keras.callbacks.TensorBoard(log_dir = logdir)
        
    hist = model.fit(X_train, y_train, epochs = epochnumber, validation_data = (X_val, y_val), callbacks = [callback])
    
    
    
    return hist, model

   