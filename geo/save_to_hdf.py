def tohdf(myid,date,band,myarray,pathrow,year):

    myid = str(myid)
    date = str(date)

    
    hdfpath = ''
    hdfname = os.path.join(hdfpath,pathrow + '_' + year + '.hdf')

    with h5py.File(hdfname, 'a') as hf:
        if hf.get(myid) is None:
            idgroup = hf.create_group(myid)
        else:
            idgroup = hf.get(myid)
        if idgroup.get(date) is None:
            dategroup = idgroup.create_group(date)
        else:
            dategroup = idgroup.get(date)
        dategroup.create_dataset(band,data= myarray)
