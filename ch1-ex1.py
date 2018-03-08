from PIL import Image
from numpy import *
import matplotlib.pyplot as plt
from scipy.ndimage import   filters
from pylab import *
im = array(Image.open('empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im,10)
im = array(Image.open('empire.jpg'))
im2 = zeros(im.shape)
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
    im2 = uint8(im2)
    im2 = array(im2,'uint8')
    plt.imshow(im2)
plt.axis('off')

#A medida que el sigma aumenta el nivel de emborronamiento es mayor

