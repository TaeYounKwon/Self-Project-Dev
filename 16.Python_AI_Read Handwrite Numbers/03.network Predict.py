import sys, os
import numpy as np
import pickle

sys.path.append(os.pardir)

from dataset.mnist import load_mnist
from PIL import Image

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c) # again, prevent overflow
    sum_exp_a = np.sum(exp_a)
    y= exp_a/sum_exp_a
    return y

def get_data():
    (x_train, t_train),(x_test, t_test) = \
        load_mnist(flatten=True, normalize=True, one_hot_label=False )
        # normalize=True => transfer 0~255 pixcel value to 0.0~1.0
        # Simply divide the pixcel value by '255'

    return x_test, t_test

def init_network():
    with open("./dataset/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1)+b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2)+b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3)+b3
    y=softmax(a3)
    
    return y

# Normalization&Pre Processing
x, t = get_data()
network = init_network()

# Check Accuracy
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p=np.argmax(y) # get the index of element that has the highest accuracy
    if p ==t[i]:
        accuracy_cnt +=1
        
print("Accuracy: "+str(float(accuracy_cnt)/len(x))) # Accuracy: 0.9352   

# Check Accuracy with Batch_size
x, t = get_data()
network = init_network()

# Check Accuracy with batch_size 
batch_size = 100 
accuracy_cnt = 0

# range(start, end-1, step)
# ex) list(range(0,10,3)) => [0,3,6,9]
for i in range(0,len(x),batch_size):
    x_batch = x[i:i+batch_size] # x[0:100],x[100:200] ...
    y_batch = predict(network, x_batch)
    
    # get the index of element that has the highest accuracy
    # axis=1 means getting it from 
    p = np.argmax(y_batch, axis=1) 
    accuracy_cnt += np.sum(p==t[i:i+batch_size])
    
print("Accuracy: "+str(float(accuracy_cnt)/len(x)))    


'''
From this Chapter!

Neuron network use sigmoid function
perceptron used step_function to calculate.
Learn more about these next chapter!!


'''
