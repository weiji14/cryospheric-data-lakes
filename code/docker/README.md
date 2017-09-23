# Dockerfiles

## Docker image list

#### Main
- [x] [atom-hydrogen-beta](https://atom.io/)
- [x] [jupyter-lab](https://github.com/jupyterlab/jupyterlab)
- [x] [python3](https://www.python.org)

#### Maybes
- [ ] [Generic Mapping Tools (GMT)](http://gmt.soest.hawaii.edu/)
- [ ] [Broadview Radar Altimetry Toolbox (BRAT)](https://github.com/BRAT-DEV/main)
- [ ] [CryoSat User Tool (CUT)](https://earth.esa.int/web/guest/-/cryosat-user-tool-7386)
- [ ] [CryoSat Matlab routines](https://earth.esa.int/web/guest/-/cryosat-matlab-routines)

## Notes
- Using [Debian](http://www.debian.org/) 10 Buster slim as our default docker base image
- See buster-slim tag at https://hub.docker.com/r/_/debian/
- Rationale:
  - Why Buster and not Stretch? This repo began around late June 2017, after Debian 9 Stretch became stable. Debian 10 Buster should move from testing to stable around the finalization of this project so this seemed the best environment to develop in for medium-term future reproducibility's sake.
  - Why Buster and not Alpine? Partly because I'm more familiar with apt-get (ok, not a good reason), but also because Alpine's fast paced development might be a bit too unstable. Then again, I do like to go a bit bleeding edge, but need to stop myself here.
  - Why Buster-slim and not Buster? Well, because of size issues of course!
  - Why the contradiction in wanting smaller size but not Alpine? Now that my friend, I'll get to once I get deeper into the heavy development stages  :simple_smile:

## How to build docker image from Dockerfiles!

### Pre-requisites:
- Refer to the [official docs](https://docs.docker.com/engine/reference/builder/)
- You have [docker](https://www.docker.com/) installed!!
- Ideally, you have also configured yourself to be in the [dockers](https://docs.docker.com/engine/installation/linux/linux-postinstall/#manage-docker-as-a-non-root-user) group, otherwise use `sudo docker` instead of `docker`.

### Build Example:
Below are the code you can use to build the python3/atom-beta docker images, assuming that your terminal's current working directory is in ../code:

`cd ~/path/to/antarctic-lakes-phd/code`

`docker build -f docker/python3/Dockerfile -t icepy3 .`

`docker build -f docker/jupyter-lab/Dockerfile -t jlab .`

`docker build -f docker/atom-hydrogen-beta/Dockerfile -t ahb .`


Example output for building the python3 image,:

    Sending build context to Docker daemon   5.12kB
    Step 1/5 : FROM debian:buster-slim
    buster-slim: Pulling from library/debian
    a6cddc8d20af: Pull complete
    Digest: sha256:e52faaaab74faf91a7a0933ab310e3bcb41d4c321ffde373dae7066186f607f5
    Status: Downloaded newer image for debian:buster-slim
     ---> b57f4b324200
    Step 2/5 : LABEL maintainer "https://github.com/weiji14"
     ---> Running in 64c083030ef5
     ---> b5483e944092
    Removing intermediate container 64c083030ef5
    Step 3/5 : ENV LANG C.UTF-8 LC_ALL C.UTF-8
     ---> Running in aced65e22df8
     ---> f688c1dfeedb
    Removing intermediate container aced65e22df8
    Step 4/5 : RUN apt-get -qq update && apt-get install -y --no-install-recommends        python    python-dev    python-pip    git
     ---> Running in 3a6d0c4670a6
    Reading package lists...
    Building dependency tree...
    Reading state information...
    The following additional packages will be installed:
      .
      .
      .
    done.
     ---> a0088c18fca6
    Removing intermediate container 3a6d0c4670a6
    Step 5/5 : CMD python
     ---> Running in 08fd54f49b0d
     ---> 394b9c199adb
    Removing intermediate container 08fd54f49b0d
    Successfully built 394b9c199adb
    Successfully tagged icepy3:latest


### Post-build steps:

#### [Python3](https://www.python.org)

Try running a python command from your terminal using the docker image you just built

    $ docker run --rm icepy3 python3 -c "print('Hello World')"

    Hello World

    $ docker run --rm icepy3 python3 -c "import sys; print(sys.version)"

    3.5.3+ (default, Jun  7 2017, 23:23:48)
    [GCC 6.3.0 20170516]


#### [Jupyter Lab](https://github.com/jupyterlab/jupyterlab)

To start the jupyter lab server, assuming that your terminal's current working directory is in ../code

    $ docker run --rm -p 8888:8888                        `#Map port 8888 for Jupyter` \
                  -v `dirname "$PWD"`:/home/atom/alp      `#Set working directory` \
                  jlab                                    `#Run jupyter lab`

There will be many lines printed out, and you will see an output similar to this at the end :

    Copy/paste this URL into your browser when you connect for the first time, to login with a token:
        http://0.0.0.0:8888/?token=2151518272a8eeff0f37b2488f09e22cc85ed8adcb1e1d3c

Do what it says, by copying that link and pasting it into your own host browser (e.g. Firefox/Chrome/etc). You may have to try an address like http://localhost:8888/ instead in some cases.

If port 8888 is taken, change the `docker run` command to use a higher port number e.g. `-p 8889:8888`. You would then access jupyter lab a url like http://localhost:8889/.


#### [Atom](https://atom.io/)

To open up the atom-beta editor environment, assuming that your terminal's current working directory is in ../code

    $ docker run --rm -p 8888:8888                        `#Map port 8888 for Jupyter` \
                      -v /tmp/.X11-unix/:/tmp/.X11-unix/  `#X11 forwarding` \
                      -v /dev/shm:/dev/shm                `#ALSA forwarding` \
                      -v `dirname "$PWD"`:/home/atom/alp  `#Set working directory` \
                      -e DISPLAY                          `#Tell docker to display` \
                      ahb                                 `#Run atom-beta`

If nothing seems to happen, you may need to allow access to the X Server from other hosts using a tool like xhost (see [here](https://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-docker-container#comment65709322_25168483)). Try running `xhost +local:`, then re-run the command above.


If you have your own atom editor and want to use your own configurations from your /home/user/.atom folder, do:

    $ docker run --rm -p 8888:8888                        `#Map port 8888 for Jupyter` \
                      -v /tmp/.X11-unix/:/tmp/.X11-unix/  `#X11 forwarding` \
                      -v /dev/shm:/dev/shm                `#ALSA forwarding` \
                      -v ${HOME}/.atom:/home/atom/.atom \ `#Personalized .atom config` \
                      -v `dirname "$PWD"`:/home/atom/alp  `#Set working directory` \
                      -e DISPLAY                          `#Tell docker to display` \
                      ahb                                 `#Run atom-beta`

To set up an alias you can run directly from the command-line, or pin to your Linux taskbar/dock:

    $ alias alp-atom='cd path/to/antarctic-lakes-phd/code/ && \
            docker run --rm -p 8888:8888                        `#Map port 8888 for Jupyter` \
                            -v /tmp/.X11-unix/:/tmp/.X11-unix/  `#X11 forwarding`  \
                            -v /dev/shm:/dev/shm                `#ALSA forwarding` \
                            -v `dirname "$PWD"`:/home/atom/alp  `#Set working directory` \
                            -e DISPLAY                          `#Tell docker to display` \
                            ahb                                 `#Run atom-beta`

    $ alp-atom     `#This single statement now runs the above code directly :woohoo:`

Note that the alias only applies for your current login session, to make it permanent, add the "alias alp-atom ... " code block to the end of your ~/.bashrc file, or create a [~/.bash_aliases](https://askubuntu.com/questions/17536/how-do-i-create-a-permanent-bash-alias/17537#17537) file and put it in there.

**BONUS**: Once you launch the docker container, you can also access a [Jupyter Lab](https://github.com/jupyterlab/jupyterlab) IDE-like environment either through your own host browser at http://localhost:8888/ or http://0.0.0.0:8888/. You can also open it inside of Atom using `Ctrl+Shift+P` and typing `Browser Plus: Open`. The token code can be copied from the terminal where you executed the `docker run` statement.

For Windows users wanting to try out this docker atom build, you can do so using MobaXterm (see [here](https://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-docker-container/36190462#36190462)). I recommend installing it using [choco](https://chocolatey.org/) from an elevated command shell.

    > choco install mobaxterm

After that, start MobaXterm, configure X server: Settings -> X11 (tab) -> set X11 Remote Access to full, and then you can do:

    > cd ../
    > echo %cd%

    D:\path\to\top-level-directory

    > docker run --rm -p 8888:8888 -v "%cd%:/home/atom/alp" -e DISPLAY=10.64.66.107:0.0 ahb

The display IP address you should use can be found in MobaXterm if you click on 'Start local terminal'.

Animated instructions:

![mobaxterm_atom](https://user-images.githubusercontent.com/23487320/28297702-77686926-6bc3-11e7-9ff1-bd9b73f85c44.gif)

Alternatively, you can try using Xming (see [here](https://github.com/moby/moby/issues/8710#issuecomment-135109677)). Again, I recommend installing it using [choco](https://chocolatey.org/) from an elevated command shell.

    > choco install xming
    > "C:\Program Files (x86)\Xming\Xming.exe" :0 -multiwindow -clipboard -ac

Then you can do:

    > docker run --rm -p 8888:8888 -v "%cd%:/home/atom/alp" -e DISPLAY=10.0.75.1:0 ahb

Useful guide on how it should look like if it works:

https://medium.com/@cswiggz/quick-start-to-tensorflow-in-docker-with-a-gui-39414245251f

If you hit an error `Gtk: cannot open display: 10.0.75.1:0.0`, welcome to my world :)

### Something's messed up and you want to clean up stuff:

General cleanup methods:

    docker images -a          #Check what docker images you have now by running`

    docker container prune    #Remove all stopped containers

    docker rmi <imagename>    #To remove the specified docker image from your machine



Forceful cleanup methods (**careful!!**):

    docker rmi $(docker images -q)     #Remove all docker images from your machine

    docker rmi -f $(docker images -q)  #Force remove all docker images (be very very careful!!)

P.S. If you're a bit lazy in doing the build yourself, you could try to pull it from docker hub directly

###### TODO
