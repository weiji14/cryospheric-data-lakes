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
    start = time.time()
    print('Fetch async process {0} started at {1}'.format(pid, start))

    toCdDir = "/".join(URL.split("/")[1:-1])   #the directory inside the ftp server to change_directory (cd) into
    theFile = URL.split("/")[-1]               #the filename which we wish to get

    async with aioftp.ClientSession(siteURL, 21, user=usr, password=pwd) as client:
        print(await client.get_current_directory())   #print current working directory in ftp
        await client.change_directory(toCdDir)        #change ftp directory to the folder we want
        print(await client.get_current_directory())   #print the new current working directory

        #for path, info in (await client.list(recursive=True)):
        #    print(path, info)

        print("Downloading", theFile)
        print(await client.is_file(theFile))
        await client.download(theFile, os.path.join(dataDir, satName, path))                #finally downloads the file we want into specified folder
        print(theFile, "has been downloaded")

        #for path, info in (await client.list(recursive=True)):
            #print(path,info)
            #if info["type"] == "file" and path.suffix == ".HDR":
            #    await client.download(path)

    print('Process {}, took: {:.2f} seconds'.format(pid, time.time() - start))

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
    '''
        Info below is valid as of 20170701:

        To access Cryosat data, you'll have to obtain an ESA Earth Online login https://earth.esa.int/web/guest/-/how-to-access-cryosat-data-6842
        TLDR:
            Registration page is at https://eo-sso-idp.eo.esa.int/idp/umsso20/registration, go there and fill in all your login info.

        HAHAYHTR (haha you have to read):
            Once you have an ESA EO account, do the 2-day long 'fast registration' https://earth.esa.int/web/guest/pi-community/apply-for-data/fast-registration
            This is so that you can actually gain access to the ftp servers holding the data.
            Follow the guidelines there to register for access to practical all the Cryosat datasets you can get your hands on (in case you want them later).
            Specifically though, you probably just want the SIR_GDR_2 product, which is the most processed Geophysical Data Record Level 2 Cryosat product.

        Once you get an email that tells you your ftp username and password, you can enter it into the fields below! Good luck!!
    '''
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
    print("Synchronous process took: {:.2f} seconds".format(time.time() - start))
    #9.88s benchmark

    filepaths = [r"{0}".format("/".join([siteURL]+pathList+[filename])) for filename in filenames[2:4]]

    async def asynchronous():
        start = time.time()

        tasks = [asyncio.ensure_future(fetch_async(i, urlpath)) for i, urlpath in enumerate(filepaths)]  #Create series of coroutines to execute
        #tasks = [fetch_async(i, urlpath) for i, urlpath in enumerate(filepaths)]
        await asyncio.wait(tasks)                                                 #Execute those coroutines concurrently and wait for them to fin

        print("Asynchronous process took: {:.2f} seconds".format(time.time() - start))
        #17.80s benchmark

    #Asynchronous loop to download files recursively
    print('Asynchronous:')
    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(asynchronous())
        finally:
            loop.close()
    print("end")
