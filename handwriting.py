import gzip
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

import tensorflow as tf
from keras.callbacks import EarlyStopping
from keras.layers import Dense
from keras.models import Sequential
from keras.utils.np_utils import to_categorical

#Loading training data

f = gzip.open('data/train-images-idx3-ubyte.gz','r')

image_size = 28
num_images = 60000

header=f.read(16)
buf = f.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = np.asarray(data.reshape(num_images, image_size, image_size, 1))
x_train = np.asarray(data.reshape(num_images, image_size*image_size)) / 255

#Loading training labels

f = gzip.open('data/train-labels-idx1-ubyte.gz','r')
f.read(8)
   
buf = f.read(num_images)
labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64) 
labels = np.asarray(labels.reshape(num_images, 1))
y_train_categorical = to_categorical(labels)

#Creating model

early_stopping_monitor = EarlyStopping(patience=3)
input_shape = image_size * image_size
    
model = Sequential()
model.add(Dense(150, activation='relu', input_shape = (input_shape,)))
model.add(Dense(150, activation='relu'))
model.add(Dense(150, activation='relu'))
model.add(Dense(10, activation='softmax'))

#Compiling and fitting model
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics=['accuracy',tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])
final = model.fit(x_train, y_train_categorical,epochs=20,callbacks = [early_stopping_monitor],validation_split= 0.3)

#Loading testing data

f = gzip.open('data/t10k-images-idx3-ubyte.gz','r')
num_images = 10000

header = f.read(16)
buf = f.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = np.asarray(data.reshape(num_images, image_size, image_size, 1))
x_test = np.asarray(data.reshape(num_images, image_size*image_size)) / 255

#Plotting for control 

#image = np.asarray(data[151]).squeeze()
#plt.imshow(image)
#plt.show()

#Loading testing labels

f = gzip.open('data/t10k-labels-idx1-ubyte.gz','r')
f.read(8)

buf = f.read(10000)
labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64) 
labels = np.asarray(labels.reshape(10000, 1))
y_test_categorical = to_categorical(labels)

#Evaluating model and printing stats
results = model.evaluate(x_test, y_test_categorical)
stats = dict(zip(final.history.keys(), results))
print(stats)

#Predicting with test data 
predictions = model.predict(x_test)

b = np.zeros_like(predictions)
b[np.arange(len(predictions)), predictions.argmax(1)] = 1
y_results = np.argmax(predictions, axis=-1)

#Exporting results to a spreadsheet for control

header = ['Real','Pred']
df = pd.DataFrame(data=np.column_stack((labels[:,0],y_results)), columns=header)
df.to_excel('control.xlsx')