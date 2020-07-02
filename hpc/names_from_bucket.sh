#!/bin/bash

###########################
#small bash script to get all Sentinel-2 SAFE dir filenames from a bucket in object storage
###########################

bucketname=s3://2001106_L1C/

#get list of files from s3cmd ls and only get the SAFE directory names, print to file
s3cmd ls $bucketname | awk '{ print $2 }' > file.txt
#get rid of file structure print to file
cut -d '/' -f 4 file.txt >> newfile.txt
#get rid of everything other than S-2 files starting with S2.... print to file
sed '/^S2/!d' newfile.txt >> finalfile.txt
#rename file
mv finalfile.txt downloaded.txt
