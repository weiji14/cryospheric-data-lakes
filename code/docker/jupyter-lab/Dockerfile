FROM debian:buster-slim
LABEL maintainer "https://github.com/weiji14"
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install standard dependencies a la buildpack-deps curl https://hub.docker.com/_/buildpack-deps/
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Initiate docker container with user 'atom'
ENV USER=atom
ENV HOME=/home/$USER
RUN useradd -d $HOME -m $USER

# Install bzip2 as root which is required for miniconda installation
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
        bzip2 \
    && rm -rf /var/lib/apt/lists/*

USER $USER

# Install miniconda3 a la https://github.com/jupyter/docker-stacks/blob/master/base-notebook/Dockerfile
RUN curl -L -o ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && /bin/bash ~/miniconda.sh -b -p $HOME/miniconda3 \
    && rm ~/miniconda.sh \
    && $HOME/miniconda3/bin/conda config --system --prepend channels conda-forge \
    && $HOME/miniconda3/bin/conda update --all --yes \
    && $HOME/miniconda3/bin/conda clean -tipsy

ENV PATH=$HOME/miniconda3/bin:$PATH

# Install Scientific python libraries a la scipy-notebook https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile
RUN pip install --no-cache-dir \
    dask[dataframe] \
    h5py \
    matplotlib \
    numpy \
    pandas \
    scikit-learn \
    scipy \
    tables \
    xarray

# Install jupyterlab https://github.com/jupyterlab/jupyterlab
RUN conda install -y -c conda-forge \
    jupyterlab \
    && conda clean -tipsy

# Install plotting libraries
RUN conda install -y -c conda-forge \
    -c bokeh \
    -c ioam \
        datashader \
        geoviews \
        holoviews \
        python-graphviz \
    && conda clean -tipsy

# Using conda 4.4.0 from conda-canary https://github.com/conda/conda/blob/d4f0bd4ee9af42d3e72c65d690ed83a9cb6aad0f/CHANGELOG.md#440-unreleased
#RUN conda install -y -c conda-canary conda

USER root

# Make graphviz work
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
        graphviz \
    && rm -rf /var/lib/apt/lists/*

USER $USER

# Miscellaneous python packages to install
RUN pip install --no-cache-dir \
    aiohttp \
    aioftp

# Setup default command to launch at docker container startup
EXPOSE 8888
WORKDIR /home/atom
CMD jupyter lab --no-browser --ip=0.0.0.0
