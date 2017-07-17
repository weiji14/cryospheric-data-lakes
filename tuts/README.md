# Tutorials

Some of the lessons I use to sharpen my tack. Stuff in this folder is meant to be messy, highly experimental, hard to follow and understand. I.e. probably not the place you should be looking at if you have better things to do.

### Notes to Self & Others

Most of the tutorials here are clones of git projects from various places implemented as git [submodules](https://github.com/blog/2104-working-with-submodules). If you cloned this entire repository using the normal `git clone` command as per the standard/default instructions [here](/README.md#cloning-the-repository), the tutorial files won't be downloaded (i.e. you won't see anything under tuts/subfolder). To get the full copy of everything in all its glory after you have cloned the core code:

    git submodule update --init --recursive

\*Repo owner note: submodules tutorials can be added by doing something like:

    git submodule add https://github.com/<repo username>/<tut name> tuts/<tut name>

## [nn-from-scratch](https://github.com/dennybritz/nn-from-scratch)

Neural Network from Scratch in Python by Denny Britz! Teaches us how implement a simple 3-layer neural network from scratch.

### Guides

- Blog post tutorial [here](http://www.wildml.com/2015/09/implementing-a-neural-network-from-scratch/),
- iPython/Jupyter notebook [here](https://github.com/dennybritz/nn-from-scratch/blob/master/nn-from-scratch.ipynb).

### Requires
- [matplotlib](https://github.com/matplotlib/matplotlib)
- [numpy](https://github.com/numpy/numpy)
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)
- [scipy](https://github.com/scipy/scipy)


## [scipy-2017-sklearn](https://github.com/amueller/scipy-2017-sklearn)

Scipy 2017 scikit-learn tutorial by Alex Gramfort and Andreas Mueller. Walkthrough of scikit-learn.

### Guides

- Youtube video [here](https://www.youtube.com/watch?v=2kT6QOVSgSg),
- Introductory iPython/Jupyter notebook [here](https://github.com/amueller/scipy-2017-sklearn/blob/master/notebooks/01.Introduction_to_Machine_Learning.ipynb).

### Requires
- [matplotlib](https://github.com/matplotlib/matplotlib)
- [numpy](https://github.com/numpy/numpy)
- [pandas](https://github.com/pandas-dev/pandas)
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)
- [scipy](https://github.com/scipy/scipy)

## *Extra hint!*

Psst! If you look under [/code/docker/atom-hydrogen-beta](/code/docker/atom-hydrogen-beta), I will have already installed (or will strive to install very soon!) the dependency libraries inside of the Atom text editor, so you can use that as the development environment. The trick is to have **docker** installed first, full instructions can be found on the [main page](/).

![scipy_imp](https://user-images.githubusercontent.com/23487320/28257799-7ec2fbd4-6b21-11e7-9daf-d993f6b15578.gif)
