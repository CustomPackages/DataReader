#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:42:44 2021

@author: dp

"""
import OpenandRead
from osgeo import osr

'''

X,Y TO LATLON

'''

def TRANSFORM(folder):
    data = OpenandRead.openWithGdal(folder) 
    old_cs = osr.SpatialReference()
    old_cs.ImportFromWkt(data.GetProjectionRef())
    
    wgs84_wkt = '''
         GEOGCS["WGS 84",
            DATUM["WGS_1984",
                SPHEROID["WGS 84",6378137,298.257223563,
                    AUTHORITY["EPSG","7030"]],
                AUTHORITY["EPSG","6326"]],
            PRIMEM["Greenwich",0,
                AUTHORITY["EPSG","8901"]],
            UNIT["degree",0.0174532925199433,
                AUTHORITY["EPSG","9122"]],
            AUTHORITY["EPSG","4326"]] '''
    new_cs = osr.SpatialReference()
    new_cs.ImportFromWkt(wgs84_wkt)
    
    transform = osr.CreateCoordinateTransformation(old_cs, new_cs)
    return transform



def xC(folder, col,row):
    data = OpenandRead.openWithGdal(folder)
    geo_matrix = data.GetGeoTransform()
    xp = geo_matrix[1]*col + geo_matrix[2]*row + geo_matrix[1]*0.5 + geo_matrix[2]*0.5 + geo_matrix[0]
    return xp

def yC(folder, col,row):
    data = OpenandRead.openWithGdal(folder)
    geo_matrix = data.GetGeoTransform()
    yp = geo_matrix[4]*col + geo_matrix[5]*row + geo_matrix[4]*0.5 + geo_matrix[5]*0.5 + geo_matrix[3]
    return yp



def XYtoLATLONG(folder, col, row):
    x1 = xC(folder, col, row)
    y1 = yC(folder, col, row)
    transform = TRANSFORM(folder)
    latlong = transform.TransformPoint(x1, y1)
    lat = latlong[0]
    lon = latlong[1]
    final_latlong = (lat,lon)
    return final_latlong
