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

# %%
def init_h5_keyDict(h5file):
    '''
    Function to pick the fields we want from a HDF5 file.
    Currently hardcoded for ICESAT GLAH12 HDF5 files.

    Arguments:
    h5file -- input data, of type HDF5 https://support.hdfgroup.org/HDF5/whatishdf5.html

    Returns:
    fields -- python dictionary with keys (e.g. x, y, z, t) mapped to values (fieldnames within the HDF5 file)
    '''
    h5 = h5py.File(h5file, "r")
    assert(isinstance(h5, (h5py._hl.files.File)))

    #GLAH12 Product Data Dictionary https://nsidc.org/data/glas/data-dictionary-glah12
    #[k for k in h5.keys()]

    #%% Retrieve data stored in the hdf5 file using known keys.
    datagroup = "Data_40HZ"
    [g for g in h5['{0}'.format(datagroup)]]

    fields = collections.OrderedDict()
    [v.name for v in h5[datagroup].values()]

    #Standard parameters
    fields['x'] = datagroup+'/Geolocation/d_lon'
    fields['y'] = datagroup+'/Geolocation/d_lat'
    fields['z'] = datagroup+'/Elevation_Surfaces/d_elev'
    fields['t'] = datagroup+'/Time/d_UTCTime_40'

    #All other useful-ish parameters
    #def func(name, obj):
    #    if isinstance(obj, h5py.Dataset):
    #        if obj.ndim == 1:
    #            fields[name] = name
    #        else:
    #            print("Warn: {0} is not one-dimensional, ignoring...".format(name))
    #h5[datagroup].visititems(func)

    assert(isinstance(fields, dict))
    return fields

def h5_to_pydata(h5file, h5fields):
    '''
    Function to load data from one HDF5 file to standard Python based formats.
    Basically creates an n-dimensional array to store all the data. Do this by stacking each feature (e.g. coordinates/time/other param) using np.stack.

    Arguments:
    h5file -- input data, of type HDF5 https://support.hdfgroup.org/HDF5/whatishdf5.html
    h5fields -- python dictionary containing keys (e.g. x, y, z, t) mapped to values (fieldnames within the HDF5 file)

    Returns:
    xyzt  -- numpy.array of shape (n, m) where n is number of fields and m is number of datapoints
    pdData -- pandas.DataFrame version of above numpy array, with the time (t) field/column expressed in standard python datetime format
    xrData -- xarray.Dataset version of the above pandas.DataFrame which has dimensions (m) and data variables (n)
    '''
    h5 = h5py.File(h5file, "r")
    assert(isinstance(h5, (h5py._hl.files.File)))
    #h5.name
    #h5.libver
    #h5.driver

    #%% calculate m (number of individual datapoints) so we can do reshapes and assertion checks
    dataListShape = [h5[h5fields[key]].shape for key in h5fields.keys()]
    assert(np.median(dataListShape) == np.max(dataListShape))  #stupid way to get 'm' which is the no. of individual datapoints
    m = np.max(dataListShape) #take m as the largest length

    #%% numpy
    xyzt = np.hstack((h5[h5fields[key]][:].reshape(-1,1) for key in h5fields.keys() if h5[h5fields[key]].shape == m)).T
    assert(xyzt.shape == (len(h5fields), m))  #check that final numpy array has shape (n, m) where n is no. of features and m is no. of datapoints e.g. (4, 20000)
    xyzt.shape
    xyzt.ndim
    xyzt.T.ndim

    #%% pandas
    assert(isinstance(xyzt, np.ndarray))
    pdData = pd.DataFrame(xyzt.T, columns=h5fields.keys())
    pdData['t'] = pd.to_datetime(pdData['t'], unit='s', origin=pd.Timestamp('2000-01-01'), infer_datetime_format=True)  #convert time data into standard python datetime format
    assert(isinstance(pdData['t'][0], pd.Timestamp))

    #%% xarray
    assert(isinstance(pdData, pd.DataFrame))
    xrData = pdData.to_xarray()
    xrData
    assert(isinstance(xrData, xr.Dataset))

    return xyzt, pdData, xrData

h5fields = init_h5_keyDict("GLAH12_634_1102_001_0071_0_01_0001.H5")
xyzt, pdData, xrData = h5_to_pydata("GLAH12_634_1102_001_0071_0_01_0001.H5", h5fields)
pdData.loc[:,['x','y','z']].loc[lambda df: df.y < 0].to_csv("/home/atom/alp/code/scripts/pdData.csv")  #export Antarctic data (South of Equator) only
pdData.to_csv("/home/atom/alp/code/scripts/pdData.csv")



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
