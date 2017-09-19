FROM debian:buster-slim
LABEL maintainer "https://github.com/weiji14"
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install standard dependencies a la buildpack-deps curl https://hub.docker.com/_/buildpack-deps/
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Setup base atom-beta install
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    # Install atom required dependencies See `apt-cache depends atom-beta`
    git \
    gconf2 \
    gconf-service \
    libgtk2.0-0 \
    libnotify4 \
    libxtst6 \
    libnss3 \
    python \
    gvfs-bin \
    xdg-utils \
    libcap2 \

    # Install X11 and ALSA dependencies so we can view (and hear?) the atom GUI
    libx11-xcb1 \
    libxss1 \
    libasound2 \
    libxkbfile1 \

    # Install jupyter's required build dependencies
    build-essential \
    python3-dev \
    python3-pip \

    # Get beta atom-amd64.deb release from https://atom.io/beta
    && curl -L -o atom-beta-amd64.deb https://atom.io/download/deb?channel=beta \

    # Finally install the 'base' atom-amd64 beta-build
    && dpkg -i atom-beta-amd64.deb \
    && rm -f atom-beta-amd64.deb \

    # Install jupyterlab via pip3 https://github.com/jupyterlab/jupyterlab
    && pip3 install setuptools wheel \
    && pip3 install jupyterlab \
    && jupyter serverextension enable --py jupyterlab --sys-prefix \

    # Remove dev/build stuff as not needed anymore
    && apt-get remove -y \
    build-essential \
    python3-dev \

    # More purging
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Initiate atom-beta with user 'atom'
RUN useradd -d /home/atom -m atom
USER atom

# Setup atom directory for user 'atom'
RUN mkdir -p /home/atom/.atom
RUN chmod 755 /home/atom/.atom
RUN chown -R `whoami` /home/atom/.atom

# Using apm-beta to install hydrogen to /home/atom/.atom
RUN apm-beta install hydrogen

# Install apm packages to view ipynb notebooks
RUN apm-beta install nbviewer browser-plus

# Initiate Jupyter config and start Jupyter notebook service
RUN jupyter lab --generate-config --no-browser

# Fix 'No module named ipykernel_launcher' https://github.com/nteract/hydrogen/issues/730
RUN python3 -m ipykernel install --user

RUN jupyter kernelspec list --json

# Miscellaneous python packages to install for asyncio
RUN pip3 install aiohttp aioftp

# Scientific python libraries
RUN pip3 install \
    h5py \
    matplotlib \
    numpy \
    pandas \
    scikit-learn \
    scipy \
    xarray

# Setup command to start Jupyter Notebook server and atom-beta at launch
EXPOSE 8888
WORKDIR /home/atom
CMD { jupyter lab --no-browser --ip=0.0.0.0 & } ; atom-beta -f /home/atom/alp
