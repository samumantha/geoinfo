"""

class to check that cloudcover (according to metadata) of Sentinel-2 file (.SAFE) is below the maximum given by user

"""

import os
import glob
from xml.dom import minidom


class RasterValidator(object):

    def __init__(self, SAFEpath, maxcloudcover):
        self.SAFEpath = SAFEpath
        self.maxcloudcover = maxcloudcover
        self.cloudcovered = self.check_cloudcover()
        
    def get_xml(self):
        xmlname = 'MTD_MSIL2A.xml'
        xmlpath = os.path.join(self.SAFEpath, xmlname)
        return xmlpath

    def read_xml(self,xmlpath):
        doc = minidom.parse(xmlpath)
        return doc

    def get_cloudcover_percentage(self, doc): 
        cc_perc = float(doc.getElementsByTagName('Cloud_Coverage_Assessment')[0].firstChild.data)
        return cc_perc
    
    def check_cloudcover(self):
        # checks that according to metadata the cloudcover is below user given threshold
        cloudcover_percentage = self.get_cloudcover_percentage(self.read_xml(self.get_xml()))
        if cloudcover_percentage <= self.maxcloudcover:
            return True
        else:
            return False

          
# Call the object like this:
SAFEpath = 'path/to/one/S2/tile'
maxcloudcover = 10
# returns true or false
filecloudcovered = RasterValidator(SAFEpath, maxcloudcover)
