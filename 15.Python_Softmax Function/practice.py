import numpy as np


# Simple Soft Max function
# Problem! --- OVERFLOW ---
# if a value is large number, exp_a will be a huge number, 
# and computer will not be able to handle those number 
# if 'a' = [990,995,1000], the return y=[[nan, nan, nan]]
def softmax_v1(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

# Soft Max function (prevent overflow version)
def softmax_v2(a):
    c = np.max(a) # max number of 'a', ex) 1000 if a = [990,995,1000]
    exp_a = np.exp(a-c) # now a = [-10,-5,0] 
    sum_exp_a = np.sum(exp_a)
    y=exp_a/sum_exp_a
    
    return y

# Test softmax v1 & v2
a = np.array([990,995,1000])
result1 = softmax_v1(a)
result2 = softmax_v2(a)

# Check result
print('Result_1: ',result1) #Result_1:  [nan nan nan]
print('Result_2:',result2 ) #Result_2: [4.50940412e-05 6.69254912e-03 9.93262357e-01]
print('Sum of Result_2: ',np.sum(result2)) # Sum of the SoftMax Function results is always '1' 
