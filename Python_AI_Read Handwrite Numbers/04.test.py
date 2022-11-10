import numpy as np

# To practice and test np.argmax() function

x1 = np.array([
                [0.1,0.8,0.1],
                [0.3,0.1,0.6],
                [0.2,0.5,0.3],
                [0.8,0.1,0.1]
                ])

y1 = np.argmax(x1,axis=0)
print('axis=0 value:\n',y1) # [3 0 1]

y2 = np.argmax(x1,axis=1)
print('\naxis=1 value:\n',y2) # [1 2 1 0]



x2 = np.array([
               [[1,5,1],
                [5,1,1],
                [1,1,5]],
               [[5,1,1],
                [1,2,3],
                [7,3,2]],
               [[9,8,1],
                [2,3,5],
                [8,6,3]]
               ])

# print(x2.shape) (3,3,3)
y3 = np.argmax(x2,axis=0)
print('\naxis=0 value:\n',y3)
#  [[2 2 0]
#  [0 2 2]
#  [2 2 0]]

y4 = np.argmax(x2,axis=1)
print('\naxis=1 value:\n',y4) 
#  [[1 0 2]
#  [2 2 1]
#  [0 0 1]]

'''
From the Practice,
np.argmax(#, axis=0) returns!!!
---np.array에서 []끼리 비교해서 최대값 index---

np.argmax(#, axis=1) returns!!!
---np.array에서 []안의 최대값 index 

'''

y = np.array([1,2,1,0])
t = np.array([1,2,0,0])
print(y==t) # [ True  True False  True]

print(np.sum(y==t)) # 3