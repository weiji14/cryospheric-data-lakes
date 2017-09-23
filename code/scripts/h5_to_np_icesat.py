##Python 3 script to extract geophysical data from icesat HDF5 format files into python numpy-based arrays

import collections
import h5py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import pandas as pd
import xarray as xr

#print(os.getcwd())
os.chdir('/home/atom/alp/data/icesat/GLAH12.034/2003.02.20')
print(os.getcwd())

### Part 1 Load Data
#%%
def init_h5_keyDict(h5file, datagroup="Data_40HZ", useAll=False):
    '''
    Function to pick the fields we want from a HDF5 file.
    Currently hardcoded for ICESAT GLAH12 HDF5 files.

    Arguments:
    h5file -- input data, of type HDF5 https://support.hdfgroup.org/HDF5/whatishdf5.html
    datagroup -- the HDF5 data group to look in for ICESAT see https://nsidc.org/data/glas/data-dictionary-glah12
    useAll -- Set to True if you want to retrieve all fields in the datagroup, else just get stardard xyzt data

    Returns:
    fields -- python dictionary with keys (e.g. x, y, z, t) mapped to values (fieldnames within the HDF5 file)
    '''
    h5 = h5py.File(h5file, "r")
    assert(isinstance(h5, (h5py._hl.files.File)))

    #GLAH12 Product Data Dictionary https://nsidc.org/data/glas/data-dictionary-glah12
    #[k for k in h5.keys()]

    #%% Retrieve data stored in the hdf5 file using known keys.
    [g for g in h5['{0}'.format(datagroup)]]

    fields = collections.OrderedDict()
    [v.name for v in h5[datagroup].values()]

    #Standard parameters
    if useAll == False:
        fields['i'] = datagroup+'/Time/i_rec_ndx'                 #GLAS Record Index (i)
        fields['x'] = datagroup+'/Geolocation/d_lon'              #Longitude         (x)
        fields['y'] = datagroup+'/Geolocation/d_lat'              #Latitude          (y)
        if datagroup == 'Data_40HZ':
            fields['z'] = datagroup+'/Elevation_Surfaces/d_elev'  #Elevation         (z)
            fields['t'] = datagroup+'/Time/d_UTCTime_40'          #Timestamp         (t)
        elif datagroup == 'Data_1HZ':
            fields['k'] = datagroup+'/Geolocation/i_track'        #Track number      (k)
            fields['t'] = datagroup+'/Time/d_UTCTime_1'           #Timestamp         (t)

    #All other useful-ish parameters
    if useAll == True:
        def func(name, obj):
            if isinstance(obj, h5py.Dataset):
                if obj.ndim == 1:
                    fields[name] = datagroup+'/'+name
                else:
                    print("Warn: {0} is not one-dimensional, ignoring...".format(name))
        h5[datagroup].visititems(func)

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
    npData  -- numpy.array of shape (n, m) where n is number of fields and m is number of datapoints
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
    npData = np.hstack((h5[h5fields[key]][:].reshape(-1,1) for key in h5fields.keys() if h5[h5fields[key]].shape == m)).T
    assert(npData.shape == (len(h5fields), m))  #check that final numpy array has shape (n, m) where n is no. of features and m is no. of datapoints e.g. (4, 20000)
    npData.shape
    npData.ndim
    npData.T.ndim

    #%% pandas
    assert(isinstance(npData, np.ndarray))
    pdData = pd.DataFrame(npData.T, columns=h5fields.keys())
    pdData['t'] = pd.to_datetime(pdData['t'], unit='s', origin=pd.Timestamp('2000-01-01'), infer_datetime_format=True)  #convert time data into standard python datetime format
    assert(isinstance(pdData['t'][0], pd.Timestamp))

    #%% xarray
    assert(isinstance(pdData, pd.DataFrame))
    xrData = pdData.to_xarray()
    xrData
    assert(isinstance(xrData, xr.Dataset))

    return npData, pdData, xrData

#%%

h5fields40hz = init_h5_keyDict("GLAH12_634_1102_001_0071_0_01_0001.H5", datagroup="Data_40HZ")
npData, pdData, xrData = h5_to_pydata("GLAH12_634_1102_001_0071_0_01_0001.H5", h5fields40hz)
df40 = pdData.loc[:,['x','y','z','i']].loc[lambda df: df.y < 0]  #filter for Antarctica only (South of Equator)

h5fields1hz = init_h5_keyDict("GLAH12_634_1102_001_0071_0_01_0001.H5", datagroup="Data_1HZ", useAll=False)
npData, pdData, xrData = h5_to_pydata("GLAH12_634_1102_001_0071_0_01_0001.H5", h5fields1hz)
df1 = pdData.loc[:,['x','y','k','i']].loc[lambda df: df.y < 0]  #filter for Antarctica only (South of Equator)

df = df40
#pdData.to_csv("/home/atom/alp/code/scripts/pdData.csv")   #export Greenland and Antarctic data
#df.to_csv("/home/atom/alp/code/scripts/pdData.csv")       #export Antarctic data (South of Equator) only


### Part 2 Plot those datapoints!!
#%matplotlib notebook
%matplotlib inline
#old_settings = np.seterr()
#np.seterr(all='ignore')
#np.seterr(**old_settings)


#%% Matplotlib 2D
plt.scatter(pdData.loc[:,['x']], pdData.loc[:,['y']]); #2d plot, will show Greenland on top right and Antarctica at the bottom
plt.show()
plt.scatter(df.loc[:,['x']], df.loc[:,['y']]); #2d plot, showing data for Antarctica
plt.show()


#%% Matplotlib 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
mi=10000
x=df.loc[:mi,['x']]
y=df.loc[:mi,['y']]
z=df.loc[:mi,['z']]
ax.scatter(x, y, z, c=z, cmap=plt.cm.jet, zdir='z', s=2)
fig;

#%% Matplotlib 3D surface plot https://gis.stackexchange.com/a/66440/78212
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(x,y,z)
#ax.contour(x,y,z)
#fig;


#%% ipyleaflet
#!pip3 install ipyleaflet
#!jupyter nbextension enable --py ipyleaflet
#!jupyter nbextension enable --py --sys-prefix ipyleaflet
import ipyleaflet
print(ipyleaflet.__version__)
ipyleaflet.Map(center=[-77.84651, 166.75710], zoom=2)


#%% ipyvolume
#!pip3 install ipyvolume
#!jupyter nbextension enable --py ipyvolume
#jupyter nbextension enable --py --sys-prefix ipyvolume
import ipyvolume as ipv
print(ipv.__version__)
# If a blank box shows up, see https://superuser.com/questions/836832/how-can-i-enable-webgl-in-my-browser
ipv.quickscatter(x.values.flatten(), y.values.flatten(), z.values.flatten(), size=100000, marker="sphere")


#%% Folium
#!pip3 install folium
import folium
print(folium.__version__)
#%%timeit
map_osm = folium.Map(location=[-77.84651, 166.75710], zoom_start=3)
df.loc[0:100].apply(lambda row:folium.CircleMarker(location=[row['y'], row["x"]], popup=str(row['k']), radius=5).add_to(map_osm), axis=1)
map_osm


#%% laspy
#!pip3 install laspy
import laspy
print(laspy.__version__)
header = laspy.header.Header()
outfile = laspy.file.File("/home/atom/alp/code/scripts/output.las", mode="w", header=header)

allx = df.loc[:,['x']].values.flatten()
ally = df.loc[:,['y']].values.flatten()
allz = df.loc[:,['z']].values.flatten()

xmin = np.floor(np.min(allx))
ymin = np.floor(np.min(ally))
zmin = np.floor(np.min(allz))

outfile.header.offset = [xmin,ymin,zmin]
outfile.header.scale = [0.001,0.001,0.001]

outfile.x = allx
outfile.y = ally
outfile.z = allz

outfile.close()






# %%
latvar = f['/Data_1HZ/Geolocation/d_lat']
latitude = latvar[:]
lat_vr = [latvar.attrs['valid_min'], latvar.attrs['valid_max']]

lonvar = f['/Data_1HZ/Geolocation/d_lon']
longitude = lonvar[:]
lon_vr = [lonvar.attrs['valid_min'], lonvar.attrs['valid_max']]

latlon = np.dstack((latvar, lonvar))

# %%
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
