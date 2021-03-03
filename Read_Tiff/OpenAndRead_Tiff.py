#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:56:08 2021

@author: dp
"""

from osgeo import gdal

def getGeoTiffasArray(path_to_tiff):
    dataset = gdal.Open(path_to_tiff)
    image = dataset.ReadAsArray()
    return image

def openWithGdal(path_to_tiff):
    data_set = gdal.Open(path_to_tiff)
    return data_set

def readBands(path_to_tiff):
    files = [1,2,3]
    mylist = []
    for file in files:
        f = path_to_tiff + '/BAND%d'%file + '.tif'
        arr = getGeoTiffasArray(f)
        mylist.append((arr))
    return mylist

