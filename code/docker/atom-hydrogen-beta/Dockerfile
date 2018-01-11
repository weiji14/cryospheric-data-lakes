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

# Using conda 4.4.0 from conda-canary https://github.com/conda/conda/blob/d4f0bd4ee9af42d3e72c65d690ed83a9cb6aad0f/CHANGELOG.md#440-unreleased
RUN conda install -y -c conda-canary conda

# Install Scientific python libraries a la scipy-notebook https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile
# Install jupyterlab https://github.com/jupyterlab/jupyterlab
# Install big data, geospatial and plotting libraries
RUN conda install -y -c \
        dask-core \
        h5py \
        matplotlib \
        numpy \
        pandas \
        scikit-learn \
        scipy \
        pytables \
        xarray \
        jupyterlab \
        fastparquet \
        geopandas \
        bokeh::datashader \
        ioam::geoviews \
        ioam::holoviews \
        python-graphviz \
        python-snappy \
    && conda clean -tipsy

# Miscellaneous python packages to install
RUN pip install --no-cache-dir \
    aiohttp \
    aioftp

USER root

# Make graphviz work
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
        graphviz \
    && rm -rf /var/lib/apt/lists/*

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

# Install TeX Live
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
        lmodern \
        texlive \
    && rm -rf /var/lib/apt/lists/*

USER $USER

# Setup atom directory for user 'atom'
RUN mkdir -p $HOME/.atom
RUN chmod 755 $HOME/.atom
RUN chown -R `whoami` $HOME/.atom

# Using apm-beta to install hydrogen to $HOME/.atom
RUN apm-beta install hydrogen

# Using apm-beta to install Markdown-preview-enhanced (primarily for Pandoc/LaTeX PDF export)
RUN apm-beta install markdown-preview-enhanced

# Initiate Jupyter config and start Jupyter notebook service
RUN jupyter lab --generate-config --no-browser

# Fix 'No module named ipykernel_launcher' https://github.com/nteract/hydrogen/issues/730
RUN python3 -m ipykernel install --user

RUN jupyter kernelspec list --json

# Setup default command to launch at docker container startup
EXPOSE 8888
WORKDIR $HOME
CMD { jupyter lab --no-browser --ip=0.0.0.0 & } ; atom-beta -f $HOME
