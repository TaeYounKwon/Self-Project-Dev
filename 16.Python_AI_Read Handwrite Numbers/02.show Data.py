import sys, os
import numpy as np

sys.path.append(os.pardir)

from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# flatten=True => save the data as 1D np.array type
# To show the original Image, requires to change the 1D np.array => 28x28 size by using 'reshape()'    
(x_train, t_train),(x_test, t_test) = load_mnist(flatten=True, normalize=False) 

img = x_train[0]
label = t_train[0]
print(label) # 5

print(img.shape) # (784,)
img = img.reshape(28,28) # change the array to the original 28x28 shape
print(img.shape) # (28,28)

img_show(img)