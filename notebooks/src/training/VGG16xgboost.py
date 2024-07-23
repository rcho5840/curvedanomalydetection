from keras.applications.vgg16 import VGG16
from sklearn import metrics
from sklearn import preprocessing
import pickle
def VGG16xgboost(X_train, y_train, X_test, y_test):
    VGG_model = VGG16(weights = 'imagenet', include_top = False, input_shape = (256,256,3))
    
    for layer in VGG_model.layers:
        layer.trainable = False
    
    VGG_model.summary()

    X_features_for_training = VGG_model.predict(X_train)
    X_features_for_training = X_features_for_training.reshape(X_features_for_training.shape[0], - 1)

    import xgboost as xgb
    xgb_model = xgb.XGBClassifier()
    xgb_model.fit(X_features_for_training, y_train)
    
    X_features_for_testing = VGG_model.predict(X_test)
    X_features_for_testing = X_features_for_testing.reshape(X_features_for_testing.shape[0],  -1)
    
    prediction = xgb_model.predict(X_features_for_testing)
    le = preprocessing.LabelEncoder()
    le.fit(y_test)
    prediction = le.inverse_transform(prediction)
    
    print("Accuracy = ", metrics.accuracy_score(y_test, prediction))
    
    with open ('C:/Users/randy/OneDrive/Desktop/CS/curvedanomalydetection/conf/VGG16xgboost', 'wb') as f:
        pickle.dump(xgb_model, f)
        
    return xgb_model
    
        


    