import numpy as np
import matplotlib.pyplot as plt

# x could be simple int, but cannot be np.array([1.0,2.0])
def step_function_V1(x):
    if x>0:
        return 1
    else:
        return 0
    
# now x could be anything    
def step_function_V2(x):    
    
    return np.array(x>0,dtype=np.int) 


def sigmoid(x):
    return 1/(1+np.exp(-x))


def ReLU(x):
    return np.maximum(0,x) # Use np.maximum to return the higher value than '0'

# Print Functions Outputs

# Step Function
print('Step Function_V1 result of "5": ',step_function_V1(5))
print('Step Function_V2 result of "5": ',step_function_V2(5))
# print('V1 result of "[1.0,3.3]": ',step_function_V1(np.arange(-1.0,3.3,0.1)))
# prints error
print('Step Function_V2 result of "[-1.0,3.3]": ',step_function_V2(np.arange(-1.0,3.3,0.1)))

# Sigmoid
print('Sigmoid Function result of "[-1.0,3.3]: ', sigmoid(np.arange(-1.0,3.3,0.1)))


# Divide the graph Using SubPlot
sub_plots = plt.subplots(2, 2)
fig = sub_plots[0]
graph = sub_plots[1]

# 01. Step Function
x = np.arange(-1.0,3.3,0.1)
y = step_function_V2(x)
graph[0][0].plot(x,y)
graph[0][0].set_title('Step Function')
graph[0][0].set_ylim(-0.1,1.1)

# 02. Sigmoid Function
x = np.arange(-1.0,3.3,0.1)
y = sigmoid(x)
graph[0][1].plot(x,y,color='orange')
graph[0][1].set_title('Sigmoid Function')
graph[0][1].set_ylim(-0.1,1.1)

# 03. Step VS Sigmoid
x = np.arange(-1.0,3.3,0.1)
y = step_function_V2(x)
graph[1][0].plot(x,y)
y = sigmoid(x)
graph[1][0].plot(x,y,color='orange')
graph[1][0].set_title('Step VS Sigmoid')

# 04. ReLu Function
x = np.arange(-1.0,3.3,0.1)
y = ReLU(x)
graph[1][1].plot(x,y)
graph[1][1].set_title('ReLU Function')
graph[1][1].set_ylim(-0.1,1.1)

fig.suptitle('Multiple Functions')
fig.tight_layout(pad=2)
plt.savefig('Multiple Functions.png')
plt.show()