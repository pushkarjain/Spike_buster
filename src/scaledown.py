import numpy as np

def scale_down(noisy_image, up_bound, low_bound):
    """ Scale down the values from *noisy_image* within the values bound by *up_bound* and *low_bound* """
    noisy_image_scaled = (up_bound-low_bound)/(np.max(noisy_image)-np.min(noisy_image))*(noisy_image - np.min(noisy_image)) - up_bound
    return noisy_image_scaled
