#LIBRARIES
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


#FUNCIONS
#Plot_i plots image, accuracy percentage, 
#class of the image and class predicted
#Plot_v shows prediction on a graph, 
#pink for correct answer, purple for mistakes, and gray for dismissed predictions

def plot_i(i,p_array,true_label,im):
    p_array,true_label,im=p_array,true_label[i],im[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(im,cmap=plt.cm.binary)
    predict=np.argmax(p_array)
    if predict==true_label:
        color='black'
    else:
        color='black'
    plt.xlabel('{} {:2.0f}% ({})'. format(class_names[predict],
                                     100*np.max(p_array),
                                     class_names[true_label]),
                                     color=color)
def plot_v(i,p_array,true_label):
    p_array,true_label=p_array,true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot=plt.bar(range(10),p_array,color='#777777')
    plt.ylim([0,1])
    predicted=np.argmax(p_array)

    thisplot[predicted].set_color('purple')
    thisplot[true_label].set_color('pink')


#DATA SET
#This dataset was provided by TensorFlow
#It contains clothes images for classification, (28,28)
#10 classes

fashion_mnist=keras.datasets.fashion_mnist
(train_data,train_lables),(data,labels)=fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#DATA PRE-PROCESE AND FORMATING (SHOW IMAGES)
#Convert images values from [0,255] to [0,1]
#Plots 25 examples of the prepared images

train_data=train_data/255.0
data=data/255

plt.figure(figsize=(15,15))
for i in range (25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_data[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[train_lables[i]])
plt.show()

#CALLBACK
#Stops model when chosen accuracy is reached

class CallBack(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get("accuracy") is not None and logs.get("accuracy") >0.97:
            self.model.stop_training=True

#CONFIGURE MODEL (NEURONAL NETWORK LAYERS)
#Softmax activation chooses highest value from the classes, most likely prediction

modelo=keras.Sequential([keras.layers.Flatten(input_shape=(28,28)),
                        keras.layers.Dense(128, activation='relu'),
                        keras.layers.Dense(10,activation='softmax')])

#COMPILE METRICS, OPTIMIZER AND LOSS           
#Sparse_Categorical_Crossentropy, as the model has more than 2 possible outcomes

modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

#TRAIN MODEL
#Callback must be declared when training model

Callback=CallBack()
modelo.fit(train_data,train_lables,epochs=30,callbacks=[Callback])

#EVALUATE
t_loss,t_acc=modelo.evaluate(data,labels,verbose=2)
print('Test Accuracy: ', t_acc)

#PREDICTIONS
#Written outcome of a prediction
predictions=modelo.predict(data)
predictions[0]


#SHOWING PREDICTIONS
#Plots 36 images with the prediction graph, class name, and prediction name

rows=6
col=6
num_pics=rows*col

plt.figure(figsize=(2*2*col,2*rows))
for i in range (num_pics):
    plt.subplot(rows,2*col,2*i+1)
    plot_i(i,predictions[i],labels,data)
    plt.subplot(rows,2*col,2*i+2)
    plot_v(i,predictions[i],labels)
plt.tight_layout()
plt.show()


