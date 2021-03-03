#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:09:59 2021

@author: dp
"""


import argparse

parser = argparse.ArgumentParser(
        description = "Getting folders where data is present and where to store it"
)

parser.add_argument("-a", "--folder0", required = True, help = "path to file where all the Band images are located")
parser.add_argument("-b", "--folder1", required = True, help = "path to  path to any Band image: ")
parser.add_argument("-c", "--folder2", required = True, help = "path to map image: ")
parser.add_argument("-d", "--folder3", required = True, help = "path to folder where you want to save the RGB Band chips: ")
parser.add_argument("-e", "--folder4", required = True, help = "Path to folder where you want to save the Map chips: ")
parser.add_argument("-f", "--folder5", required = True, help = "path to folder where you want to save the RGB Band chip numpy files: ")

args = vars(parser.parse_args())

#print(args['folder0'] + '   ' + args['folder5'] + '   ' + args['folder2'] + '   ' + args['folder3'] + '   ' + args['folder4'] + '   ' + args['folder1'])
#UserInput.args['folder4'] + str(counter) + '.png', C)