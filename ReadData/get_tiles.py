import cv2
import numpy as np

def save_npy(tiles,filename,string):
    i=0 # defining just for count
    for j in range(0,len(tiles)):
        a= tiles[j]
        np.save(filename + string+'__{0:05d}'.format(i), a)
        i += 1
       
# saving files  as .png: both image and masks  
def save_png(tiles,filename,string):
    i=0 # defining just for count
    for j in range(0,len(tiles)):
        a= tiles[j]
        a= a.astype(np.uint8)
        cv2.imwrite(filename + string+ '__{0:05d}.png'.format(i), a)
        i += 1
       
# here in both cases filename is the the name of the directory where you want to save and
# string is the name of the files at which name you want to save

def get_tiles(data,M,N,filename,string):
    tiles = list()

    for i in range(0,data.shape[0],M):
        for j in range(0,data.shape[1],N):
            start_y = i
            start_x = j
       
            if (start_y + M >= data.shape[0]):
                start_y = start_y - (start_y + M - data.shape[0])
           
            if (start_x + N >= data.shape[1]):
                start_x = start_x - (start_x + N - data.shape[1])
           
            data_tile = data[start_y:start_y+M,start_x:start_x+N] #get the tile
           
            tiles.append(data_tile) # getting all the tiles
   
    # changing datatype uint to float
   
    for i in range(len(tiles)):
        tiles[i]= np.float32(tiles[i])
   
    return tiles
