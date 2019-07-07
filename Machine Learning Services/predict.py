import numpy as np
import json
from keras.models import load_model
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('fashion-mnist-model')
    model = load_model('fashion-mnist-model.h5')

def run(raw_data):
    data = np.array(json.loads(raw_data)['data'])