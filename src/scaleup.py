import numpy as np
def scale_up(original, image):
    #scaled_back_image = (np.max(original) - np.min(original))*(image + 1.0)/2.0 + np.min(original)
    scaled_back_image = (np.max(original) - np.min(original))*(image +
            np.min(image))/(np.max(image)-np.min(image)) + np.min(original)
    return scaled_back_image
