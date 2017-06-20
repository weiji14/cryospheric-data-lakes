try:
    import requests
except ImportError as e:
    missingModule = e.message.split(' ')[-1]
    print('{0} not acccessible/installed, doing pip install now'.format(missingModule))
    import pip
    pip.main(["install", "--upgrade", "pip"])  #upgrades pip to latest version first
    pip.main(["install", missingModule])       #uses pip to install missing module
finally:
    import os


#url = "https://n5eil01u.ecs.nsidc.org/GLAS/GLA12.034/"  #with metadata and nicer folder structure
#url = "https://search.earthdata.nasa.gov/granules/download.html?project=5498684463&collection=C1000000441-NSIDC_ECS"  #just the 637 *.DAT files
with open("icesat_links.txt", 'r') as manyLinks:
    links = manyLinks.readlines()
    for link in links:
        pass

