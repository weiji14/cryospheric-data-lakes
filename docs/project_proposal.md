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
keywords: Antarctica, big data, deep learning, convolutional neural networks, computer vision
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
On the hardware front, we make use of Graphical Processing Units (GPUs) where possible to speed up our neural network model's calculations [see @SteinkrausUsingGPUsmachine2005].
On the software front, parallel implementations of algorithms and self learning artificial intelligence modules offer us a similar speed up advantage in analyzing the data.
Taken together, these increases result in several magnitude orders of improved runtime efficiencies, allowing us to scale alongside the volumes of data being collected to analyze.
Keeping up with these technological improvements will allow for more experimental iterations even as our data repository size grows, thus improving our chances of uncovering groundbreaking discoveries within a reasonable amount of time.

## Previous work

### Subglacial lake inventories



### Convolutional Neural Networks

Convolutional Neural Networks have existed since @LeCunBackpropagationAppliedHandwritten1989, and have been shown to outperform pattern recognition tasks [e.g. @LecunGradientbasedlearningapplied1998].

There are many ways to classify different Convolutional Neural Network (ConvNet) architectures, but for the purposes of our subglacial lake detection exercise which is of one object class type, we can focus on the degree to which the boundaries of the lake can be segmented.
In order of increasing complexity, we can present pattern recognition problems as one of:

- Image Classification (e.g. @LecunGradientbasedlearningapplied1998; @SimonyanVeryDeepConvolutional2014; @KrizhevskyImageNetclassificationdeep2017)
- Object Localization (e.g. @GirshickRichfeaturehierarchies2013; @GirshickFastRCNN2015; @RenFasterRCNNRealTime2015; @RedmonYouOnlyLook2015; @RedmonYOLO9000BetterFaster2016)
- Object Segmentation (e.g. @LongFullyConvolutionalNetworks2014; @RonnebergerUNetConvolutionalNetworks2015; @JegouOneHundredLayers2016; @HeMaskRCNN2017).

Note that these three different ConvNet classes relate to the output node of the ConvNet and not the architectural complexity or depth of the ConvNet's hidden layers.
It can be argued however, that an object segmentation ConvNet would require a more specialized architecture with more layers than an image classification ConvNet.

For the Object Localization class of ConvNets, we can identify two broad family groups.
The Region-based family of R-CNN ConvNets such as R-CNN [@GirshickRichfeaturehierarchies2013], Fast-RCNN [@GirshickFastRCNN2015], and Faster R-CNN [@RenFasterRCNNRealTime2015] involves a two-step pipeline that first divides an image into regions before running a classifier algorithm on those regions to output bounding boxes.
The Regression-based family of ConvNets such as YOLO [@RedmonYouOnlyLook2015], Multibox SSD [@LiuSSDSingleShot2015], and YOLOv2 [@RedmonYOLO9000BetterFaster2016] takes a unified approach with a single neural network that simultaneously predicts bounding boxes and class probabilities.
While state-of-the-art regression-based ConvNets such as YOLOv2 [@RedmonYOLO9000BetterFaster2016] tend to be faster and more capable as real-time object detection systems, they present a tradeoff in accuracy when compared to region-based ConvNets like Faster-RCNN [@RenFasterRCNNRealTime2015], especially if they are trained on fewer examples or tasked with identifying smaller objects [@HuangSpeedaccuracytradeoffs2016; @XiaDOTALargescaleDataset2017].

For the Object Segmentation class of ConvNets, we can describe the evolution of this class from a basic Fully Convolutional Network to one that has been extended with multiple skip-connections.
Fully Convolutional Networks are neural networks without the fully connected layers seen in regular deep feedforward neural networks.
Their fully convolutional-based nature allows input images of any arbitrary size and preserves spatial information [@LongFullyConvolutionalNetworks2014].
The U-Net architecture is an implementation of this Fully Convolutional Network that has a symmetric contracting and expanding path, and it has been applied successfully to the field of biomedicine [@RonnebergerUNetConvolutionalNetworks2015] and remote sensing [e.g. @LiDeepUNetDeepFully2017; @ZhangRoadExtractionDeep2017; @ZhuDeepLearningRemote2017].
By using DenseNets [@HuangDenselyConnectedConvolutional2016] which are an extension of ResNets [@HeDeepResidualLearning2015], Fully Convolutional Networks can be made even deeper while maintaining a reasonable number of parameters to obtain better image segmentation results [@JegouOneHundredLayers2016].

Although many new ConvNet developments appear regularly in this fast moving computer vision field, the basic mechanics of convolutional and pooling layers are still well established elements present in most of the papers listed above.
That said, there are other architectural advances to keep note of which challenge important components of ConvNet architectures.
Some promising experimental work has been done to replace the convolutional and pooling layers of a ConvNet with an Recurrent Neural Network (RNN)-based alternative [@VisinReNetRecurrentNeural2015; @VisinReSegRecurrentNeural2015], or even supplement ConvNets with RNNs when applying them to higher dimensional datasets such as 3D point clouds [@Liu3DCNNDQNRNNDeepReinforcement2017] or multi-temporal remote sensing datasets [@MinhDeepRecurrentNeural2017; @IencoLandCoverClassification2017].
Atrous or Dilated Convolutions are another development that allows us to enlarge the field of view of filters for deeper layers while preserving spatial resolution [@ChenDeepLabSemanticImage2016; @ChenRethinkingAtrousConvolution2017; @ZhangProgressivelyDiffusedNetworks2017; @YuDilatedResidualNetworks2017; @ZhangImageSegmentationPyramid2017].
Futhermore, we have Capsule Networks (CapsNet) which can preserve detailed spatial position and pose information of objects in an equivariant manner, overcoming the limitations of maxpooling layers that can only handle object invariance [@SabourDynamicRoutingCapsules2017].

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

### Convolutional Neural Network

Given an input of a multi-dimensional image of Antarctica, the goal of our subglacial lake identification project would be to determine each location of our lake.
Training an image classification ConvNet, specifically a binary image classifier, would tell us if a region of interest does or does not contain a lake. With an object localization classifier, it may output a bounding box which gives us a better answer. Finally for an object segmentation classifier, the exact boundaries of a lake can be probabilitically determined down to each geographical pixel.

Our proposed ConvNet architecture will be as follows:






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
