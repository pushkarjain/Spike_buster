"""
Spike-buster : Despiking reflectivity data

Usage:
    pymain.py IN_FILE

Arguments:
    IN_FILE    :       Input GeoTIFF file path

Options:
    -h         :       Show help
"""
from docopt import docopt
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
from skimage.filter import rank
from skimage.morphology import erosion, disk

from georead import GeoRead
from pyplot.plot_comparison import plot_comparison
from pyplot.plot_output import plot_output
from read_input import read_input
from scaledown import scale_down
from scaleup import scale_up
from write_output import write_output

def main(arguments):
    #Read input GeoTIFF file
    in_data = GeoRead(arguments['IN_FILE'])

    #--------------------------------------------------------------#
    # Alogirtihm
    # Read image -> Scale down to [-1,1] -> Mean_percentile -> 
    #Erosion -> Scale up new image upto original maxima and minima
    #--------------------------------------------------------------#

    # Consider the sun spikes as noise
    print "Reading input GeoTIFF file..."
    noisy_image = in_data.arys[0]
    print "The maxima is %f & the minima is %f.\n" %(np.max(noisy_image), np.min(noisy_image))

    # Scale array data to [-1,1] so that mean_percentile can implemented
    print "Scaling input data to [-1,1]..."
    noisy_image_scaled = scale_down(noisy_image, 1.0, -1.0)
    print "Done construction of scaled noisy_image.\n"

    #Disk size for implementing mean percentile
    #selem = disk(5) #Not good
    #selem = disk(10) #Can be better
    selem = disk(15)
    #selem = disk(20) #Not good

    #Applying mean percentile
    print "Applying Mean percentile with p0 = 0.1 & p1 = 0.9..."
    percentile_result = rank.mean_percentile(noisy_image_scaled, selem=selem, p0=.1, p1=.9)
    print "Done construction of percentile_result.\n"

    #Applying erosion. 
    print "Applying erosion to remove the sun spikes..."
    sun_spikes_removed = erosion(percentile_result, selem)
    print "Done construction of sun spikes removed scaled down result.\n"

    #Scaling the final result to original scale
    print "Scaling the final output to maxima and minima of original image..."
    sun_spikes_removed_original_scale = scale_up(noisy_image, sun_spikes_removed)
    print "Process completed.\n"


    # Writing Output
    Screen_out = False
    print "Screen_output is %r." %(Screen_out)
    write_output(Screen_out, noisy_image, noisy_image_scaled, percentile_result, sun_spikes_removed, sun_spikes_removed_original_scale)

    #Plot data
    print "Generating plots..."
    plot_output(noisy_image, percentile_result, sun_spikes_removed, sun_spikes_removed_original_scale)

    print "Script completed successfully."

if __name__ == '__main__':
    arguments = docopt(__doc__, version = '1.0.0')
    print arguments

    main(arguments)
