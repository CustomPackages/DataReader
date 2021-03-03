#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:42:43 2021

@author: dp
"""
import OpenandRead
from osgeo import ogr, osr

'''

LAT LONG TO X,Y

'''

def world_to_pixel(folder, geo_matrix, x, y):
    data = OpenandRead.openWithGdal(folder)
    geo_matrix = data.GetGeoTransform()
    ul_x = geo_matrix[0]
    ul_y = geo_matrix[3]
    x_dist = geo_matrix[1]
    y_dist = geo_matrix[5]
    pixel = int((x - ul_x)/x_dist)
    line = -int((ul_y - y)/y_dist)
    return pixel, line


def LATLONG_TO_XY(folder, lat, long):
    data = OpenandRead.openWithGdal(folder)
    target = osr.SpatialReference(wkt=data.GetProjection())
    source = osr.SpatialReference()
    source.ImportFromEPSG(4326)
    transform = osr.CreateCoordinateTransformation(source, target)
    
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(lat, long)
    point.Transform(transform)
    
    x, y = world_to_pixel(folder, data.GetGeoTransform(), point.GetX(), point.GetY())
    list1 = [x, y]
    return list1