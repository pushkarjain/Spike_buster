from osgeo import gdal
from read_input import read_input

class GeoRead(object):
    def __init__(self, myfile):
        self.myfile = myfile
        self.ds = read_input(myfile)
        (self.X, self.deltaX, self.rotation, self.Y, self.rotation, self.deltaY) = self.ds.GetGeoTransform()
        
        self.arys = []
        for i in xrange(1, self.ds.RasterCount + 1):
            self.arys.append(self.ds.GetRasterBand(i).ReadAsArray())
        try:
            self.ary = self.ds.GetRasterBand(1).ReadAsArray()
        except RuntimeError, e:
            print "Band (%i) not found" %band_num
            print e
            sys.exit(1)
