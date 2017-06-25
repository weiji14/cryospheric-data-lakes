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

    # Install X11 and ALSA dependencies so we can view (and hear?) atom
    libx11-xcb1 \
    libxss1 \
    libasound2 \
    libxkbfile1 \

    # Get beta atom-amd64.deb release from https://atom.io/beta
    && wget --no-verbose https://atom.io/download/deb?channel=beta -O atom-amd64.deb \

    # Finally install the 'base' atom-amd64 beta-build
    && dpkg -i atom-amd64.deb \
    && rm -f atom-amd64.deb \

    # Remove wget as not needed anymore
    && apt-get remove -y \
    wget \

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

#ENTRYPOINT ["/usr/bin/atom-beta","-f"]
