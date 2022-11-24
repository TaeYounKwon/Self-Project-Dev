import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('mycat.jpg')
plt.imshow(img)
plt.show()