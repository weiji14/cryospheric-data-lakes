# Dockerfiles

### Notes
- Using [Debian](http://www.debian.org/) 10 Buster slim as our default docker base image
- See buster-slim tag at https://hub.docker.com/r/_/debian/
- Rationale:
  - Why Buster and not Stretch? This PhD began around late June 2017, after Debian 9 Stretch became stable. Debian 10 Buster should move from testing to stable around the end of this PhD so this seemed the best environment to develop in for medium-term future reproducibility's sake.
  - Why Buster and not Alpine? Partly because I'm more familiar with apt-get (ok, not a good reason), but also because Alpine's fast paced development might be a bit too unstable. Then again, I do like to go a bit bleeding edge, but need to stop myself here.
  - Why Buster-slim and not Buster? Well, because of size issues of course!
  - Why the contradiction in wanting smaller size but not Alpine? Now that my friend, I'll get to once I get deeper into the heavy development stages  :simple_smile:


### How to build docker image from Dockerfiles!

##### Pre-requisites:
- Refer to the [official docs](https://docs.docker.com/engine/reference/builder/)
- You have [docker](https://www.docker.com/) installed!!
- Ideally, you have also configured yourself to be in the [dockers](https://docs.docker.com/engine/installation/linux/linux-postinstall/#manage-docker-as-a-non-root-user) group, otherwise use `sudo docker` instead of `docker`.

##### Build Example:
Below are the code you can use to build the python3/atom-beta docker images, assuming that your terminal's current working directory is in ../code/docker:

`cd ~/path/to/antarctic-lakes-phd/code/docker`

`docker build -f python3/Dockerfile -t icepy3 .`

`docker build -f atom-hydrogen-beta/Dockerfile -t ahb .`


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


##### Post-build steps:

###### Python3

Try running a python command from your terminal using the docker image you just built

    $ docker run --rm icepy3 python3 -c "print('Hello World')"

    Hello World

    $ docker run --rm icepy3 python3 -c "import sys; print(sys.version)"

    3.5.3+ (default, Jun  7 2017, 23:23:48)
    [GCC 6.3.0 20170516]

##### Atom

To open up the atom-beta editor environment, assuming that your terminal's current working directory is in ../code/docker

    $ docker run -d -v /tmp/.X11-unix/:/tmp/.X11-unix/
                    -v /dev/shm:/dev/shm
                    -v `dirname "$PWD"`:/home/atom/code
                    -e DISPLAY
                    ahb atom-beta -f

If you have your own atom editor and want to use your own configurations from your /home/user/.atom folder, do:

    $ docker run -d -v /tmp/.X11-unix/:/tmp/.X11-unix/
                    -v /dev/shm:/dev/shm
                    -v ${HOME}/.atom:/home/atom/.atom
                    -e DISPLAY
                    ahb atom-beta -f


##### Something's messed up and you want to clean up stuff:

Check what docker images you have now by running

`docker images -a`

To remove the specified docker image from your machine

`docker rmi <imagename>`

Remove all docker images from your machine (**careful!!**)

`docker rmi $(docker images -q)`

To force remove all docker images (**be very very careful!!**)

`docker rmi -f $(docker images -q)`

P.S. If you're a bit lazy in doing the build yourself, you could try to pull it from docker hub directly
