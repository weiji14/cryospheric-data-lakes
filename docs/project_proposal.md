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
geometry: margin=2.5cm
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
The standard convolution operation in a ConvNet can be factorized into a more efficient depth-wise separable convolution [@SifreRigidMotionScatteringImage2014] that consists of a channel-wise spatial convolution followed by a pointwise convolution.
This results in a lighter parameter footprint, making it less computationally expensive with only a slight accuracy loss [@HowardMobileNetsEfficientConvolutional2017], and enabling faster model convergence [@CholletXceptionDeepLearning2016]. Atrous or Dilated Convolutions are another development that allows us to enlarge the field of view of filters for deeper layers while preserving spatial resolution [@ChenDeepLabSemanticImage2016; @ChenRethinkingAtrousConvolution2017; @ZhangProgressivelyDiffusedNetworks2017; @YuDilatedResidualNetworks2017; @ZhangImageSegmentationPyramid2017].

Some promising experimental work have also been done to replace the convolutional and pooling layers of a ConvNet with an Recurrent Neural Network (RNN)-based alternative [@VisinReNetRecurrentNeural2015; @VisinReSegRecurrentNeural2015], or even supplement ConvNets with RNNs when applying them to higher dimensional datasets such as 3D point clouds [@Liu3DCNNDQNRNNDeepReinforcement2017] or multi-temporal remote sensing datasets [@MinhDeepRecurrentNeural2017; @IencoLandCoverClassification2017].
Futhermore, we have Capsule Networks (CapsNet) which can preserve detailed spatial position and pose information of objects in an equivariant manner, overcoming the limitations of maxpooling layers that can only handle object invariance [@SabourDynamicRoutingCapsules2017].

Well trained ConvNets can offer state of the art accuracy in classification tasks, but they have also inspired other interesting applications.
One such application is the Super-Resolution Convolutional Neural Network (SRCNN) which is a regression method used to increase the resolution of images [@DongImageSuperResolutionUsing2014], a technology that has since been applied to turn coarse resolution climate models to finer resolution ones via statistical downscaling with the addition of additional input channels, allowing us to capture climate patterns at local levels. [@VandalDeepSDGeneratingHigh2017].
In the art world, the neural representations learned by the intermediate layers of a ConvNet has also been used to tranfer the content and style from one artform to another [@GatysNeuralAlgorithmArtistic2015].

Given the empirical success of ConvNets, it has started to attract much more critical attention than ever and there is a growing movement to interpret the decision making process of such black box models.
On one hand, there are valid concerns for needing to improve interpretability arising from the advent of adversarial attacks which can make ConvNets output incorrect predictions a human would not make [@SzegedyIntriguingpropertiesneural2013].
These adversarial problems are part of the motivation for us to ensure that our proposed research project is end to end reproducible, starting from cryptographically securing the data we input into our ConvNet models.
On the other hand, having a rich grammar of interpretability starting from building blocks like feature visualization, attribution and dimensionality reduction can help us to derive more meaning from what a ConvNet sees [@OlahBuildingBlocksInterpretability2018], potentially leading to insights that can pave the way for more research avenues into the future.


# Proposed Research

## Research questions

## Geographical setting

We narrow the geographical extent of our study down to the Antarctic continent, lying South of latitude 60 degrees South.
As our focus is on finding the presence of subglacial lakes and their networked channels, this further restricts our geographical study area to the grounded portion of the Antarctic Ice Sheet, anywhere South of the grounding line.

Note that the grounding line is a dynamic boundary that can change considerably over time.
We refrain ourselves however, from setting a strict temporal extent filter on data (e.g. less than a decade timeframe) that allows assumptions of an arbitrary stasis baseline to be made, at the expense of excluding potentially useful datasets.
We assume that our deep neural networks will work better with more messy data than a restricted set of clean data, and that the model will learn to account for the various idiosyncrasies of the datasets it is trained on.

## Datasets

The deep learning models will require the use of Antarctic datasets with nearly full coverage of the continent.
For the supervised classification task, our input data will include stacked layers of gridded raster datasets, and these will be mapped to known output labels or masks of subglacial lake areas.
Input data for our study will include single-satellite digital terrain models (e.g. ICESAT, CryoSat), compiled products (e.g. BEDMAP2) and model outputs (e.g. MEASURES Ice flow speed).
Output data will come from published subglacial lake inventory collections.
For select regions of interest, we may source finer resolution data directly from airborne geophysical missions (e.g. Operation Icebridge) and there will be some scope for additional field data collection for groundtruthing purposes.

Our criteria for incorporating a dataset into the shortlist is prioritized based on factors like spatial resolution and whether they have the potential to be useful for our subglacial lake classification task.
Where data products of similar types are available, we tend to choose the latest version, keeping an older version only if it has some value not found in the newer version.
For example, we have two Digital Elevation Models (DEM), one from ICESAT data, and one from CryoSat-2 data, as even though the ICESAT DEM is older, it is of higher spatial resolution and also sourced from a laser altimeter compared to CryoSat-2's radar altimeter.

### Training data - Raster Arrays

|Type         | Sensor Type     | Name                    | Spatial Resolution | Literature Citation                          | Data Citation                            |
|:----------- |:----------------|:----------------------- | ------------------:|:-------------------------------------------- |:---------------------------------------- |
| Imagery     | Radar           | RAMP RADARSAT mosaic    |               100m | [@JezekGlaciologicalpropertiesAntarctic1999] | [@JezekRAMPAMM1SAR2013]                  |
| Imagery     | Multi-spectral  | MODIS MOA               |               125m | [@ScambosMODISbasedMosaicAntarctica2007]     | [@TerryHaranMODISMosaicAntarctica2014]   |
| Terrain     | Radar           | RAMP2 DEM               |               200m | [@JezekGlaciologicalpropertiesAntarctic1999] | [@LiuRadarsatAntarcticMapping2001]       |
| Terrain     | Laser Altimeter | GLAS/ICESat DEM         |               500m | [@ShumanICESatAntarcticelevation2006]        | [@DimarzioGLASICESat5002007]             |
| Terrain     | Radar Altimeter | CryoSat-2 DEM           |              1000m | [@HelmElevationelevationchange2014]          |                                          |
| Terrain     | Multiple        | BEDMAP2                 |              1000m | [@FretwellBedmap2improvedice2013]            |                                          |
| Glacio-logy | Radar           | MEASURES Ice flow speed |               450m | [@RignotIceFlowAntarctic2011;@MouginotMappingIceMotion2012] | [@RignotMEaSUREsInSARBasedAntarctica2017]
| Glacio-logy | Model           | Subglacial water flux   |              1000m | [@LeBrocqEvidenceiceshelves2013]             |                                          |
| Geo-physics | Magnetic        | Subglacial heat flux    |             15000m | [@MartosHeatFluxDistribution2017]            | [@MartosAntarcticgeothermalheat2017]     |
| Geo-physics | Gravity         | AntGG Gravity Anomaly   |             10000m | [@ScheinertNewAntarcticgravity2016]          | [@ScheinertAntarcticfreeaircomplete2016] |
| Geo-physics | Gravity         | SatGravRET2014          |             10000m | [@Hirtnewdegree2190102016]                   |                                          |

### Training data - Vector Labels

#### Subglacial Lake Inventories

| Vector Type | Name                                         | Count | Citation                              |
|:----------- |:-------------------------------------------- |:-----:|:------------------------------------- |
| Polygon     | Smith et al.                                 |  124  | [@Smithinventoryactivesubglacial2009] |
| Point       | Wright & Siegert                             |  379  | [@WrightfourthinventoryAntarctic2012] |

#### Individual Subglacial Lakes

| Vector Type | Name                                         | Count | Citation                              |
|:----------- |:-------------------------------------------- |:-----:|:------------------------------------- |
| Polygon     | Vostok Subglacial Lake                       |   1   | [@StudingerIcecoverlandscape2003]     |
| Polygon     | Recovery Subglacial Lakes                    |   4   | [@BellLargesubglaciallakes2007]       |
| Polygon     | Kamb Subglacial Lakes                        |   3   | [@KimActivesubglaciallakes2016]       |
| Polygon     | Thwaites Subglacial Lakes                    |   4   | [@SmithConnectedsubglaciallake2017]   |


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
While it is not quite as robust as a docker container, conda virtual environments trades off perfect reproducibility with practicality as is usually the case during exploratory analysis stages when one is trying to see if something new will work.

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

### Data preparation

With our highly reproducible and cryptographically secure version-control frameworks in place, we move on to the actual work of readying our data for feeding into our model.
The heterogeneous nature of our datasets presents some challenges, but the observation-level data fusion process can be structured as a step by step process consisting of data alignment and data correlation, otherwise known as matching and coregistration in remote sensing terminology [@SchmittDataFusionRemote2016].

Geographic data can be broadly classified into vector and raster datasets, with the former being more suitable for discrete datasets, and the latter more associated with continuous datasets.
For each spot on the surface, we will assemble all the sensor measurements available for that spot using locational attributes tied to the sensor data.
As we are interested in the continuous spatial variation of adjacent sensor measurements at any one spot, which may determine the presence or absence of subglacial features, we choose to employ the continuous raster format in our Geographic Information System (GIS).

Each data layer can be stacked together to create a multi-dimensional raster image that will feed into our computer vision model.
Conceptually, we can think of stacking multiple input feature layers in much the same way as stacking multiple bands in a multipectral optical satellite image.
In order to create the stack, we will first reproject each input layer to a common projected coordinate system - the Antarctic Polar Stereographic (EPSG:3031) which is a conformal projection system based on the WGS84 ellipsoid surface.

Next, each layer may need to be undergo further transformation so that the pixels are aligned across layers, either via a translational shift and/or resampling to a common spatial resolution.
For the resampling process, we may choose to use classical resampling techniques such as bilinear or bicubic interpolation, or a custom spline interpolation method.
Alternatively, it is also possible to employ Super-Resolution Convolutional Neural Network (SRCNN) to increase the spatial resolution of the raster [@DongImageSuperResolutionUsing2014].
For example, we can train an SRCNN to capture interdependencies with variables in the other layers to improve the reliability of the upscaling function [@VandalDeepSDGeneratingHigh2017], compared to a standard bicubic interpolation method which only looks at information from a single layer.

Once this is done, we will generate standardized square tiles of the stacked multi-layer raster.
Each tile will be centered on one subglacial lake polygon, and may contain more than one lake if lakes are found close to each other.
Thus, the number of training tiles would equal the number of lakes in our compiled subglacial lake inventory.

At this point, we will divide our dataset into a training set and cross-validation set.
The training set will be used to train our ConvNet model, while the cross-validation set will be used to evaluate the performance of that model across different hyperparameter settings.
Furthermore, we will also have a test set to independently verify our final model.
This test set will likely be generated from the data in the point-only subglacial lake inventory [@WrightfourthinventoryAntarctic2012].

As our training sample is very small, just over a hundred or so, we will also use data augmentation to virtually increase our training set.
Data augmentation will involve randomly tranforming our tiles, by any combination of the following: mirror image, vertical/horizontal shifts, rotation, shear warping, cropping, adding noise, etc.
Such data augmentations will reduce the likelihood of overfitting in our ConvNet model.

### Convolutional Neural Network

Given an input of a multi-dimensional image of Antarctica, the goal of our subglacial lake identification project would be to determine each location of our lake.
Training an image classification ConvNet, specifically a binary image classifier, would tell us if a region of interest does or does not contain a lake.
With an object localization classifier, it may output a bounding box which gives us a better answer.
Finally for an object segmentation classifier, the exact boundaries of a lake can be probabilitiscally determined down to each geographical pixel.

Our proposed ConvNet will initially be architectured as follows:








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
