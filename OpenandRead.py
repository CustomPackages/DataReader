#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:56:08 2021

@author: dp
"""

from osgeo import gdal

def getGeoTiffasArray(folder):
    dataset = gdal.Open(folder)
    image = dataset.ReadAsArray()
    return image

def openWithGdal(folder):
    data_set = gdal.Open(folder)
    return data_set

def readBands(folder):
    # '/huser/users/trainee/vihan/Ahmedabad/AHM_BAND/16334311-518-1-5-X-STUC00OTD-_hrdpd_Sarkhej_India_'
    files = [1,2,3]
    mylist = []
    for file in files:
        f = folder + '/BAND%d'%file + '.tif'
        arr = getGeoTiffasArray(f)
        mylist.append((arr))
    return mylist
