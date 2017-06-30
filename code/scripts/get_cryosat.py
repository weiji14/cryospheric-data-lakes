#!/usr/bin/env python3
## Python 3 script to download satellite data from FTP sites.
## Originally designed for pulling data from European Space Agency (ESA) FTP sites, e.g. for Cryosat-2
import ftplib
import getpass
import os
import asyncio
import aioftp
import time

print(os.getcwd())
dataDir = os.path.join(os.getcwd(), 'data')
ftpSites = {'ESA EO' : "science-pds.cryosat.esa.int"}
#ftpSites.extend{"NSIDC Earthdata" : "https://n5eil01u.ecs.nsidc.org/GLAS/GLA12.034/"}  #TODO add icesat and other satellites as well?

MAX_CLIENTS = 3
async def fetch_async(pid, URL):
    print('Fetch async process {} started'.format(pid))
    start = time.time()
    response = await aiohttp.request('GET', URL)
    datetime = response.headers.get('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    response.close()
    return datetime

for orgAccount, siteURL in ftpSites.items():
    #
    if 'cryosat' in siteURL:
        satName = 'cryosat'
        pathList = ["SIR_GDR", "2017", "01"]
        path = os.path.join("SIR_GDR", "2017", "01")

    #Make directory if not already exist
    if not os.path.exists(os.path.join(dataDir, satName, path)):
        os.makedirs(os.path.join(dataDir, satName, path))

    #Connect to ftp site using your own login information
    ftp = ftplib.FTP(siteURL)                           #Connect to top level of the FTP server
    usr = input("{0} login username".format(orgAccount))
    pwd = getpass.getpass("{0} login password".format(orgAccount))
    ftp.login(usr, pwd)                                 #login using raw input of username and password

    #Get list of stuff in the ftp directory
    #print(ftp.dir())
    [ftp.cwd(dir) for dir in path.split(os.sep)]        #change to path we want recursively, cross-platform compatible
    #ftp.retrlines('LIST')                               #print list of files in ftp folder
    filenames = ftp.nlst()                              #get list of files in ftp folder

    #Synchronous loop to download files recursively
    print('Synchronous:')
    start = time.time()
    for filename in filenames[:2]:
        ftp.retrbinary('RETR {0}'.format(filename), open(os.path.join(dataDir, satName, path, filename), 'wb').write)
    print("Process took: {:.2f} seconds".format(time.time() - start))

    async def asynchronous():
        start = time.time()
        filepaths = [r"ftp://{0}".format("/".join([siteURL]+pathList+[filename])) for filename in filenames[2:4]]
        tasks = [asyncio.ensure_future(
            fetch_async(i, urlpath)) for i, urlpath in enumerate(filepaths)]
        await asyncio.wait(tasks)
        print("Process took: {:.2f} seconds".format(time.time() - start))

    #Asynchronous loop to download files recursively
    print('Asynchronous:')
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asynchronous())
    ioloop.close()
