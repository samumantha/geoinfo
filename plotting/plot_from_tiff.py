"""

S14Science Amazonas project

Author: Samantha Wittke, FGI

Last update: June 2020

atm: Script to plot tif file
Input: path to tif file to be plotted

Output: None, only showing figure  

"""

from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np


afile ='xxx.tif'

def raster2array(rasterfn):
    raster = gdal.Open(rasterfn)
    band = raster.GetRasterBand(1).ReadAsArray().astype('float')
    return band

band = raster2array(afile)
band[band==-99999] = np.nan

mymin= np.nanmin(band)
mymax= np.nanmax(band)

plt.axis('off')

plt.imshow(band, vmin=mymin,vmax=mymax)
plt.show()
plt.close()
