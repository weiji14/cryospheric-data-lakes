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
