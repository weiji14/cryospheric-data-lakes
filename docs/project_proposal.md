---
documentclass: article
title: |
  | Deep Learning in the Cryosphere:
  | Using deep neural networks to investigate subglacial water.
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

Glaciers flow via a combination of three methods: 1) plastic deformation of the viscous ice itself, 2) Sliding from water between the glacier and bed, 3) Deformation of the bed [see Figure 1, @Cuffeyphysicsglaciers2010, p.223].
Our study is part of this wider literature of work looking at how the flow of glaciers or ice streams is speeding up or slowing down over time in Antarctica.
In particular, we will focus on mechanisms 2 and 3 which look at the subglacial component of the glacier.
These basal processes are not very well understood, as they are difficult to observe directly.
Also, the problem is compounded as basal sliding and deformation are not mutually exclusive but controlled in some way by the amount of water in the subglacial part of the glacier [@Cuffeyphysicsglaciers2010, p.223].

![The 3 components that contribute to glacier flow](https://upload.wikimedia.org/wikipedia/commons/3/3a/Glacier_flow-mechanisms.png){width=350px}

Taken together, the motion of glaciers from sliding and deformation at the bed is also called basal slip [@Cuffeyphysicsglaciers2010, p.223].
The amount of water available plays an important role in increasing or decreasing basal slip.
In mountain glaciers, it has been observed how glaciers flow faster during the spring melt season and ocassionally after heavy rainfall [@IkenUpliftUnteraargletscherBeginning1983].
Similarly in Antarctica, there are ice streams overlying subglacial lakes - large water bodies that drain ocassionally and trigger rapid ice flow events [@BellLargesubglaciallakes2007].

We do have some knowledge on how water underneath a glacier helps ice to flow faster.
On one hand, water in sufficient amounts can exert an upward pressure that is greater than the downward gravitational pull on the ice.
This tends to occur in small channel cavities where drainage is poor, causing water to accumulate and build up enough pressure to increase the area of separation between ice and rock, lowering friction and thus allowing ice to slide over its bedrock [@Cuffeyphysicsglaciers2010, p.238].
On the other hand, water can also percolate into porous bedrock and weaken it into a softer material more prone to deformation.
In fact, most glacier beds are composed of glacial till.
When these highly porous sediments are saturated with water, they can easily give way and move downhill, carrrying along with it the ice on top [@Cuffeyphysicsglaciers2010, p.255-256].
Given enough information on the basal velocity, shear stress, and properties of the bedrock, it will then be possible to formulate a slip relation that can predict the movement of a glacier [@Cuffeyphysicsglaciers2010, p.223].

Understanding how water behaves at the glacier bed enables us to solve two major outstanding problems in glaciology: the detailed mechanisms of basal slip; and the causes and mechanisms of glacial surges [@Cuffeyphysicsglaciers2010, p.176].
All of these will be crucial for figuring out how fast the ice draining from Antarctica will flow as our planet continues to warm.
Consequently, this will feed into the bigger picture question on what is the rate at which sea level will rise and affect our global community.

## Plan

The increasing amount of remotely sensed geophysical data provided daily across Antarctica is an unrealized potential that can help us to answer one basic question - Where does water lie beneath the ice sheet?
Here we propose a novel deep learning based approach to discover subglacial features, specifically subglacial lakes and their networked channels, that have mostly been studied previously using isolated aerial or ground-based surveys.
This approach aims to utilize openly available datasets, with the goal of making discoveries that individual datasets alone would not confidently yield.

At present, the large amount and varied formats of the datasets presents many challenges to researchers, from the very basic management of the data volume itself to the specialized task of logically interpreting the data within set realms of scientific uncertainty.
For us, we introduce another layer of complexity by attempting to combine such specialized cross-disciplinary datasets in both the dimensions of space and time.
The challenge for us lies in the integration methodology, which involves the combination of standard geographical frameworks and state of the art data science practices.

To tackle this, we adhere ourselves to an automated data processing workflow that is as reproducible as possible, down to the very copies of the software and data used.
We make use of Graphical Processing Units (GPUs) where possible to speed up our neural network model's calculations [see @SteinkrausUsingGPUsmachine2005].
On the software front, parallel implementations of algorithms and self learning artificial intelligence modules offer us a similar speed up advantage in analyzing the data.
Taken together, these increases result in several magnitude orders of improved runtime efficiencies, allowing us to scale alongside the volumes of data being collected to analyze.
Keeping up with these technological improvements will allow for more experimental iterations even as our data repository size grows, thus improving our chances of uncovering groundbreaking discoveries within a reasonable amount of time.

## Previous work

### Glacier flow in relation to basal water

Ice is interesting where there is water.
In Antarctica, water can be easily seen on the surface in some places, mostly close to dark, low-albedo areas like rock outcrops and blue ice regions [@KingslakeWidespreadmovementmeltwater2017].
The bulk of liquid water in Antarctica however, lies hidden below the ice sheet.
There are over 400 subglacial lakes already discovered, and we know from geomophological evidence that water also flows in subglacial channels underneath the ice sheet [@SiegertRecentadvancesunderstanding2016].
Water in the cryospheric system is interesting primarily because of its fluid properties.
Compared to ice, water flows a lot more quickly over short timescales, and ice that is in contact with water exhibits a higher level of dynamicity than it would otherwise solely by itself.

Various subglacial drainage pathways have been theorized over the years, ranging from fast channelized flow in concentrated channels to slower distributed flows over a large surface area [see Figure 2, @FlowersModellingwaterflow2015].
These subglacial drainage structures are known to change between the two extremes of efficient and inefficient regimes over space and time, with implications for ice dynamics [@MullerVelocityfluctuationswater1973].
The treatment of Antarctic glaciers/ice streams does however, differ from that of temperate glaciers owing to the lack of input from surface meltwater, i.e. the Antarctic subglacial water system is predominantly supplied from basal melt processes.
One area of initial heavy focus was on the Whillans Ice Stream (formerly Ice Stream B), where seismic surveys found a water saturated, ~5 metre thick porous till layer [@BlankenshipSeismicmeasurementsreveal1986] that could easily deform and explain the observed high surface velocities [@AlleyDeformationtillice1986].
Indeed, further studies in other geographic locations found that soft beds and abundant meltwater are seen as one of the major controls on the locations of ice streams, secondary only to topographic focusing linked to a calving margin [@WinsborrowWhatcontrolslocation2010].
This reinforces the importance of water as drivers of fast ice flow, and it goes back to the question of why we need to know the location of water beneath the ice sheet.

![Channelized vs Distributed flow in a subglacial drainage system.](http://rspa.royalsocietypublishing.org/content/royprsa/471/2176/20140907/F2.large.jpg){width=350px}

TODO:
- Surging Glaciers
- Shallow Ice Approximation (SIA) and Shallow Shelf Approximation (SSA) models of flow
- Comparison to inverse models

### Deep Neural Networks

An artificial neural network, very loosely based on biological neural networks, is a system made up of neurons.
Each single neuron comprises of a simple mathematical function that takes an input value 'x' and produces some output 'y'.
Neural networks are architected by combining many of these neurons together, either by stacking them in parallel (width-wise), or by joining them one after another (depth-wise) as multiple hidden layers.

[insert picture of one neuron, a shallow 1-layer network, a deep 2-layer network]

The term deep neural network is used when there is not a direct function mapping between the input data and final output prediction.
In other words, we call it deep when there are two or more hidden layers in the neural network.
Earlier layers in the neural network start off as representations of fairly simple features.
Deeper layers progressively build on these earlier layers, forming more complex feature representations that can provide useful information to generate the output prediction.

Almost certainly at the start, a neural network will output predicted values that do not match the actual groundtruth value.
The difference between the groundtruth and predicted value is used as the basis of training the neural network to do better.
We do this by taking the error difference, and step backwards through the neural network, updating the weights of each neuron using some calculus.
Basically, the more a neuron contributes to the predicted output, the more that neuron's weight will be adjusted.
This backward update is also termed as backpropagation [add citation].

# Proposed Research

## Research questions

The goal of this research is to explore the applicability of deep learning to extract information from cryospheric remote sensing datasets, with a particular focus on Antarctic subglacial hydrology.
Due to the rich variation and large amount of openly available cryospheric datasets we have, we will first attempt to make full use of the spatial correlations between different physical datasets to increase the spatial resolution of lower resolution datasets.
Next, we can align and stack these different high resolution datasets together and train a neural network on known subglacial lakes, and see if this can yield potential lakes yet to be discovered by classical methods.
Finally, we will interpret the ConvNet model's intermediate layers and see how it may inform a new generation of cryospheric research and potentially improve ice sheet models.
The questions to be addressed are as follows:

(@) What is the potential of using a Super-image Resolution Convolutional Neural Network to increase the spatial resolution of cryospheric datasets?
Where might this resolution enhancement perform adequately and where might it fail compared to standard resampling techniques?

(@) How can we architect and train a Deep Convolutional Neural Network on a high-dimensional raster dataset to detect subglacial lakes?
What are the building blocks and hyperparameters that will allow this ConvNet to work well?

(@) Why does a Deep Convolutional Neural Network predict that a subglacial lake is present or absent in any one particular area?
How might we apply deep learning to improve the predictive capability of ice sheet models?

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

\newpage

![RAMP RADARSAT](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/sat_radarsat.png){width=200px}
![MODIS MOA](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/sat_modis.png){width=200px}
![RAMP2 DEM](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/ter_ramp.png){width=200px}

![Cryosat2 DEM](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/ter_cryosat.png){width=200px}
![BEDMAP2](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/ter_bedmap.png){width=200px}
![MEASURES Ice flow speed](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/glac_flowspeed.png){width=200px}

![Subglacial Water Flux](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/glac_subglflux.png){width=200px}
![Subglacial Heat Flux NOTE INCORRECT ONE](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/phys_anhf.png){width=200px}
![AntGG Gravity Anomaly](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/phys_antgg.png){width=200px}

![EIGEN-6C4 Gravity Model](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/phys_eigen.png){width=200px}
![Subglacial Lakes Smith](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/glac_lakess.png){width=200px}
![Subglacial lakes Wright & Siegert](http://quantarctica.npolar.no/opencms/export/sites/quantarctica/data-catalog/images/glac_lakesws.png){width=200px}

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


# Methodology

## Data preparation

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

## Neural Network model

Given an input of a multi-dimensional image of Antarctica, the goal of our subglacial lake identification project would be to determine each location of our lake.
Our initial proposed model is a Convolutional Neural Network that can perform object segmentation down to the level of a geographic pixel to delineate the exact boundaries of a subglacial water body.
The model's architecture is as follows:




# Preliminary Results

Trained a standard feedforward artificial neural network on ICESAT x, y, z, t, zs, zb data but due to imbalanced dataset problem, could not get good test accuracy.
Namely, high number of false negatives.

Trained an object localization classifier based on YOLOv2 using a stacked optical imagery, surface elevation and bed elevation raster.
Hard to quantify whether predicted bounding boxes where random or meaningful to our study.

Adapted a U-net based ConvNet to perform object segmentation of subglacial lakes on same stacked dataset.
Used SELU non-linearity instead of RELU to self normalize images, and tweaked some model hyperparameters.
More promising than YOLOv2-based model as can output oval shaped objects.

Future steps:

- Stack together even more layers (see Data section)
- Use depthwise separable convolutions, factorizing a standard convolution to look spatially at individual channels before combining them across channels.
- Deepen the ConvNet and introduce more Residual-like units.


# Project framework

## Outline

This research project will be structured as a series of sections containing a few chapters.

### Section 1 - Applications of Deep Learning in the Cryosphere

Here, we start of with a few mini-projects that provide a gentle introduction to the applicability of deep learning to the cryosphere.
The first chapter is inspired by facial recognition technology, and uses an extensive photo dataset to teach a neural network to identify glaciers for a data rescue operation.
The second chapter is an idea we will explore, whereby a neural network is trained to produce a crisp high resolution image from a lower resolution image, and this is based on similar work that has been applied to regular everyday photos.

- Chapter 1 - Using Capsule Networks to recognize the names of glaciers in New Zealand.

- Chapter 2 - Using a super-image resolution convolutional neural network to increase spatial resolution of cryospheric datasets.


### Section 2 - A supervised Deep Learning approach to mapping the subglacial hydrology of Antarctica

Next, the deep learning techniques are revised and applied on a larger scale to map the geography of subglacial water in Antarctica. For the third chapter, we use a neural network architecture similar to those used in self-driving cars that detect objects, and apply it to several geographic layers to find spatial subglacial lake boundaries. In the fourth chapter, we introduce the time dimension and use it to understand how this subglacial hydrological network drains, fills or re-routes itself over the satellite era.

Chapter 3 - Semantic segmentation of subglacial lakes in Antarctica using Convolutional Neural Networks.

Chapter 4 - Inferring the changing subglacial hydrology of Antarctica from time series data using a Recurrent Convolutional Neural Network.


### Section 3 - Making sense of our Cryospheric Deep Neural Networks and their applicability to ice sheet models

Finally, our focus shifts towards an in depth interpretation of the results in our previous sections.
The fifth chapter aims to peer into our black box neural network models and provide insights on what are the most important parameters that matter in our mathematical models.
The sixth chapter will then gather these insights and use them to update some of the assumptions underlying our ice sheet models, hopefully leading to more accurate predictions on the future of the Antarctic Ice Sheet.

Chapter 5 - Visualizing and interpreting the layers of a deep subglacial lake classifier and its contribution to cryospheric research.

Chapter 6 - Applications of Deep Learning to dynamic ice sheet models.



## Timeline

| Month | TODO                                         |
|:-----:|:-------------------------------------------- |



# Budget and Resource Requirements

## Funding

- Rutherford Discovery Fellowship
- Antarctic Research Centre Endowed Development Fund (for travel to Fairbanks, Alaska)

## Hardware

- Linux High Performance Computing cluster
- Graphical Processing Units (e.g. 4 Tesla K80 GPUs)

# Acknowledgements

I would like to acknowledge some of the short courses and public competitions I have participated in which taught me a lot of things about glaciology and deep learning.

### Courses

- [Deep learning Specialization Coursera by Andrew Ng](https://www.coursera.org/specializations/deep-learning).
- [Fifth International Summer School in Glaciology at University of Alaska, Fairbanks](https://glaciers.gi.alaska.edu/courses/summer-school/2018).

### Competitions

- [Kaggle Statoil iceberg classification challenge](https://www.kaggle.com/c/statoil-iceberg-classifier-challenge).
- [Kaggle Data Science Bowl 2018](https://www.kaggle.com/c/data-science-bowl-2018).
- [New Zealand Space Challenge 2018](https://www.nzspacechallenge.com/).



# References
