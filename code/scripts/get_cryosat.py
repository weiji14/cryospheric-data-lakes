#!/usr/bin/env python3
## Python 3 script to download satellite data from FTP sites.
## Originally designed for pulling data from European Space Agency (ESA) FTP sites, e.g. for Cryosat-2
import asyncio
import aioftp
import getpass
import pathlib
import time

MAX_CLIENTS = 7       #set the number of connections allowed (default: 7)
print(pathlib.Path.cwd())
dataDir = pathlib.PurePath(pathlib.Path.cwd()).joinpath('data')

ftpSites = {'ESA EO' : "science-pds.cryosat.esa.int"}
#ftpSites.extend{"NSIDC Earthdata" : "https://n5eil01u.ecs.nsidc.org/GLAS/GLA12.034/"}  #TODO add icesat and other satellites as well?

async def smart_recursive_dwn(client, pathName, pathFolder):
    '''
    Using aioftp client, download what's in pathName (remote) to pathFolder (local)
    '''
    #checks first if the pathName references a file or a folder
    if await client.is_file(pathName):
        #print((await client.stat(pathName))['size'], pathlib.Path(pathFolder, pathName).stat().st_size)
        #print(pathlib.Path(pathFolder, pathName).exists(), (await client.stat(pathName))['size'], pathlib.Path(pathFolder, pathName).stat().st_size)
        if (not pathlib.Path(pathFolder, pathName).exists()) or (int((await client.stat(pathName))['size']) != pathlib.Path(pathFolder, pathName).stat().st_size):
            start = time.time()
            print("Downloading", pathName)
            await client.download(pathName, pathFolder)                #finally downloads the file we want into specified folder
            print("{} download took {:.2f} seconds".format(pathName, time.time()-start))
    elif await client.is_dir(pathName):
        await client.change_directory(pathName)
        print("Starting recursive download of {0} files in {1}".format(len(await client.list(await client.get_current_directory())), await client.get_current_directory()))
        for newPath, _ in (await client.list()):
            await smart_recursive_dwn(client, newPath, pathlib.Path(pathFolder, pathName))                   #we loop inside a loop!

async def fetch_async(sem, pid, posixPath):
    async with sem:        #ensure that we abide by Semaphore limit. I.e. do not DOS attack the FTP server
        start = time.time()
        print('Fetch async process {0} started at {1}'.format(pid, start))

        toCdDir = posixPath.parent  #[1:-1])   #the directory inside the ftp server to change_directory (cd) into
        pathName = posixPath.name               #the folder/filename which we wish to get

        async with aioftp.ClientSession(siteURL, 21, user=usr, password=pwd) as client:
            await client.change_directory(toCdDir)        #change ftp directory to the folder we want
            await smart_recursive_dwn(client, pathName, pathlib.Path(dataDir, satName, toCdDir))

            #for path, info in (await client.list(recursive=True)):
                #print(path,info)
                #if info["type"] == "file" and path.suffix == ".HDR":
                #    await client.download(path)

        print('Process {}, took: {:.2f} seconds'.format(pid, time.time() - start))

async def async_download(site, cdpath, usr, pwd):
    start = time.time()

    #Get list of filenames of the data files we want in a particular ftp folder
    async with aioftp.ClientSession(site, 21, user=usr, password=pwd) as client:
        filenames = [filename for filename, info in (await client.list(cdpath))]           #List of pathlib.PurePosixPaths to the files we want
        print("{0} files inside {1}".format(len(filenames), cdpath))

    #Create tasks and run them concurrently via asyncio
    sem = asyncio.Semaphore(MAX_CLIENTS)                                                 #Pass in Semaphore FTP connection limit
    tasks = [asyncio.ensure_future(fetch_async(sem, i, filename)) for i, filename in enumerate(filenames, start = 1)]  #Create series of coroutines tasks (download tasks) to execute
    await asyncio.wait(tasks)                                                   #Execute those coroutines concurrently and wait for them to fin

    print("Asynchronous process took: {:.2f} seconds".format(time.time() - start))
    #1827.44s benchmark on 942 files

for orgAccount, siteURL in ftpSites.items():
    #Manual hardcode to create local subdirectory name based on which server we get data from (E.g. cryosat if from ESA, icesat if from NSIDC, etc)
    if 'cryosat' in siteURL:
        satName = 'cryosat'
        cdPath = pathlib.Path("SIR_GDR", "2017")
    else:
        raise ValueError('unknown satellite')

    #Make directory if not already exist
    pathlib.Path.mkdir(pathlib.Path(dataDir / satName / cdPath), mode=0o777, parents=True, exist_ok=True)
    #pathlib.Path(dataDir / satName / cdPath).chmod(0o777)

    #Enter FTP login information
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

    #Asynchronous loop to download files recursively
    print('Asynchronous:')
    if __name__ == '__main__':
        #See https://stackoverflow.com/questions/43646768/cant-create-new-event-loop-after-calling-loop-close-asyncio-get-event-loop-in-p
        loop = asyncio.new_event_loop()         #Create a new asyncio event_loop
        asyncio.set_event_loop(loop)            #Set the event loop for the current context to loop
        loop = asyncio.get_event_loop()         #Use that new asyncio event_loop!

        try:
            loop.run_until_complete(async_download(siteURL, cdPath, usr, pwd))
        finally:
            loop.close()

    print("end")
