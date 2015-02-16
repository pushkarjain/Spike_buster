import matplotlib.pyplot as plt

def plot_comparison(original, filtered, filter_name):
    """ Compare the *original* and *filtered* image using the title *filter_name*"""
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4))
    ax1.imshow(original)
    ax1.set_title('Baseline image')
    ax1.axis('off')
    ax2.imshow(filtered)
    ax2.set_title(filter_name)
    ax2.axis('off')
    return fig
