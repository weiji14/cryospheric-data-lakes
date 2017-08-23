FROM debian:buster-slim
LABEL maintainer "https://github.com/weiji14"
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Setup base atom-beta install
RUN apt-get -qq update && apt-get install -y --no-install-recommends \
    # Install atom required dependencies
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

    # Install wget, ca-certificates
    wget \
    ca-certificates \

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
    && wget --no-verbose https://atom.io/download/deb?channel=beta -O atom-beta-amd64.deb \

    # Finally install the 'base' atom-amd64 beta-build
    && dpkg -i atom-beta-amd64.deb \
    && rm -f atom-beta-amd64.deb \

    # Install jupyter via pip3
    && pip3 install setuptools wheel \
    && pip3 install jupyter \

    # Remove dev/build stuff as not needed anymore
    && apt-get remove -y \
    wget \
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
RUN jupyter notebook --generate-config --no-browser

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

# Setup script to start Jupyter Notebook server and atom-beta at launch
EXPOSE 8888
WORKDIR /home/atom
RUN echo "#!/bin/bash\n \
          jupyter notebook --no-browser --ip=0.0.0.0 &\n \
          jupyter notebook list\n \
          atom-beta -f /home/atom/alp" > start_script.sh
RUN chmod +x start_script.sh

# Configure container startup
#ENTRYPOINT ["tini", "--"]
CMD ["./start_script.sh"]

# Add Tini as late as possible to avoid cache busting
#ENV TINI_VERSION v0.15.0
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini tini
#RUN chmod +x tini
