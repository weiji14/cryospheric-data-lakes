---
documentclass: article
title: |
  | Deep lakes with deep networks:
  | An integrated deep convolutional neural network approach to reveal subglacial lakes and their channel networks from multiple open remote sensing datasets in Antarctica.
  |
  | PhD Proposal in Physical Geography
author: Wei Ji Leong
institute: |
  | Antarctic Research Centre
  | Victoria University of Wellington
output: pdf_document
#toc: true
date: \today
export_on_save:
  pandoc: true
colorlinks: true
bibliography: bibliography.bib
csl: apa.csl
---

# Abstract


\newpage
# Topic Development

## Background
With the exponentially increasing amount of remotely sensed geophysical data being generated every day for Antarctica, there lies an immense potential in answering many of the outstanding and urgent questions that this continent refuses to yield.
Here we propose a novel deep learning based approach to discover features, specifically subglacial lakes and their networked channels, that may have escaped detection from the custom-built data analysis methods that is standard for generations trained prior to the deep learning era.

This approach aims to more fully utilize openly available datasets, with the goal of uncovering discoveries that each individual dataset alone would not have confidently yielded.
At first glance, the large amount and varied formats of the datasets presents many challenges to researchers, from the very basic management of the data volume itself to the specialized task of logically interpreting the data within set realms of scientific uncertainty.
For us, we introduce another layer of complexity by attempting to combine such specialized cross-disciplinary datasets though the use of geographical frameworks and state of the art data science practices.

From first principles, we assert that an exponential rise in the amount of data necessitates the use of exponentially growing technologies, so that the amount of value generated from the data per unit time can increase proportionately.
To tackle this, we adhere ourselves to an automated data processing workflow that is as reproducible as possible, down to the very copies of the software and data used.
On the hardware front, we make use of Graphical Processing Units (GPUs) where possible to speed up our neural network model's calculations.
On the software front, parallel implementations of algorithms and self learning artificial intelligence modules offer us a similar speed up advantage in analyzing the data.
Taken together, these increases result in several magnitude orders of improved runtime efficiencies, allowing us to scale alongside the volumes of data being collected to analyze.
Keeping up with these technological improvements will allow for more experimental iterations even as our data repository size grows, thus improving our chances of uncovering groundbreaking discoveries within a reasonable amount of time.

## Previous work

Mention previous studies in this field.



# Proposed Research

## Research questions

## Geographical setting

We narrow the geographical extent of our study down to the Antarctic continent, lying South of latitude 60 degrees South.
As our focus is on finding the presence of subglacial lakes and their networked channels, this further restricts our geographical study area to the grounded portion of the Antarctic Ice Sheet, anywhere South of the grounding line.

Note that the grounding line is a dynamic boundary that can change considerably over time.
We refrain ourselves however, from setting a strict temporal extent filter on data (e.g. less than a decade timeframe) that allows assumptions of an arbitrary stasis baseline to be made, at the expense of excluding potentially useful datasets.
We assume that our deep neural networks will work better with more messy data than a restricted set of clean data, and that the model will learn to account for the various idiosyncrasies of the datasets it is trained on.

## Datasets

The data for our study will include, but is not limited to, satellite-based datasets (e.g. ICESAT, CryoSat) supplemented by derived products (e.g. BEDMAP2) and data from airborne geophysical missions (e.g. Operation Icebridge). Subglacial lake boundary training data will use information from published inventories, and there will be some scope for additiional field data collection for groundtruthing purposes.

### Geophysical data

- ICESAT - LiDAR
- CryoSat - Radar
- BEDMAP2 - Mixture

### Training data

- Smith lakes [@Smithinventoryactivesubglacial2009]
- 4th Inventory [@WrightfourthinventoryAntarctic2012]



# Data Science Workflow

## Reproducible software environment

### Containers - Docker

A huge part of this data-driven research relies on the software environment.
The task of setting up a computational environment can be a non-trivial task, but once it is done, that exact software environment should be made available across any computer, and produce the same results given the same data input.

Docker (https://www.docker.com) is one such lightweight containerization technology that resolves issues related to "Dependency Hell", imprecise documentation, code-rot and barriers to reuse by creating a packaged binary image of the exact software environment down to the operating system level [@BoettigerintroductionDockerreproducible2015].

Essentially, it simplifies the management of complex computational environments, through the use of a 'Dockerfile' which encodes how the environment is to be built from the ground up, starting from a base operating system image, up to the very commands used to install or compile the various software packages.
Once built, the binary docker image itself can be frozen or packaged up, and shared across collaborators, providing them with a hardware-agnostic and platform-agnostic replica of the software stack used to by to run the author's work.

Docker's open-source, cross-platform and lightweight nature makes it an attractive choice amongst scientists, but its requirement for administrative level privileges to run does pose issues for users without such rights, such as those working in high performance computing cluster environments [@SilverSoftwaresimplified2017].
For more advanced use-cases, like ours here requiring the use of specialized NVIDIA GPU hardware, additional effort may required to leverage the benefits of docker containerization, notably through the nvidia-docker (https://github.com/NVIDIA/nvidia-docker) package that tries to maintain reproducibility across different NVIDIA host drivers, albeit at a cost of restricting support to GNU/Linux platforms.

### Virtual environments - Conda

The fast moving pace of the data science ecosystem is not easy to keep track of.
The field is constantly refreshing itself, with new programming languages, tools and frameworks being created so regularly that managing all these complex components is a job in itself.
Although docker containers can act as a gold standard for ensuring reproducibility, there are restrictions in its use (see previous section).
Indeed, there is a big time penalty involved from setting up a docker environment, to the build of the container image from scratch, especially for someone who just wants to use the computing resources they have at hand as quickly as possible.
This necessitates a tool that has less of an overhead, but still provides a good amount of isolation for reproducibility (see Fig. 1).

https://chdoig.github.io/pydata2015-dallas-conda/images/repro-3.png
https://chdoig.github.io/pydata2015-dallas-conda/#/4/3

Conda (https://conda.io/docs/) is a cross-platform tool for managing data science packages and environments.
It removes the issues of compiling packages and their dependencies as it packages binaries across Linux, Mac and Windows.
Conda environments can be created for individual projects, are isolated from other parts of a user's system, and can be recreated through a single plain-text 'environment.yml' file that lists all the packages within the environment, down to their exact version if required.

In a nutshell, conda manages to extend the ease of use of the pip Python package manager to multiple languages and operating system platforms.
Much of its value lies in the ability to quickly install a software package using conda to do some ad hoc analysis without messing with dependencies and compilers, and still maintain a degree of assurance that the environment can be reliably reproduced at another place.
While it is not quite as robust as a docker container, conda virtual environments trades off perfect reprobucibility with practicality as is usually the case during exploratory analysis stages when one is trying to see if something new will work.


## Version control system

### Source code management - Git

At its most primitive level, a source code version control system tracks changes made to files within a project repository.
This simple feature offers multiple benefits.
Timestamped snapshots of a project opens up individual changes to be audited, and allows trivial rollbacks to be performed to past backups in case of major mistakes.
A good version control system can also ensure the cryptographic integrity of a tracked project down to every bit, and enable finer collaboration between people who can interrogate the whole history.

Git (https://git-scm.com) is a version control system popular amongst  scientists, whose distributed nature ensures that every user has a full backup or 'clone' of the project to ensure fault tolerance, with an incredible branching system that supports a variety of non-linear research and development workflows.
Github (https://github.com) is one example of a fungible place to host git-tracked projects, with additional tools that facilitates collaboration between contributors by simplifying the sharing of code, and allowing issues to be tracked and discussed transparently alongside the source code [@BlischakQuickIntroductionVersion2016].

Although there is a learning curve associated with its unintuitive syntax, it has become the de facto standard for recording changes in line-orientated plain text files including source code, documentation written in Markdown or LaTeX, CSV files, and others.
However, it will not be as effective for binary formats such as in our big data science project, and indeed, there are known performance struggles with git handling large files (e.g. over 100 megabytes) or a huge number of files [@PerkelDemocraticdatabasesscience2016].

### Data management - Dat

Big data files present with it many challenges.
Data integrity issues can manifest itself anywhere during data download, storage, processing, and sharing.
Ideally, we require a means of ensuring the data we use and share is first and foremost consistent down to every bit.
Next, any changes made to the data need to be tracked and made evident, and the data must be able to be shared as quickly and securely as possible to each user in a non-centralized distributed manner.

Dat (https://datproject.org/) is a protocol designed to handle data, even if they are large or changing constantly [@OgdenDatDistributedDataset2018].
It features content integrity through the use of signed hashes, specifically BLAKE2b [@AumassonBLAKE2SimplerSmaller2013] to address content, with hashes arranged in a Merkle tree [@MykletunAuthenticationintegrityoutsourced2006] where each leaf node contain pieces of the actual dataset.
Access to the files are then shared through Dat links which are Ed25519 [@BernsteinHighspeedhighsecuritysignatures2012] public keys.

Binary datasets split and hashed into a Merkle tree pattern by Dat allow for small parts or minute changes to a large file to be shared individually, quickly and securely over the network in a decentralized manner.
Although Dat itself is still a relatively young technology, it has managed to combine the best parts of technologies such as Git, BitTorrent [TODO cite], Kademlia Distributed Hash Table [@MaymounkovKademliaPeertoPeerInformation2002] and others into a formidable product.
The reader is directed to @OgdenDatDistributedDataset2018 for the finer technical implementation details of the Dat protocol.
The current javascript-only implementation of this data transfer protocol presents some integration challenges into our Python heavy stack, but its features and philosophy align well with our project's goals of transparency and reproducibility, and it provides the most rigorous means of ensuring that our source and derived datasets can be stored, handled and moved around in the most cryptographically secure and verifiable way possible.

## Model development

### Data ingestion

With our highly reproducible and cryptographically secure version-control frameworks in place, we move on to the actual work of readying our data for feeding into our model.



# Preliminary Results



# Project framework

## Outline

## Timeline



# Budget and Resource Requirements

## Funding

## Training

## Hardware



# Summary

Methodology - we detail the setup of our intended data science pipeline.
For ensuring software and data reproducibility, we start from a well known and supported technological foundation (Docker and Git), supplemented by an emerging technological stack (Conda and Dat) that handles some of the known limitations of our base setup.
The solid foundation serves as a skeleton platform where we rest the more experimental and mutable parts of our data science project.
While each component is different, they are all open source projects with a fundamental respect for cryptographic integrity, ensuring that our data processing pipeline is of high integrity.



# References
