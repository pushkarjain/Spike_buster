import matplotlib.pyplot as plt
from pyplot.plot_comparison import plot_comparison

def plot_output(noisy_image, percentile_result, sun_spikes_removed, sun_spikes_removed_original_scale):
    """Consolidated plot output"""
    
    final_plot1 = plot_comparison(percentile_result, sun_spikes_removed, 'Removed sun spikes with scaled down')
    #final_plot = plot_comparison(noisy_image, sun_spikes_removed_original_scale, 'Removed sunspikes with original scale')
    #final_plot.savefig("../Output/No_spikes_unscaled.png")
    final_plot1.savefig("../Output/No_spikes_scaled.png")
    plt.show()
