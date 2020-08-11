from osgeo import gdal,osr
import os
import subprocess

def reproject(shpfile,raster):
    print('INFO: checking the projection dependent on '+ raster +' of the inputfile now')
    head, tail = os.path.split(shpfile)
    root, ext = os.path.splitext(tail)
    openrasterfile = gdal.Open(raster)
    rasterprojection = openrasterfile.GetProjection()
    rasterrs = osr.SpatialReference(wkt=rasterprojection)
    rasterepsg = rasterrs.GetAttrValue('AUTHORITY',1)
    #rasterepsg = '32634'
    ##reproject the shapefile according to projection of Sentinel2/raster image
    reprojectedshape = os.path.join(head, root + '_reprojected_'+ rasterepsg+ ext)
    if not os.path.exists(reprojectedshape):
        reprojectcommand = 'ogr2ogr -t_srs EPSG:'+rasterepsg+' ' + reprojectedshape + ' ' + shpfile
        subprocess.call(reprojectcommand, shell=True)
        print('INFO: ' + shpfile + ' was reprojected to EPSG code: ' + rasterepsg + ' based on the projection of ' + raster)
    return reprojectedshape
