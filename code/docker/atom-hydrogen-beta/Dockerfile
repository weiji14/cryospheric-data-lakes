FROM debian:buster-slim
LABEL maintainer "https://github.com/weiji14"
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install standard dependencies a la buildpack-deps curl https://hub.docker.com/_/buildpack-deps/
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Install python pip and setuptools
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    python3-pip \
    && pip3 install --no-cache-dir setuptools wheel \
    && rm -rf /var/lib/apt/lists/*

# Install Scientific python libraries a la scipy-notebook https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile
RUN pip3 install --no-cache-dir \
    dask[dataframe] \
    graphviz \
    h5py \
    matplotlib \
    numpy \
    pandas \
    scikit-learn \
    scipy \
    tables \
    xarray \
    && apt-get -qq update && apt-get install -y --no-install-recommends \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

# Install jupyterlab via pip3 https://github.com/jupyterlab/jupyterlab
RUN pip3 install --no-cache-dir \
    jupyterlab \
    && jupyter serverextension enable --py jupyterlab --sys-prefix

# Install jupyter widgets https://jupyter.org/widgets.html
RUN pip3 install --no-cache-dir ipyleaflet bqplot pythreejs ipyvolume \
    && jupyter nbextension enable --py --sys-prefix widgetsnbextension \
    && jupyter nbextension enable --py --sys-prefix ipyleaflet \
    && jupyter nbextension enable --py --sys-prefix bqplot \
    && jupyter nbextension enable --py --sys-prefix pythreejs \
    && jupyter nbextension enable --py --sys-prefix ipyvolume

# Install beta atom-amd64.deb release from https://atom.io/beta, plus X11 and ALSA dependencies
RUN curl -L -o atom-beta-amd64.deb https://atom.io/download/deb?channel=beta \
    && apt-get -qq update && apt-get install -y --no-install-recommends \
        ./atom-beta-amd64.deb \
        libx11-xcb1 \
        libxss1 \
        libasound2 \
        libxkbfile1 \
    && rm -f atom-beta-amd64.deb \
    && rm -rf /var/lib/apt/lists/*

# Initiate docker container with user 'atom'
RUN useradd -d /home/atom -m atom
USER atom

# Setup atom directory for user 'atom'
RUN mkdir -p /home/atom/.atom
RUN chmod 755 /home/atom/.atom
RUN chown -R `whoami` /home/atom/.atom

# Using apm-beta to install hydrogen to /home/atom/.atom
RUN apm-beta install hydrogen

# Install apm packages to view ipynb notebooks
RUN apm-beta install browser-plus

# Initiate Jupyter config and start Jupyter notebook service
RUN jupyter lab --generate-config --no-browser

# Fix 'No module named ipykernel_launcher' https://github.com/nteract/hydrogen/issues/730
RUN python3 -m ipykernel install --user

RUN jupyter kernelspec list --json

# Miscellaneous python packages to install
RUN pip3 install --no-cache-dir \
    aiohttp \
    aioftp

# Setup default command to launch at docker container startup
EXPOSE 8888
WORKDIR /home/atom
CMD { jupyter lab --no-browser --ip=0.0.0.0 & } ; atom-beta -f /home/atom/alp
