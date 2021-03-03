#from osgeo import gdal, ogr, osr
#import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image
import LtoP
import PtoL
import OpenandRead
import UserInput


'''

CROP IMAGE

'''

def saveCrop(): 

    mylist = OpenandRead.readBands(UserInput.args['folder0'])
    counter = 0
    C = np.zeros((256,256,3), np.float32)
    #bands being fetched from mylist (from OpenandRead python file)
    band1 = mylist[0]
    band2 = mylist[1]
    band3 = mylist[2]
    ##newlist = []
    band = mylist[0]
    
    # all the inputs from user
#    folder1 = str(input('path to any Band image: ')) 
#    folder2 = str(input('path to map image: ')) 
#    folder3 = str(input('where do you want to save the RGB Band chips? '))
#    folder4 = str(input('where do you want to save the Map chips ? '))
#    folder5 = str(input('where do you want to save the RGB Band chip numpy files? '))
    for i in np.arange(0, band.shape[0], 256):
        
        for j in np.arange(0, band.shape[1], 256):
            chip_band1 = band1[i:i+256, j:j+256]
            chip_band2 = band2[i:i+256, j:j+256]
            chip_band3 = band3[i:i+256, j:j+256]
           
            print('chip_band1 : ' + str(chip_band1.shape))
            
            #calculating lat long coordinates of top left and bottom right point of the tile
            topleft = PtoL.XYtoLATLONG(UserInput.args['folder1'], i, j)
            bottomright = PtoL.XYtoLATLONG(UserInput.args['folder1'], i+256, j+256)
            
            #calculating the pixel coordinates in the map image corresponding to the lat long coordinates calculated above 
            XY_TOP_LEFT = LtoP.LATLONG_TO_XY(UserInput.args['folder2'], topleft[0], topleft[1])
            XY_BOTTOM_RIGHT = LtoP.LATLONG_TO_XY(UserInput.args['folder2'], bottomright[0], bottomright[1])
            
            #change the shape of map image tile to 256*256*3
            map_image = OpenandRead.getGeoTiffasArray(UserInput.args['folder2'])
            map_image = np.moveaxis(map_image, 0, -1)
            chip_map = map_image[XY_TOP_LEFT[0]:XY_BOTTOM_RIGHT[0], XY_TOP_LEFT[1]:XY_BOTTOM_RIGHT[1]] 
            print('chip_map shape : ' + str(chip_map.shape))
            print('-------------')
            
            a = chip_band1.shape
            b = chip_map.shape
            # making sure all the tiles being considered are 256*256
            if(a[0]+a[1] == 512 and b[0]+b[1] == 512):
                # individual bands to bgr
                C[:,:,0] = chip_band1
                C[:,:,1] = chip_band2
                C[:,:,2] = chip_band3
                ##newlist.append(C.max())
                C = C/600
                C = 255*C
                C [C>255] = 255 # if C is > 255 then C = 255
                
                #saving RGB band chips (cv2.imwrite converts to rgb)
                cv2.imwrite(UserInput.args['folder3'] + str(counter) + '.png', C)
                
                #making all the elements black in map tiles where it's black in the corresponding rgb band tiles
                values = C
                zero = 0
                find_zero = np.where(values == zero)
                chip_map[find_zero] = 0
               
                #saving map chips 
                Image.fromarray(chip_map).save(UserInput.args['folder4'] + str(counter) + '.png')
                
                #saving numpy files of rgb band chips 
                np.save(UserInput.args['folder5'] + str(counter) + '.npy', C)

                #counter + 1
                counter +=1
