#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:54:58 2021

@author: spaul
"""
import numpy as np
from PIL import Image
import glob
from ReadData import ReadData
#%%
def normalize_image(filename):
    """
    Args:
        image : a string of name of image file for jpg and png and
                for tif files considering its saved npy version and
                normalilizing wrt no. of bits representing each pixel
    Return:
        image_asarray : numpy array of the image
                        that is normalized by being divided by 255
    """
    data = ReadData(filename)
    if data.max != 0:
        norm_data = data/data.max()
    else:
        norm_data[data == 0] = 0
   
    return norm_data

#%%
def find_mean(image_path):
    """
    Args:
        image_path : pathway of all images
    Return :
        mean : mean value of all the images
    """
    all_images = glob.glob(image_path)
    num_images = len(all_images)
    mean_sum = 0

    for image in all_images:
        img_asarray = ReadData(image)
        individual_mean = np.mean(img_asarray)
        mean_sum += individual_mean
       

    # Divide the sum of all values by the number of images present
    mean = mean_sum / num_images

    return mean

#%%
def find_stdev(image_path):
    """
    Args:
        image_path : pathway of all images
    Return :
        stdev : standard deviation of all pixels
    """
    # Initiation
    all_images = glob.glob(image_path)
    num_images = len(all_images)

    # Recall mean value from function above: def Mean(path)
    mean_value = find_mean(image_path)
    std_sum = 0

    for image in all_images:
        img_asarray = ReadData(image)
        individual_stdev = np.std(img_asarray)
        std_sum += individual_stdev

    std = std_sum / num_images

    return std

#%% Gaussian Normalize
def Gaussian_normalize(image_path):
    std = find_stdev(image_path)
    mean = find_mean(image_path)
   
    all_images = glob.glob(image_path)
    data = []
    for image in all_images:
        img_asarray = ReadData(image)
        norm_data = (img_asarray-mean)/std
        data.append(norm_data)
    return data    
