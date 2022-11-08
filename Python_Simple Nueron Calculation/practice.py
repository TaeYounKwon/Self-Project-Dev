import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

# Simple Perceptron calculation
X = np.array([1,2]) # shape = (2,)
W = np.array([[1,3,5],[2,4,6]]) # shape = (2,3)
Y = np.dot(X,W)
print(Y) # [ 5 11 17]

# Simple Perceptron Calculation (+ bias)
X = np.array([1.0,0.5]) # (2,)
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) # (2,3)
B1 = np.array([0.1,0.2,0.3]) # (3,)

A1 = np.dot(X,W1) + B1
print(A1) # [0.3 0.7 1.1]

Z1 = sigmoid(A1)
print(Z1) # [0.57444252 0.66818777 0.75026011]