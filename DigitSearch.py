#LIBRARIES
import tensorflow as tf
import keras
from keras.datasets import mnist
import matplotlib.pyplot as plt

#SPLIT DATASET

(train_data,train_labels),(test_data,test_labels)= mnist.load_data()
num_classes=10

train_data=train_data.reshape(train_data.shape[0],28,28,1)
train_labels=keras.utils.to_categorical(train_labels,num_classes)
train_data=train_data.astype("float32")
train_data/=255.0


test_data=test_data.reshape(test_data.shape[0],28,28,1)
test_labels=keras.utils.to_categorical(test_labels,num_classes)
test_data=test_data.astype("float32")
test_data/=255.0

#MODEL

model=tf.keras.Sequential([
                            tf.keras.layers.Conv2D(32, kernel_size=(3,3), activation="relu", input_shape=(28,28,1)),
                            tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
                            tf.keras.layers.MaxPooling2D((2,2)),
                            tf.keras.layers.Dropout(0.25),
                            tf.keras.layers.Flatten(),
                            tf.keras.layers.Dense(256, activation="relu"),
                            tf.keras.layers.Dropout(0.5),
                            tf.keras.layers.Dense(num_classes, activation="softmax")
])

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=["accuracy"])

model.summary()

history=model.fit(train_data,train_labels, batch_size=128, epochs=15, validation_data=(test_data,test_labels))

model.save("model_digit.h5")

#EVALUATE MODEL

acc=history.history["accuracy"]
val_acc=history.history["val_accuracy"]

loss=history.history["loss"]
val_loss=history.history["val_loss"]

epochs=range(len(acc))

plt.plot(epochs,acc,"r",label="Training Accuracy")
plt.plot(epochs,val_acc,"b",label="Validation Accuracy")

plt.title("Accuracy")

plt.legend(loc=0)
plt.figure()
plt.show()

