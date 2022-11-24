import numpy as np

# Simple 1D array
A = np.array([1,2,3,4])

# Print info
print('A: ', A) # A:  [1 2 3 4]
print('A dimention: ', np.ndim(A)) # A dimention:  1
print('A shape: ', np.shape(A)) # A shape:  (4,) <- Always comes out as Tuple!!

# Simple 2D array
B = np.array([[1,2],[3,4],[5,6]])

# Print info
print('B: ', B) #B:  [[1 2]
                #     [3 4]
                #     [5 6]]
print('B dimention: ', np.ndim(B)) # B dimention:  2
print('B shape: ', np.shape(B)) # B shape:  (3, 2) <- Always comes out as Tuple!!

# Multiply 2D array
A = np.array([[1,2],[3,4]])
B = np.array([[4,5],[6,7]])
result = np.dot(A,B) # Using np.dot() to multiply two array
print('A x B = \n',result)
# [[16 19]
#  [36 43]]

# Result could be changed by putting the value with different order
result = np.dot(B,A)
print('B x A = \n',result)
#  [[19 28]    <--- Value changes because of multiplying 2D array with different order
#  [27 40]]

# 2X3 * 3X2 array
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2],[3,4],[5,6]])
print('A-shape: ', np.shape(A)) # 2X3
print('B-shape: ', np.shape(B)) # 3X2
print('A x B= \n', np.dot(A,B))  
#  [[22 28]
#  [49 64]]
#  1번째 차원의 열 수(A=3) 와 2번째 차원의 행 수(B=3) 가 같아야함

