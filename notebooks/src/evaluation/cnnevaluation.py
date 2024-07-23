from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
from sklearn.preprocessing import LabelEncoder
import pickle
import os
def cnnevaluation(model, X_test, y_test):
    # precision = Precision()
    # recall = Recall()
    # accuracy = BinaryAccuracy()

    loss, accuracy = model.evaluate(X_test, y_test)
    
    print(f"Loss: {loss}")
    print(f"Accuracy: {accuracy}")

    
    
    
    # precision.update_state(prediction, y_test)
    # recall.update_state(prediction, y_test)
    # accuracy.update_state(prediction, y_test)

    # print(f'Precision:{precision.result()}')
    # print(f' Recall:{recall.result()}')
    # print(f'Accuracy:{accuracy.result()}')