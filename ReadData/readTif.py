import gdal 
import numpy as np

def ReadTif(filename):
  band=gdal.Open(filename)
  band = band.ReadAsArray()
  band = np.array(band)
  return band
