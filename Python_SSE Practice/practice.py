import numpy as np

def sum_squres_error(y,t):
    return 0.5*np.sum((y-t)**2)

# EX-1
# SoftMax function output values
# Predict that '2nd Value' has highest possibility
y= [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]

# Correct Answer Label
# only one '1' -> correct answer
# other wrong answers -> '0'
# called "One Hot Encoding"
t=[0,0,1,0,0,0,0,0,0,0]
SSE_Result = sum_squres_error(np.array(y),np.array(t))
print(SSE_Result)


# EX-2
# Predict that '7th' value has the hihest possibility
y=[0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
SSE_Result = sum_squres_error(np.array(y),np.array(t))
print(SSE_Result)