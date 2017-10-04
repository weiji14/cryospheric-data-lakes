##Python 3 script to extract geophysical data from icesat HDF5 format files into python numpy-based arrays

import collections
import dask
import dask.dataframe as dd
from dask.diagnostics import ProgressBar
import glob
import h5py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import pandas as pd
import tables
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

    # Retrieve data stored in the hdf5 file using known keys.
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
            fields['k'] = datagroup+'/Geolocation/i_track'        #Track number      (k)tables
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

#%%

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

    # calculate m (number of individual datapoints) so we can do reshapes and assertion checks
    dataListShape = [h5[h5fields[key]].shape for key in h5fields.keys()]
    assert(np.median(dataListShape) == np.max(dataListShape))  #stupid way to get 'm' which is the no. of individual datapoints
    m = np.max(dataListShape) #take m as the largest length

    # numpy
    npData = np.hstack((h5[h5fields[key]][:].reshape(-1,1) for key in h5fields.keys() if h5[h5fields[key]].shape == m)).T
    assert(npData.shape == (len(h5fields), m))  #check that final numpy array has shape (n, m) where n is no. of features and m is no. of datapoints e.g. (4, 20000)
    npData.shape
    npData.ndim
    npData.T.ndim

    # pandas
    assert(isinstance(npData, np.ndarray))
    pdData = pd.DataFrame(npData.T, columns=h5fields.keys())
    pdData['t'] = pd.to_datetime(pdData['t'], unit='s', origin=pd.Timestamp('2000-01-01'), infer_datetime_format=True)  #convert time data into standard python datetime format
    assert(isinstance(pdData['t'][0], pd.Timestamp))

    # xarray
    assert(isinstance(pdData, pd.DataFrame))
    xrData = pdData.to_xarray()
    xrData
    assert(isinstance(xrData, xr.Dataset))

    return npData, pdData, xrData

#%%

h5fields40hz = init_h5_keyDict("GLAH12_634_1102_001_0071_0_01_0001.H5", datagroup="Data_40HZ", useAll=False)
h5fields1hz = init_h5_keyDict("GLAH12_634_1102_001_0071_0_01_0001.H5", datagroup="Data_1HZ", useAll=False)

npData, pdData, xrData = h5_to_pydata("GLAH12_634_1102_001_0071_0_01_0001.H5", h5fields40hz)
df40 = pdData.loc[:,['x','y','z','i']].loc[lambda df: df.y < 0]  #filter for Antarctica only (South of Equator)

npData, pdData, xrData = h5_to_pydata("GLAH12_634_1102_001_0071_0_01_0001.H5", h5fields1hz)
df1 = pdData.loc[:,['x','y','k','i']].loc[lambda df: df.y < 0]  #filter for Antarctica only (South of Equator)

df = df40
#pdData.to_csv("/home/atom/alp/code/scripts/pdData.csv")   #export Greenland and Antarctic data
#df.to_csv("/home/atom/alp/code/scripts/pdData.csv")       #export Antarctic data (South of Equator) only

#%% Dask
#See also VITables, a GUI for PyTables https://github.com/uvemas/ViTables
print(dask.__version__)
p = ProgressBar()  #Real-time feedback on dask processes
p.register()

#%% Info inside the HDF5 file
#h5file = os.path.join('/home/atom/alp/data/icesat/GLAH12.034/2003.02.20/GLAH12_634_1102_001_0071_0_01_0001_test.H5')
#[k for k in h5py.File(h5file, "r").keys()]
#list(h5fields40hz.values())[0]

#%% Debugging https://github.com/pandas-dev/pandas/issues/17661
#store = pd.HDFStore(h5file, mode='r+')
#store.select('Data_40HZ/Geolocation/d_lon')
#store.__contains__("Data_40HZ/Geolocation")
#store.get_node("Data_40HZ/Elevation_Surfaces")
#store.get_storer("Data_40HZ")
#store.groups()
#store.items
#store.close()

#tables.is_hdf5_file(h5file)
#lala = tables.open_file(h5file, mode='r+', root_uep='/Data_40HZ/Geolocation')
#lala.del_node_attr('/d_lon', 'DIMENSION_LIST')
#lala.close()

#pd.read_hdf(h5file, key='/Data_40HZ/Geolocation/d_lon')
#dd.read_hdf(h5file, key='Data_40HZ/Geolocation/d_lon')

#%% Get dask.dataframe(s) for fields [i, x, y, z, k, t] from Data_40HZ and Data_1HZ
bugFixed = False
if bugFixed == True:
    #ideal command to run once ICESAT dask.read_hdf bug is fixed, upstream problem with PyTables https://github.com/PyTables/PyTables/issues/647
    df40 = dd.read_hdf('/home/atom/alp/data/icesat/GLAH12.034/**/*.H5', key='/Data_40HZ')
    df1 = dd.read_hdf('/home/atom/alp/data/icesat/GLAH12.034/**/*.H5', key='/Data_1HZ')
else:
    hpyPath = "/home/atom/alp/data/icesat/GLAHPY12.034"
    os.makedirs(hpyPath, mode=0o777, exist_ok=True)
    def pdData_to_hdf(h5f):
        outFile = hpyPath+"/"+h5f.split('/')[-1]
        if not os.path.exists(outFile):
            print(h5f.split('/')[-1])
            pd40 = h5_to_pydata(h5f, h5fields40hz)[1]
            pd40.to_hdf(outFile, key="/Data_40HZ", format='table', mode='w')
            pd1 = h5_to_pydata(h5f, h5fields1hz)[1]
            pd1.to_hdf(outFile, key="/Data_1HZ", format='table', mode='a')
    if len(glob.glob(hpyPath+'/*.H5')) != 637:
        [pdData_to_hdf(h) for h in glob.iglob('/home/atom/alp/data/icesat/GLAH12.034/**/*.H5')]  #convert data from raw NSIDC supplied HDF5 into PyTables compatible format
    subsetLen = 20
    subsetFiles = glob.glob(hpyPath+'/*.H5')[:subsetLen]
    df40 = dd.read_hdf(subsetFiles, key='/Data_40HZ')  #workaround command to load Data_40HZ data into dask, not dask.delayed so slow
    df1 = dd.read_hdf(subsetFiles, key='/Data_1HZ')   #workaround command to load Data_40HZ data into dask, not dask.delayed so slow
    #df40 = dask.delayed(dd.read_hdf)(hpyPath+'/*.H5', key='/Data_40HZ')
    #df1 = dask.delayed(dd.read_hdf)(hpyPath+'/*.H5', key='/Data_1HZ')

#%% Join the Data_40HZ and Data_1HZ data on i_rec_ndx(i) to get Track Number(k) on Data_40HZ table
assert(list(h5fields40hz.keys()) == ['i', 'x', 'y', 'z', 't'])
assert(list(h5fields1hz.keys()) == ['i', 'x', 'y', 'k', 't'])
df_all = dask.delayed(df40.merge)(df1[['i', 'k']], on='i')   #Perform dask delayed parallel join
os.chdir('/home/atom/alp/code/scripts')                      #change directory so that mydask.png can be saved to the right directory when running dask.visualize()
df_all.visualize()

#%% Computationally intensive code if running on full ICESAT dataset!!
df = df_all.compute()   #very computationally intensive!!
assert(isinstance(df, dd.DataFrame))
#df.to_csv(hpyPath+'/export*.csv')  #export the joined table into csv files

df_all['k'].unique().compute()   #compute unique values of 'k' where k is the ICESAT Track Number
trackSubset = ((df_all['k'] <= 72) | (df_all['k'] >= 42))  #which ICESAT tracks to use
boundSubset = ((df_all['y'] < 0) & (df_all['x'] >= 0))   #Geographical boundaries
sqlFilter = trackSubset & boundSubset
df = df_all[sqlFilter]
df = df.compute()  #Computes lazy dataframe and makes it non-lazy
df = df.persist()  #will persist dataframe in RAM
print(df)
assert(isinstance(df, dd.DataFrame))

### Part 2 Plot those datapoints!!
#%matplotlib notebook
%matplotlib inline

#%% Holoviews + Datashader + Geoviews
#!conda install -y holoviews
#!conda install -y -c bokeh datashader
#!conda install -c ioam geoviews
import holoviews as hv
import datashader as ds
import geoviews as gv
print(hv.__version__)
print(ds.__version__)
print(gv.__version__)
hv.extension('bokeh')
hv.notebook_extension('bokeh')
#holoviews misc imports
from holoviews.streams import * #RangeXY
from colorcet import cm
#datashader misc imports
from holoviews.operation.datashader import aggregate, datashade, dynspread, shade
#Geoviews misc imports
import geoviews.feature as gf
from cartopy import crs
#Datashader options
dynspread.max_px=20
dynspread.threshold=0.5
shade.cmap="#30a2da" # to match HV Bokeh default
# See https://anaconda.org/jbednar/holoviews_datashader/notebook

print(df.info(), df.head())

#%%
#df = df.set_index('t')
#Reproject points from EPSG 4326 (PlateCarree) to EPSG 3031
points = gv.Points(df, kdims=[('x', '3031X'), ('y', '3031Y')], vdims=['i', 'z', 'k'], crs = crs.PlateCarree())
projected_gv = gv.operation.project_points(points, projection=crs.epsg(3031))
assert(isinstance(projected_gv, gv.element.geo.Points))

#%%
%%opts QuadMesh [tools=['hover']] (alpha=0 hover_alpha=0.2)
%%output size=300  #set output size, e.g. 200 = 2x the default output size
hv.notebook_extension('bokeh')
gv_options = {'bgcolor':'black', 'show_grid':True}

hvmap = projected_gv
dsmap = datashade(hvmap, x_sampling=1, y_sampling=1, cmap=cm['fire'])
gvmap = dynspread(dsmap.opts(plot=gv_options))
gvmap * hv.util.Dynamic(aggregate(hvmap, width=5, height=5, streams=[PointerX]), operation=hv.QuadMesh)

#%%
#!pip install paramnb
#!conda install -y -c ioam parambokeh
import param
import paramnb
import parambokeh

minAlt = round(df['z'].min().compute(), -2)
maxAlt = round(df['z'].max().compute(), -2)

class IceSatExplorer(hv.streams.Stream):
    colormap  = param.ObjectSelector(default=cm["fire"], objects=cm.values())
    altitude  = param.Range(default=(minAlt, maxAlt), bounds=(minAlt, maxAlt), doc="""Elevation of ICESAT laser point""")
    timerange = param.Range()
    
    def make_view(self, x_range=None, y_range=None, **kwargs):
        #map_tiles = tiles.opts(style=dict(alpha=self.alpha), plot=options) 

        hvmap = projected_gv.select(z=self.altitude)
        dsmap = datashade(hvmap, x_sampling=1, y_sampling=1, cmap=self.colormap,
                          dynamic=False, x_range=x_range, y_range=y_range)
        gv_options = {'bgcolor':'black', 'show_grid':True}
        gvmap = dynspread(dsmap.opts(plot=gv_options))
        return gvmap #* hv.util.Dynamic(aggregate(hvmap, width=5, height=5, streams=[PointerX]), operation=hv.QuadMesh)
        
        #points = hv.Points(df, kdims=[self.plot+'_x', self.plot+'_y'], vdims=['passenger_count'])
        #selected = points.select(passenger_count=self.passengers)
        #taxi_trips = datashade(selected, x_sampling=1, y_sampling=1, cmap=self.colormap,
        #                       dynamic=False, x_range=x_range, y_range=y_range,
        #                       width=800, height=475)
        #return map_tiles * taxi_trips

#%%
%%output size=300  #set output size, e.g. 200 = 2x the default output size
explorer = IceSatExplorer()
paramnb.Widgets(explorer, callback=explorer.event)
hv.DynamicMap(explorer.make_view, streams=[explorer, RangeXY()])

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
fig

#%% Matplotlib 3D surface plot https://gis.stackexchange.com/a/66440/78212
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(x,y,z)
#ax.contour(x,y,z)
#fig;

#%% Folium
#!pip install folium
import folium
print(folium.__version__)
#%%timeit
map_osm = folium.Map(location=[-77.84651, 166.75710], zoom_start=3)
df.loc[0:100].apply(lambda row:folium.CircleMarker(location=[row['y'], row["x"]], popup=str(row['k']), radius=5).add_to(map_osm), axis=1)
map_osm


#%% laspy
#!pip install laspy
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
