from keras.models import Model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import matplotlib.pyplot as plt

def architecture(model):
    layers_info = {}
    for i in model.layers:
        layers_info[i.name] = i.get_config()

    #here the layer_weights dictionary will map every layer_name to its corresponding weights
    layer_weights = {}
    for i in model.layers:
        layer_weights[i.name] = i.get_weights()

    print(layers_info['max_pooling2d'])
    layers = model.layers

    filters, biases = model.layers[0].get_weights()
    print(layers[4].name, filters.shape)
    print(filters.shape)

    
    conv_layer_index = [0, 2, 4]
    outputs = [model.layers[i].output for i in conv_layer_index]
    model_short = Model(inputs=model.inputs, outputs=outputs)
    print(model_short.summary())

    img = load_img(r'F:\CleanDataSplit\train\Anomaly\chairanomalyframes_007.jpg', target_size = (256,256))
    img = img_to_array(img)
    img = np.expand_dims(img, axis = 0)

    feature_output = model_short.predict(img)

    columns = 8
    rows = 4
    for ftr in feature_output:
        #pos = 1
        fig=plt.figure(figsize=(12, 12))
        for i in range(1, columns*rows +1):
            fig =plt.subplot(rows, columns, i)
            fig.set_xticks([])  #Turn off axis
            fig.set_yticks([])
            plt.imshow(ftr[0, :, :, i-1], cmap='gray')
            #pos += 1
        plt.show()