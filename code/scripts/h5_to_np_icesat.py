##Python 3 script to extract geophysical data from icesat HDF5 format files into python numpy-based arrays

import collections
import h5py
import numpy as np
import os
import pandas as pd
import xarray as xr

print(os.getcwd())
os.chdir('/home/atom/alp/data/icesat/GLAH12.034/2003.02.20')
print(os.getcwd())


if 1==1:
#with h5py.File("GLAH12_634_1102_001_0071_0_01_0001.H5", "r") as f:
    f = h5py.File("GLAH12_634_1102_001_0071_0_01_0001.H5", "r")
    f.name
    f.libver
    f.driver


    #GLAH12 Product Data Dictionary https://nsidc.org/data/glas/data-dictionary-glah12
    [k for k in f.keys()]

    # %%
    if isinstance(f, (h5py._hl.files.File)):
        datagroup = "Data_40HZ"
        [g for g in f['{0}'.format(datagroup)]]

        fields = collections.OrderedDict()
        [v.name for v in f[datagroup].values()]

        #Standard parameters
        fields['x'] = 'Geolocation/d_lon'
        fields['y'] = 'Geolocation/d_lat'
        fields['z'] = 'Elevation_Surfaces/d_elev'
        fields['t'] = 'Time/d_UTCTime_40'

        #All other useful-ish parameters
#        def func(name, obj):
#            if isinstance(obj, h5py.Dataset):
#                if obj.ndim == 1:
#                    fields[name] = name
#                else:
#                    print("Warn: {0} is not one-dimensional, ignoring...".format(name))
#        f[datagroup].visititems(func)

        #Finally create the n-dimensional array to store all the data. Do this by stacking each feature (e.g. coordinates/time/other param) using np.dstack.
        dataListShape = [f[datagroup+'/'+fields[key]].shape for key in fields.keys()]
        assert(np.median(dataListShape) == np.max(dataListShape))  #stupid way to get 'm' which is the no. of individual datapoints
        m = np.max(dataListShape) #take m as the largest length

        ## numpy
        xyzt = np.hstack((f[datagroup+'/'+fields[key]][:].reshape(-1,1) for key in fields.keys() if f[datagroup+'/'+fields[key]].shape == m)).T
        assert(xyzt.shape == (len(fields), m))  #check that final numpy array has shape (n, m) where n is no. of features and m is no. of datapoints e.g. (4, 20000)
        xyzt.shape
        xyzt.ndim
        xyzt.T.ndim

        ## pandas
        assert(isinstance(xyzt, np.ndarray))
        pdData = pd.DataFrame(xyzt.T, columns=fields.keys())
        pdData['t'] = pd.to_datetime(pdData['t'], unit='s', origin=pd.Timestamp('2000-01-01'), infer_datetime_format=True)  #convert time data into standard python datetime format
        pdData

        pdData.loc[:,['x','y','z']].loc[lambda df: df.y < 0].to_csv("/home/atom/alp/code/scripts/pdData.csv")  #export Antarctic data (South of Equator) only
        pdData.to_csv("/home/atom/alp/code/scripts/pdData.csv")

        ##%%
        assert(isinstance(pdData['t'][0], pd.Timestamp))
        #help(pdData.loc)

        ## xarray
        assert(isinstance(pdData, pd.DataFrame))
        xrData = pdData.to_xarray()
        xrData
        assert(isinstance(xrData, xr.Dataset))


    # %%

    latvar = f['/Data_1HZ/Geolocation/d_lat']
    latitude = latvar[:]
    lat_vr = [latvar.attrs['valid_min'], latvar.attrs['valid_max']]

    lonvar = f['/Data_1HZ/Geolocation/d_lon']
    longitude = lonvar[:]
    lon_vr = [lonvar.attrs['valid_min'], lonvar.attrs['valid_max']]

    Data_40HZ/Time/d_UTCTime_40

    latlon = np.dstack((latvar, lonvar))

def h5_treeview(h5file):
        assert isinstance(h5file, (h5py._hl.files.File))

        for k1 in sorted(h5file.keys()):
            print(k1)
            for k2 in f[k1]:
                print("'--", k2)


h5_treeview(f)
f['ANCILLARY_DATA']

f[datagroup].visititems(lambda name, object: print(name.count('/')*"    "+"'--"+name, object))
f[datagroup].visititems(lambda name, object: (None))
