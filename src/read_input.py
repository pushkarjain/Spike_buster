from osgeo import gdal
def read_input(infile):
    """Read input file. Exit status if unable to find/open the file."""
    gdal.UseExceptions()
    try:
        ds = gdal.Open(infile)
    except RuntimeError, e:
        print "Unable to open tiff file"
        print e
        sys.exit(1)
    return ds
