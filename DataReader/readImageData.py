import numpy as np
import os


def readImageData(filename, width=None, height=None, header_size=0, dtype=np.uint16,memmap=0, mode='r'):
    """

    :param filename:
    :param width:
    :param height:  (Default value = None)
    :param header_size:  (Default value = 0)
    :param dtype:  (Default value = np.uint16)

    """

    extension = filename.split('.')[-1]
    known_extensions = ['jpg', 'gif', 'png', 'tif','bmp','JPG', 'GIF', 'PNG', 'TIF','BMP', 'npy']

    if extension in known_extensions:
       

        if extension=='tif':
            import gdal
            ds = gdal.Open(filename)
            nbands = ds.RasterCount
            width = ds.RasterXSize
            height = ds.RasterYSize
            image = np.ones((height,width),np.float32)
            band = ds.GetRasterBand(1)
            image[:,:] = np.float32(band.ReadAsArray(0, 0, width, height))
       
        elif extension=='npy':
            #import numpy as np
            image = np.load(filename)
       
        else:
            from PIL import Image
           
            image = Image.open(filename)
            image = np.array(image)

    else:

        if width is None:
           
            if os.path.exists(filename+'.hdr'):
                try:
                    #logging.info('No information about scan pix is given,trying to envi header : %s',filename+'.hdr')
                    #param_dict=read_envi_header(filename+'.hdr')
                    #params=gen_params(param_dict)
                    #width=np.int32(params.ncols)
                    #height=np.int32(params.nrows)
                    #header_size=np.int32(params.offset)
                    #dtype=params.dtype
                    raise("not gonna work without envi")

                except Exception as ex:
                    print('problem in Envi Header Parsing = '+str(ex))
               
            elif os.path.exists(filename+'.scan_pix'):
                scn_pix_fname=filename+'.scan_pix'
               
   
                scan_pix_data=read_csvfile(scn_pix_fname)
                width=np.int32(scan_pix_data[1])
                height=np.int32(scan_pix_data[0])
                dtype=np.int16
               
            else:
                raise('Cant read image given '+filename)
       
        bytes_per_pixel = np.int32(np.dtype(dtype).str[-1])

        if height is None and width != None:
            f_size = 0
            f_size = os.path.getsize(filename)
            height = int((f_size - header_size) / (width*bytes_per_pixel))

        if memmap == 0:
            count = (height * width + header_size) * bytes_per_pixel
            image = np.fromfile(filename, dtype=dtype, count=count)
            image = image[header_size // bytes_per_pixel:(header_size // bytes_per_pixel) + height * width]
            image = image.reshape(height, width)
        else:
            if header_size == 0:
                image = np.memmap(filename, dtype=dtype, mode=mode,shape=(height,width))
            else:
                raise ValueError('Memmap cannot be invoked with headers in file for now : put memmap flag to zero : contact abhishek ')
               

    return image
