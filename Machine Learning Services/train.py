from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Conv2D, Dense, Flatten, Activation
import numpy as np
import keras

#
# Parse input parameters
#
parser = argparse.ArgumentParser()
parser.add_argument('--epochs', type=int, dest='epochs', help='Number of epochs')
args = parser.parse_args()

epochs = args.epochs

#
# Load data
#

(x_train_orig, y_train_orig), (x_test_orig, y_test_orig) = fashion_mnist.load_data()

#
# Pre-process data
#

img_rows = 28
img_cols = 28
num_classes = 10

# Add missing channel dimension
x_train = x_train_orig.reshape(x_train_orig.shape[0], img_rows, img_cols, 1)
x_test = x_test_orig.reshape(x_test_orig.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

y_train = keras.utils.to_categorical(y_train_orig, num_classes)
y_test = keras.utils.to_categorical(y_test_orig, num_classes)

mask_train = np.random.binomial(1, .05, y_train.shape[0]).astype('bool')
mask_test = np.random.binomial(1, .1, y_test.shape[0]).astype('bool')

x_train = x_train[mask_train]
x_test = x_test[mask_test]

y_train = y_train[mask_train]
y_test = y_test[mask_test]

print('Number of training images: {}'.format(x_train.shape[0]))
print('Number of test images:     {}'.format(x_test.shape[0]))

#
# Define model
#

model = Sequential();
model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=input_shape))
model.add(Conv2D(64, (3, 3), strides=2, padding='same', activation='relu'))
model.add(Conv2D(128, (3, 3), strides=2, padding='same', activation='relu'))
model.add(Flatten())
model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

model.summary()

#
# Train model
#

batch_size = 32

train_hist = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_test, y_test))

#
# Save model
#
model.save('outputs/model.h5')
