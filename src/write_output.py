#def write_output(noisy_image, noisy_image_scaled, percentile_result, sun_spikes_removed,sun_spikes_removed_original_scale):
def write_output(Screen_Out, *args):
    """Write the arguments arrays to the file outdata.txt"""
    if Screen_Out:
        for j in args:
            print j
    else:
        with open("../Output/outdata.txt", "w+") as f1:
            for i in args:
                f1.write(i)
