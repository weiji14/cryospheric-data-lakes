FROM debian:buster-slim
LABEL maintainer "https://github.com/weiji14"
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install standard dependencies a la buildpack-deps curl https://hub.docker.com/_/buildpack-deps/
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Install python pip
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Scientific python libraries a la scipy-notebook https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile
RUN pip3 install --no-cache-dir \
    h5py \
    matplotlib \
    numpy \
    pandas \
    scikit-learn \
    scipy \
    xarray

# Install jupyterlab via pip3 https://github.com/jupyterlab/jupyterlab
RUN pip3 install --no-cache-dir setuptools wheel \
    && pip3 install --no-cache-dir jupyterlab \
    && jupyter serverextension enable --py jupyterlab --sys-prefix

# Install jupyter widgets https://jupyter.org/widgets.html
RUN pip3 install --no-cache-dir ipyleaflet bqplot pythreejs ipyvolume \
    && jupyter nbextension enable --py --sys-prefix widgetsnbextension \
    && jupyter nbextension enable --py --sys-prefix ipyleaflet \
    && jupyter nbextension enable --py --sys-prefix bqplot \
    && jupyter nbextension enable --py --sys-prefix pythreejs \
    && jupyter nbextension enable --py --sys-prefix ipyvolume

# Initiate docker container with user 'atom'
RUN useradd -d /home/atom -m atom
USER atom

# Miscellaneous python packages to install
#RUN pip3 install --no-cache-dir \
#    aiohttp \
#    aioftp

# Setup default command to launch at docker container startup
EXPOSE 8888
WORKDIR /home/atom
CMD jupyter lab --no-browser --ip=0.0.0.0
