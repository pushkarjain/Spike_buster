import numpy as np
def scale_up(original, image):
    """ Scale the array values from **image** to **original** """
    scaled_back_image = (np.max(original) - np.min(original))*(image +
            np.min(image))/(np.max(image)-np.min(image)) + np.min(original)
    return scaled_back_image
