import numpy as np
import matplotlib.pyplot as plt


def AND(x1, x2):
    x= np.array([x1,x2]) # input
    w = np.array([0.5,0.5]) # weight
    b = -0.7 # bias

    tmp = np.sum(x*w)+b
    if tmp <=0:
        return 0
    else:
        return 1

# Everything same as AND gate, except 'w' & 'b'
def NAND(x1,x2):
    x= np.array([x1,x2]) # input
    w = np.array([-0.5,-0.5]) # - AND gate weight
    b = 0.7 # - AND gate bias

    tmp = np.sum(x*w)+b
    if tmp <=0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x= np.array([x1,x2]) # input
    w = np.array([0.5,0.5]) # - AND gate weight
    b = -0.4 # - AND gate bias

    tmp = np.sum(x*w)+b
    if tmp <=0:
        return 0
    else:
        return 1
    
def XOR(x1,x2):
    s1 = NAND(x1,x2) # value of NAND GATE
    s2 = OR(x1,x2) # value of OR GATE
    result = AND(s1,s2) # ADD values into AND gate for XOR result
    return result    
    
# OUTPUT AND GATE    
print('AND GATE: ')
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))    

    
# OUTPUT NAND GATE
print('NAND GATE: ')    
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))    

# OUTPUT OR GATE
print('OR GATE: ')
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1)) 

# OUTPUT OR GATE
print('XOR GATE: ')
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1)) 


# Divide the graph Using SubPlot
sub_plots = plt.subplots(2, 2)
fig = sub_plots[0]
graph = sub_plots[1]

# 01. And Gate
x1 = np.arange(-2,2,0.01)
x2 = np.arange(-2,2,0.01)
b = -0.7 # bias
w = 0.5 # weight
y = (-w * x1 - b)/w


# Draw at the top-left
graph[0][0].plot(x1,y,'r--')
graph[0][0].set_xlim(-0.5,1.5)
graph[0][0].set_ylim(-0.5,1.5)
graph[0][0].grid()
graph[0][0].set_title('AND GATE')
graph[0][0].scatter(0,0, color='orange',marker='o',s=150)
graph[0][0].scatter(0,1, color='orange',marker='o',s=150)
graph[0][0].scatter(1,0, color='orange',marker='o',s=150)
graph[0][0].scatter(1,1, color='red',marker='^',s=150)

# 02. NAND Gate
x1 = np.arange(-2,2,0.01)
x2 = np.arange(-2,2,0.01)
b = 0.7 # bias
w = -0.5 # weight
y = (-w * x1 - b)/w
# Draw at the top-left
graph[0][1].plot(x1,y,'r--')
graph[0][1].set_xlim(-0.5,1.5)
graph[0][1].set_ylim(-0.5,1.5)
graph[0][1].grid()
graph[0][1].set_title('NAND GATE')
graph[0][1].scatter(0,0, color='red',marker='^',s=150)
graph[0][1].scatter(0,1, color='red',marker='^',s=150)
graph[0][1].scatter(1,0, color='red',marker='^',s=150)
graph[0][1].scatter(1,1, color='orange',marker='o',s=150)

# 03. OR Gate
x1 = np.arange(-2,2,0.01)
x2 = np.arange(-2,2,0.01)
b = 0.4 # bias
w = -0.5 # weight
y = (-w * x1 - b)/w
# Draw at the top-left
graph[1][0].plot(x1,y,'r--')
graph[1][0].set_xlim(-0.5,1.5)
graph[1][0].set_ylim(-0.5,1.5)
graph[1][0].grid()
graph[1][0].set_title('OR GATE')
graph[1][0].scatter(0,0, color='orange',marker='o',s=150)
graph[1][0].scatter(0,1, color='red',marker='^',s=150)
graph[1][0].scatter(1,0, color='red',marker='^',s=150)
graph[1][0].scatter(1,1, color='red',marker='^',s=150)

fig.suptitle('Multiple Gates')
fig.tight_layout(pad=2)
plt.savefig('Multiple Gates.png')
plt.show()