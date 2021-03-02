import gdal 
import numpy as np

def get_band_array(filename):
  band=gdal.open(filename)
  band = band.ReadAsArray()
  band = np.array(band)
  return band
