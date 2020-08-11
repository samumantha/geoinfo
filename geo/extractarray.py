# for LS 7

import os
from rasterstats import zonal_stats

def extractarray(rasterpath ,shpfile,pathrow,year):

    date = os.path.split(rasterpath)[-1].split('_')[3]
    band = os.path.splitext(os.path.split(rasterpath)[-1])[0].split('_')[-1]
    idname = 'newID

    print('arrayextractor started')

    a=zonal_stats(shpfile, rasterpath, stats=['mean'], band=1, geojson_out=True, all_touched=True, raster_out=True)

    for x in a:
        myarray = x['properties']['mini_raster_array']
        print(x['properties']['mini_raster_nodata'])
        print(myarray)
        myarray = myarray.filled(-9999)
        print(myarray)
        print(type(myarray))
        myid = x['properties'][idname]
        mystat = x['properties']['mean'] 
        #do something with it
