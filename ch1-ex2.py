from PIL import Image
from pylab import *
from scipy.ndimage import filters





im = array(Image.open("imagen2.jpg").convert('L'), "f")

# Creando imagen blurred 
sigma = 3
blurred = filters.gaussian_filter(im,sigma)


weight = 0.25# escalar que multiplica a la imagen una vez blurred
unsharp = im - weight*blurred


# construyendo la imegen
figure()
imshow(im)
gray()
title("Imagen antes")

figure()
imshow(unsharp)
gray()
title("Imagen despues".format(weight))

show()