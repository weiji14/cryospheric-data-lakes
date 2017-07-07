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

    # Install jupyter build required dependencies
    build-essential \
    python3-dev \
    python3-pip \

    # Get beta atom-amd64.deb release from https://atom.io/beta
    && wget --no-verbose https://atom.io/download/deb?channel=beta -O atom-beta-amd64.deb \
    #&& wget --no-verbose https://atom.io/download/deb -O atom-stable-amd64.deb \

    # Finally install the 'base' atom-amd64 beta-build
    && dpkg -i atom-beta-amd64.deb \
    #&& dpkg -i atom-stable-amd64.deb \
    && rm -f atom-beta-amd64.deb \
    #&& rm -f atom-stable-amd64.deb \

    # Install jupyter via pip3
    && pip3 install setuptools wheel \
    && pip3 install jupyter \
    #&& pip3 install notebook

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

# Setup atom directory
RUN mkdir -p /home/atom/.atom
RUN chmod 775 /home/atom/.atom
RUN chown -R `whoami` /home/atom/.atom

# Using apm-beta to install hydrogen to /home/atom/.atom
RUN apm-beta install hydrogen
#RUN apm install hydrogen

# Initiate Jupyter config and start Jupyter notebook service
RUN jupyter notebook --generate-config --no-browser

# Fix 'No module named ipykernel_launcher' https://github.com/nteract/hydrogen/issues/730
RUN python3 -m ipykernel install --user

RUN jupyter kernelspec list --json

# Miscellaneous python packages to install for asyncio
RUN pip3 install aiohttp aioftp

# Fancy libraries for my python work
RUN pip3 install tqdm

#ENTRYPOINT ["/usr/bin/atom-beta","-f"]
