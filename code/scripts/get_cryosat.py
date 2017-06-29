## Python 3 script to download satellite data from FTP sites.
## Originally designed for pulling data from European Space Agency (ESA) FTP sites, e.g. for Cryosat-2
import ftplib
import getpass
import os

print(os.getcwd())
ftpSites = {'ESA EO' : "science-pds.cryosat.esa.int"}
#ftpSites.extend{"NSIDC Earthdata" : "https://n5eil01u.ecs.nsidc.org/GLAS/GLA12.034/"}  #TODO add icesat and other satellites as well?

for orgAccount, siteURL in ftpSites.items():
    #
    if 'cryosat' in siteURL:
        path = os.path.join("SIR_GDR", "2017", "01")
        if not os.path.exists(os.path.join(os.getcwd(), path)):
            os.makedirs(os.path.join(os.getcwd(), path))

    #Connect to ftp site using your own login information
    ftp = ftplib.FTP(siteURL)                           #Connect to top level of the FTP server
    usr = input("{0} login username".format(orgAccount))
    pwd = getpass.getpass("{0} login password".format(orgAccount))
    ftp.login(usr, pwd)                                 #login using raw input of username and password

    #Get list of stuff in the ftp directory
    print(ftp.dir())
    [ftp.cwd(dir) for dir in path.split(os.sep)]        #change to path we want recursively, cross-platform compatible
    ftp.retrlines('LIST')                               #print list of files in ftp folder
    filenames = ftp.nlst()                              #get list of files in ftp folder

    #Loop to download files recursively
    for filename in filenames[:2]:
        ftp.retrbinary('RETR {0}'.format(filename), open(os.path.join(os.getcwd(), path, filename), 'wb').write)
