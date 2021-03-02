import gdal 
import numpy as np

def readTif(filename):
  band=gdal.open(filename)
  band = band.ReadAsArray()
  band = np.array(band)
  return band
