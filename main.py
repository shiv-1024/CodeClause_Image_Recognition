import tensorflow as tf
from tensorflow.keras import datasets, layers, models # type: ignore
import numpy as np

(x_train,y_train),(x_test,y_test) = datasets.cifar10.load_data()

y_test = y_test.reshape(-1,)
y_train = y_train.reshape(-1,)

x_train = x_train/255
x_test = x_test/255

#CNN Model
cnn = models.Sequential([
    layers.Conv2D(64, (3,3), activation='relu', input_shape=(32,32,3)), 
    layers.MaxPooling2D(2,2),

    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(256, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(256, activation='relu'), 
    layers.Dropout(0.5), 
    layers.Dense(10, activation='softmax')
])


cnn.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

cnn.fit(x_train,y_train,epochs=25)

cnn.save('cifar10_trained.h5')