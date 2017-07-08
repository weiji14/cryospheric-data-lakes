# Cryospheric Data Lakes

[![License: Open Data Commons Attribution](https://img.shields.io/badge/License-ODC_BY-brightgreen.svg)](https://opendatacommons.org/licenses/by/)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

Open-source big data tools to handle various cryospheric remote sensing datasets.

> ### [Data lake](https://en.wikipedia.org/wiki/Data_lake)
> ... a method of storing data within a system or repository, in its natural format, that facilitates the collocation of data in various schemata and structural forms, usually object blobs or files... ~Wikipedia

## Contents

Find the underlying [data here](/data) used in this project (or at least links to the sources since they might be too big).

Examine the [code here](/code) which mingles with the data to give some (hopefully) nice scientifically meaningful outputs (whatever that means). You may find some interesting dockerfiles and python3 code inside (if that clicks with you).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Pre-requisites

You have some form of [git](https://git-scm.com/) installed. Ideally, [docker](https://www.docker.com/) should be installed too to fully replicate this scientific development environment.

For Debian/Ubuntu-based systems, you can try something like:

    sudo apt install git docker-ce

Note: You may need to set-up the repository first to install docker-ce. See instructions for [Debian](https://docs.docker.com/engine/installation/linux/docker-ce/debian/) and [Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/).

For Windows, if you have [chocolatey](https://chocolatey.org/) (recommended!), it can be as easy as:

    choco install git docker

For Mac OS X:

    TODO??

### Cloning the repository

With git installed, fire up your command prompt and do:

    git clone https://github.com/weiji14/cryospheric-data-lakes.git

Alternatively, download the zip file from [here](https://github.com/weiji14/cryospheric-data-lakes/archive/master.zip), and unzip it.

### Running the code

To try out the code (that downloads big data files, processes the data, etc) you can use the atom-hydrogen-beta docker container [here](/code/docker#atom) to ensure ease of reproducibility (aka mitigate denpendency hell problems). Yes, I do my code writing and execution inside that 'atom' docker container with interactive [Hydrogen](https://github.com/nteract/hydrogen#hydrogen-) functionality!!

![atom-demo-10](https://user-images.githubusercontent.com/23487320/28195882-1c82e6dc-68a1-11e7-9da9-236918621d5d.gif)

But of course, you can install the libraries yourself.

## Contributing

Feel free to submit a pull request or issue (nice ways of saying hi!) if you'd like to see something in here that's not here yet.

## License

### Data
Any raw [data](/data) (e.g. binary satellite files) used here is licensed accordingly as per the upstream source. Derived datasets are licensed under the [Open Data Commons Attribution license](https://opendatacommons.org/licenses/by/) unless otherwise stated.

### Code

Source [code](/code) used in the handling of the data is licensed under the [GNU Lesser General Public License v3.0](https://choosealicense.com/licenses/lgpl-3.0/).

### Other

Other forms of content (such as documentation) in this project repository which is not covered by the above two licenses is licensed under the [Creative Commons Attribution Share Alike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).
