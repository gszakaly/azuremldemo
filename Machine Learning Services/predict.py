import sys
import json
import numpy as np
from keras.models import load_model
from azureml.core.model import Model
import keras
import tensorflow as tf

labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def init():
    print('Python version: {}'.format(sys.version))
    print('Keras version: {}'.format(keras.__version__))
    print('Tensorflow version: {}'.format(tf.__version__))

    global model
    model_path = Model.get_model_path('fashion-mnist-model')
    model = load_model(model_path)

def run(raw_data):
    img = np.asarray(json.loads(raw_data)['data']).reshape(28,28)
    input = img.reshape(1, 28, 28, 1)
    pred = model.predict(input).argmax()
    return {'category': int(pred), 'label': labels[pred]}
