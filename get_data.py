import numpy as np
from scipy import ndimage

nbr_images = 15747


def load_image(id):
    url = "../../datasets/cats/"+str(id)+".jpg"
    image = ndimage.imread(url, True)
    print(image)

load_image(nbr_images)