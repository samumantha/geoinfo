#export attributes to hdf or csv



import shapefile
import pandas as pd
import os
import numpy as np
from datetime import datetime
import copy
import h5py
import csv
#conda activate hdfattr/gisthings

class Attributor(object):

    def __init__(self,shpfile,hdfname):

        self.shp = shapefile.Reader(shpfile)

        self.getattributes(shpfile,hdfname)

    
    def getattributes(self,shpfile,hdfname):

        #store = pd.HDFStore(hdfname)
        #with h5py.File(hdfname) as hdf:
        self.fieldnames = self.getfieldnames()
        #print(self.fieldnames)
        columnnames = self.fieldnames[:]
        columnnames.append('centerX')
        columnnames.append('centerY')


        records = self.shp.records()
        shapes = self.shp.shapes()
        
        idbasedcontent = []
        fullcontent = []

        with open('test.csv','a') as mycsv:
            writer = csv.writer(mycsv)

            for i, rec in enumerate(records):
            
                bbox = shapes[i].bbox
                centerx = bbox[0] + ((bbox[2] - bbox[0])/2)
                centery = bbox[1] + ((bbox[3] - bbox[1])/2)


                idbasedcontent = []

                for field in self.fieldnames:

                    value = rec[field]
                    print(type(value))
                    if value is None:
                        print('none found')
                        value = 0
                    
                    idbasedcontent.append(value)
                
                idbasedcontent.append(round(centerx,3))
                idbasedcontent.append(round(centery,3))

                writer.writerow(idbasedcontent)

                #idbasedcontentscii = [n.encode("ascii", "ignore") for n in idbasedcontent]
                #print(idbasedcontentscii)
                #hdf.create_dataset(idbasedcontentscii[0],data=idbasedcontentscii[1:])

                
        return idbasedcontent


    def getfieldnames(self):

        print('getfieldnames')
        #gives all fieldnames, first of each sublist is the name, omit deletionflag  (0)
        fields = self.shp.fields
        #print(fields)

        fieldnames = []
        for a,field in enumerate(fields):
            if not a == 0:
                #print(str(field[0]))
                fieldnames.append(field[0])

        #after fieldnames there should be DOY 1-365 for the dateonehot
        
        #datefields = [np.str(x) for x in range(1,366)]
        #fieldnamesext = copy.deepcopy(fieldnames)
        #fieldnamesext.extend(datefields)
        print(fieldnames)
        
        return fieldnames



myshp = ''
hdfname = '' 

Attributor(myshp,hdfname)

