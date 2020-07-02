import datetime
import numpy as np

# sorts the second list according to the first list ascending based on indices

#INPUT
mydates = ['20140103','20141003','20150908','20140607']
mylist =['this','very','good','looks']

#FUNCTION
def sortdates(mydates,mylist):
       
        indices = np.argsort(mydates)
        #dates.sort()
        sortedlist= []
        for myindex in indices: 
            print(myindex)

            sortedarray.append(mylist[myindex])
        print(sortedlist)


#RUN
sortdates(mydates,mylist)
