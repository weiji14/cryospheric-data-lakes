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

Glaciers flow via a combination of three processes: 1) plastic deformation of the viscous ice itself; 2) sliding from water between the glacier and bed; and 3) deformation of the bed [see Figure 1, @Cuffeyphysicsglaciers2010, p.223].
Our study is part of this wider literature of work looking at how the flow of glaciers or ice streams is speeding up or slowing down over time in Antarctica.
In particular, we will focus on mechanisms 2 and 3 which look at the subglacial component of the glacier.
These basal processes are not very well understood, as they are difficult to observe directly.
Also, the problem is compounded as basal sliding and deformation are not mutually exclusive but both controlled in some way by the amount of water in the subglacial part of the glacier [@Cuffeyphysicsglaciers2010, p.223].

![The three components that contribute to glacier flow](https://upload.wikimedia.org/wikipedia/commons/3/3a/Glacier_flow-mechanisms.png){width=350px}

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
Consequently, this will feed into the bigger picture question on what is the rate at which sea level will rise and affect our coastal communities around the globe.

## Previous work

### Deep Neural Networks

An artificial neural network, very loosely based on biological neural networks, is a system made up of neurons.
Each single neuron comprises of a simple mathematical function that takes an input value 'x' and produces some output 'y'.
Neural networks are built by combining many of these neurons together, either by stacking them in parallel (width-wise), or by joining them one after another (depth-wise) as multiple hidden layers.

[insert picture of one neuron, a shallow 1-layer network, a deep 2-layer network]

The term deep neural network is used when there is not a direct function mapping between the input data and final output prediction.
In other words, we call it deep when there are two or more hidden layers in the neural network.
Earlier layers in the neural network start off as representations of fairly simple features.
Deeper layers progressively build on these earlier layers, forming more complex feature representations that can provide useful information to generate the output prediction [@GoodfellowDeeplearning2016].

Initially, a neural network will almost always output predicted values that do not match the actual groundtruth value.
The difference between the groundtruth and predicted value is used as the basis of training the neural network to do better.
We do this by taking the error difference, and step backwards through the neural network, updating the weights of each neuron using some calculus.
Basically, the more a neuron contributes to the predicted output, the more that neuron's weight will be adjusted.
This backward update is also termed as backpropagation [@RumelhartLearningrepresentationsbackpropagating1986].

For computer vision applications, Convolutional Neural Networks (ConvNets) are usually used in place of a standard feedforward neural network [see @LeCunDeeplearning2015 for a general review].
ConvNets have existed since @LeCunBackpropagationAppliedHandwritten1989, and are commonly used in pattern recognition tasks [e.g. @LecunGradientbasedlearningapplied1998].
It became a prominent tool in the computer vision community since the AlexNet architecture [@KrizhevskyImageNetClassificationDeep2012] almost halved the error rate of conventional object classification approaches in the 2012 ImageNet Large Scale Visual Recognition Competition.
Besides classification tasks, ConvNets have also been adapted for other uses.
One such application is the Super-Resolution Convolutional Neural Network (SRCNN) which is a regression method used to increase the resolution of images [@DongImageSuperResolutionUsing2014].
SRCNN can not only be used on ordinary photographic images, but also on pixel-based geographic datasets like Digital Elevation Models, improving their spatial resolution in a manner much better than ordinary interpolation methods [@ChenConvolutionalNeuralNetwork2016].
An even more interesting application is how SRCNNs can use the statistical correlation between geographical datasets like precipitation and elevation to increase the resolution of climate models, allowing us to capture more accurate local climate patterns [@VandalDeepSDGeneratingHigh2017].
Therefore, given a variety of high resolution datasets that are correlated to a low resolution geographic dataset we wish to improve, it should be possible to design and train a neural network to improve that low resolution dataset.

### Glacier flow in relation to basal water

Ice is interesting where there is water.
In Antarctica, water can be easily seen on the surface in some places, mostly close to dark, low-albedo areas like rock outcrops and blue ice regions [@KingslakeWidespreadmovementmeltwater2017].
The bulk of liquid water in Antarctica however, lies hidden below the ice sheet.
There are over 400 subglacial lakes already discovered, and we know from geomophological evidence that water also flows in subglacial channels underneath the ice sheet [@SiegertRecentadvancesunderstanding2016].
Water in the cryospheric system is interesting primarily because of its fluid properties.
Compared to ice, water flows a lot more quickly over short timescales, and ice that is in contact with water is more dynamic than it would otherwise be.

Various subglacial drainage pathways have been theorized over the years, ranging from fast channelized flow to slower distributed flows over a large surface area [see Figure 2, @FlowersModellingwaterflow2015].
These subglacial drainage structures are known to change between the two extremes of efficient and inefficient regimes over space and time, with implications for ice dynamics [@MullerVelocityfluctuationswater1973].
The treatment of Antarctic glaciers/ice streams does however, differ from that of temperate glaciers owing to the lack of input from surface meltwater, i.e. the Antarctic subglacial water system is predominantly supplied from basal melt processes.
One area of initial heavy focus was on the Whillans Ice Stream (formerly Ice Stream B), where seismic surveys found a water saturated, ~5 metre thick porous till layer [@BlankenshipSeismicmeasurementsreveal1986] that could easily deform and explain the observed high surface velocities [@AlleyDeformationtillice1986].
Indeed, further studies in other geographic locations found that soft beds and abundant meltwater are one of the major controls on the locations of ice streams, secondary only to topographic focusing linked to a calving margin [@WinsborrowWhatcontrolslocation2010].
This reinforces the importance of water as drivers of fast ice flow, and it goes back to the question of why we need to know the location of water beneath the ice sheet.

![Channelized vs Distributed flow in a subglacial drainage system.](http://rspa.royalsocietypublishing.org/content/royprsa/471/2176/20140907/F2.large.jpg){width=300px}

The most exemplary example of fast glacier flow are when glaciers *surge*, characterized by an "abnormally fast flow of a glacier over a period of a few months to years, during which the glacier margin may advance substantially" [@CogleyGlossaryglaciermass2011, p.89].
Recurring surge events are well documented in several small glaciers, the classical example being Variegated Glacier in Alaska [@EisenVariegatedGlacierAlaska2005].
There has been little evidence however, for surges happening across broad regions of modern ice sheets [@Cuffeyphysicsglaciers2010, p.537].
Isolated surge-type glaciers are found in some parts of East Greenland, initially considered to mostly exhibit Alaskan-type surges based on a hydrologic switch model [@JiskootSurgepotentialdrainagebasin2003].
Later studies have shown that Svalbard-type surges based on a thermal switch model also apply to some glaciers in the region [@JiskootSurgesmallEast2009].
Surge-type glaciers have since been catalogued into two geographical supercluster centres (named Arctic Ring and High Mountain Asia), and statistical analyses used to postulate a new enthalpy cycle model [@SevestreClimaticgeometriccontrols2015].
Optimal surging conditions are satisfied in environments that are not in the cold/dry and warm/humid extremes, but in an intermediate zone where enthalpy heat gains cannot be discharged effectively via heat conduction or meltwater discharge - a zone which includes the Antarctic Peninsula [@SevestreClimaticgeometriccontrols2015].
The main trigger for surges in Antarctica appears to be from ice shelf breakups, with satellite observations confirming the acceleration of ice after the Larsen B ice shelf partially collapsed [@DeAngelisGlacierSurgeIce2003; @RignotAcceleratedicedischarge2004; @ScambosGlacieraccelerationthinning2004].
It has been noted though that the surges were only limited to the major fast-flowing tributaries and not the slow moving ice piedmonts or smaller glaciers, showing how glacier dynamics are still governed by basal thermal conditions and subglacial hydrology [@DeAngelisGlacierSurgeIce2003].

Observing water under the ice sheet is difficult due to the different materials involved (ice, water, rock) having different transmission properties.
Surveying these features requires studying either mechanical wave (e.g. active seismic sounding) or electromagnetic wave (e.g. ground-penetrating radar) signals.
The waves may come from active or passive sources, and are detected using sensors deployed on the ground, in the air, or onboard of satellites in space.
We know that subglacial water exists in three ways: 1) subglacial lakes; 2) subglacial channels; 3) subglacial aquifers [@ColleoniSpatiotemporalvariabilityprocesses2018].
The first direct documented subglacial lake was detected in 1967 using airborne radio-echo sounding [@RobinInterpretationRadioEcho1969] from a joint programme between the UK Scott Polar Research Institute, the US National Science Foundation and the Technical University of Denmark, cumulating in the first subglacial lake inventory of 17 lakes [@OswaldLakesAntarcticIce1973], followed by a second inventory with 77 lakes  [@SiegertinventoryAntarcticsubglacial1996] and a third inventory with 145 lakes [@SiegertrevisedinventoryAntarctic2005].
Since then, large (10+ km in diameter) 'active' subglacial lakes have been detected based on vertical surface displacements using radar interferometry [@GrayEvidencesubglacialwater2005], laser altimetry [@Smithinventoryactivesubglacial2009] and optical image differencing [@FrickerActiveSubglacialWater2007], resulting in a fourth inventory that includes 379 lakes [@WrightfourthinventoryAntarctic2012] with more discoveries following [e.g. @WrightEvidencehydrologicalconnection2012; @WrightSubglacialhydrologicalconnectivity2014; @RiveraSubglacialLakeCECs2015; @KimActivesubglaciallakes2016; @SmithConnectedsubglaciallake2017].
Satellite and airborne surveys however, provide limited detail on the subglacial hydrological system, and we need ground based systems to resolve the location of hydrological structures not just directly under the ice but inside of the bedrock as well.
At Subglacial Lake Whillans for example, radar [@ChristiansonSubglacialLakeWhillans2012] and active seismic [@HorganSubglacialLakeWhillans2012] surveys were conducted to constrain the stratigraphic thickness of the ice and water bodies as part of the Whillans Ice Stream Subglacial Access Research Drilling (WISSARD) project [@TulaczykWISSARDSubglacialLake2014] by timing how long it takes for the waves to reflect off various layers.
These standard geophysical surveys can be further complemented by passive magnetotelluric [@WannamakerStructurethermalregime2004] and active controlled-source electromagnetic methods [@DuganSubsurfaceimagingreveals2015] that measure electrical conductivity, a technique that can not only detect ice-water boundaries but also map deeper groundwater present in subglacial aquifers [@Keyfeasibilityimagingsubglacial2017].
Typically, a detailed subglacial hydrology study would integrate most of these methods, using multiple ground-based electromagnetic geophysical techniques, constrained using seismic and airborne geophysical data, to detect, delineate and quantify water beneath the ice sheet [@SiegertAntarcticsubglacialgroundwater2018].

### Ice Sheet Modelling

"All models are wrong; the practical question is how wrong do they have to be to not be useful." [@BoxEmpiricalmodelbuildingresponse1987, p.74].
An ice sheet model in its most primitive form has to capture two processes: 1) climatic-basal mass balance [@CogleyGlossaryglaciermass2011, p. 29]; and 2) ice flow [@CogleyGlossaryglaciermass2011, p. 42].
For each process being modelled, there are many methods ranging from simple or complex that are used to approximate the physical reality of an ice sheet.
The choice of which scheme to choose depends on factors like the amount of computational power available, spatial resolution of the grid, the length of the time period the stimulation will run for, and how accurate the results need to be with the physical world.

Mass balance changes can be modelled by accounting for total accummulation minus total ablation [@CogleyGlossaryglaciermass2011, p.7].
For an ice sheet like Antarctica, important contributions to mass balance change are the surface ablation that can be calculated using simple temperature-index methods or sophisticated energy balance methods [@HockGlaciermeltreview2005], plus frontal ablation which includes calving, subaerial melting and subaerial sublimation, and subaqueous frontal melting [@CogleyGlossaryglaciermass2011, p. 44].

Modern ice flow modelling relies on the numerical implementation of fluid dynamics.
There is an entire hierarchy of flow models going from zero-order and higher-order models to gold standard Full-Stokes models that can describe the forces going from the grounded portion of the ice sheet to the floating ice shelves [@KirchnerCapabilitieslimitationsnumerical2011].
Zero-order models commonly used include the Shallow ice approximation (SIA), which only considers shear stresses that are assumed to govern the flow of grounded ice [@FowlerFlowPolythermalGlaciers1978; @HutterTheoreticalglaciologymaterial1983]; and the Shallow shelf approximation (SSA), which only considers longitudinal stresses that are assumed to govern the flow of floating ice shelves [@MorlandUnconfinedIceShelfFlow1987].
Higher-order models approximate the full Stokes equations [see @Hindmarshnumericalcomparisonapproximations2004], with examples including the Blatter-Pattyn models [@BlatterVelocitystressfields1995; @Pattynnewthreedimensionalhigherorder2003] and hybrid type models [@BuelerShallowshelfapproximation2009; @WinkelmannPotsdamParallelIce2011; @PollardDescriptionhybridice2012].
Full Stokes models capture the most complete physical representation we have of ice flow, with examples like Elmer/Ice [@GagliardiniCapabilitiesperformanceElmer2013] and FELIX-S [@Lengparallelhighorderaccurate2012].
Traditionally, zero-order or higher-order models have been used for their computational efficiency, and continue to be used for paleo ice-sheet stimulations over longer timescales [@KirchnerShallowiceapproximation2016].
In recent years however, there has been a gradual shift towards the use of Full Stokes models as they provide more consistent results even across dynamic regions like grounding lines [@PattynBenchmarkexperimentshigherorder2008; @ZhangcomparisontwoStokes2017].
This is especially important as there is a growing movement to couple ice sheet models with ocean models for more realistic stimulations [@deBoerCurrentstatefuture2017; @Asay-DavisExperimentaldesignthree2016].

![](https://ars.els-cdn.com/content/image/1-s2.0-S0277379111002915-gr1.jpg){width=300px}
![](https://ars.els-cdn.com/content/image/1-s2.0-S0277379111002915-gr4.jpg){width=350px}

It can be argued that the increasing demand for using complex Full Stokes ice sheet models over simpler higher-order models not only necessitates the use of more computational power, but also a smarter use of technology.
Ice sheet models have to align with observational data in the old paleo record [e.g. @PollardModellingWestAntarctic2009] and modern settings [@GolledgemultimillennialAntarcticcommitment2015] without statistically overfitting the data and losing predictive capability.
Tuning parameters to data observations takes multiple experiments, yet one full experiment can take a long time to finish.
Although parallelized implementations of ice sheet models have been developed [see e.g. @WinkelmannPotsdamParallelIce2011], a 3-dimensional Full Stokes model can still take about 40 hours to run on a high-performance computing cluster of a few hundred CPUs [@LarourContinentalscalehigh2012].
Finer refinements to the models will only continue, and if we wish to prevent computational time from spiralling out of control, we will either need to find more processors, or utilize more efficient processors.
For example, one study showed a 60-180x speedup by using a Graphical Processing Unit (GPU) implementation of a second-order ice sheet flow model instead of a normal CPU implementation [@BraedstrupIcesheetmodellingaccelerated2014].
Furthermore, physics informed neural networks can be trained with data to solve and discover non-linear partial differential equations like the Navier-Stokes equation [@RudyDatadrivendiscoverypartial2017; @RaissiPhysicsInformedDeep2017; @RaissiPhysicsInformedDeep2017a], hinting at an extremely efficient GPU accelerated way for Full Stokes ice flow modelling.
We therefore envision that bringing together geophysical observations, physics-based models, and new GPU-accelerated neural network developments will provide the driving force for accelerating advancement in the glaciological field.




# Methodology

## Plan

Remotely-sensed geophysical data across Antarctica provides an unrealized potential that can help us to answer one basic question - Where does water lie beneath the ice sheet?
Here we propose a novel deep learning based approach to explore subglacial features, specifically subglacial lakes, channels and aquifers, that have often been studied using siloed datasets from space-borne, aerial or ground-based surveys.
This approach aims to utilize openly available datasets, with the goal of making discoveries that a few individual datasets alone would not have revealed.

At present, the large amount and varied formats of the datasets presents many challenges to researchers, from the very basic management of the data volume itself to the specialized task of logically interpreting the data within set realms of scientific uncertainty.
For us, we introduce another layer of complexity by attempting to combine such specialized cross-disciplinary datasets in both the dimensions of space and time.
The challenge for us lies in the integration methodology, which involves the combination of standard geographical frameworks and state of the art data science practices.

To tackle this, we adhere ourselves to an automated data processing workflow that is as reproducible as possible, down to the very copies of the software and data used.
We make use of Graphical Processing Units (GPUs) where possible to speed up our neural network model's calculations [see @SteinkrausUsingGPUsmachine2005].
On the software front, parallel implementations of algorithms and self learning artificial intelligence modules offer us a similar speed up advantage in analyzing the data.
Taken together, these increases result in several magnitude orders of improved runtime efficiencies, allowing us to scale alongside the volumes of data being collected to analyze.
Keeping up with these technological improvements will allow for more experimental iterations even as our data repository size grows, thus improving our chances of uncovering groundbreaking discoveries within a reasonable amount of time.

## Data preparation

The heterogeneous nature of our datasets presents some challenges, but the observation-level data fusion process can be structured as a step by step process consisting of data alignment and data correlation, otherwise known as matching and coregistration in remote sensing terminology [@SchmittDataFusionRemote2016].

Geographic data can be broadly classified into vector and raster datasets, with the former being more suitable for discrete datasets, and the latter more associated with continuous datasets.
For each spot on the surface, we will assemble all the sensor measurements available for that spot using locational attributes tied to the sensor data.
As we are interested in the continuous spatial variation of adjacent sensor measurements at any one spot, we choose to employ the continuous raster format in our Geographic Information System (GIS).

Each data layer can be stacked together to create a multi-dimensional raster image that will feed into our computer vision model.
Conceptually, we can think of stacking multiple input feature layers in much the same way as stacking multiple bands in a multipectral optical satellite image.
In order to create the stack, we will first reproject each input layer to a common projected coordinate system - the Antarctic Polar Stereographic (EPSG:3031) which is a conformal projection system based on the WGS84 ellipsoid surface.

Next, each layer may need to be undergo further transformation so that the pixels are aligned across layers, either via a translational shift and/or resampling to a common spatial resolution.
For the resampling process, we may choose to use classical resampling techniques such as bilinear or bicubic interpolation, or a custom spline interpolation method.
Alternatively, it is also possible to employ Super-Resolution Convolutional Neural Network (SRCNN) to increase the spatial resolution of the raster [@DongImageSuperResolutionUsing2014].
For example, we can train an SRCNN to capture interdependencies with variables in the other layers to improve the reliability of the upscaling function [@VandalDeepSDGeneratingHigh2017], compared to a standard bicubic interpolation method which only looks at information from a single layer.
Once this is done, we will have a multi-layer raster that will act as an input to our neural network model.

## Datasets

The deep learning models will require the use of Antarctic datasets with nearly full coverage of the continent.
Our input data will include both raster- and vector-type datasets mainly collected from satellite platforms.
Examples of raster data include single-satellite digital terrain models (e.g. ICESAT, CryoSat), compiled products (e.g. BEDMAP2) and model outputs (e.g. Subglacial water flux).
Vector data will include polygons or points that come from published subglacial lake inventory collections.
For select regions of interest, we may source finer resolution data directly from airborne geophysical missions (e.g. Operation Icebridge) or ground based surveys.

Our criteria for incorporating a dataset into the shortlist is prioritized based on factors like spatial resolution and whether they have the potential to be useful for our subglacial hydrology research.
Where data products of similar types are available, we tend to choose the latest version, keeping an older version only if it has some value not found in the newer version.
For example, we have two Digital Elevation Models (DEM), one from ICESAT data, and one from CryoSat-2 data, as even though the ICESAT DEM is older, it is of higher spatial resolution and also sourced from a laser altimeter compared to CryoSat-2's radar altimeter.

### Raster Data

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

### Vector Data

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

## Preliminary Work

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

### Neural Network model

Given an input of a multi-dimensional image of Antarctica, the goal of our subglacial lake identification project would be to determine each location of our lake.
Our initial proposed model is a Convolutional Neural Network that can perform object segmentation down to the level of a geographic pixel to delineate the exact boundaries of a subglacial water body.
The model's architecture is as follows:




# Proposed Research Framework

## Research questions

The goal of this research is to explore the applicability of deep learning to extract information from cryospheric remote sensing datasets in an efficient manner, with a particular focus on Antarctic subglacial hydrology.
The questions to be addressed are as follows:

(@) What is the potential of using a Super-image Resolution Convolutional Neural Network to increase the spatial resolution of cryospheric datasets?
Where might this resolution enhancement perform adequately and where might it fail compared to standard resampling techniques?

(@) Where do subglacial lakes exist in Antarctica based on the geographical information we have gathered from our geophysical sensors?
How can we architect and train a Deep Convolutional Neural Network on a high-dimensional raster dataset to find these subglacial lakes?

(@) How can we use neural networks to speed up the calculations of Full Stokes ice sheet models via efficient Graphical Processing Units?
What is the potential of using this new and highly efficient paradigm across paleo- and modern day settings to improve our estimates on future sea level rise?

## Outline

This dissertation will follow a journal article style format, consisting of an introduction, three main topic chapters, and a conclusion.
Each of the three main topic chapters will provide significant contributions to the data, science and tools we use in glaciology.

### Chapter 1 - Introduction

### Chapter 2 - Applying Deep Learning to Cryospheric Datasets: Using a super-image resolution convolutional neural network to increase the spatial resolution of cryospheric datasets

Here, we start off by improving the cryospheric datasets that forms the basis of our project.
This is an idea based on similar work in enhancing the resolution regular everyday photos.
Over Antarctica, there are low resolution datasets for the whole continent (e.g. BEDMAP2) and high resolution datasets collected from isolated field studies.
We can match the two images geographically and train a super-image resolution neural network to produce a crisp high resolution image at places where we do not have field observations.

### Chapter 3 - Antarctic Subglacial Hydrology through Deep Learning: A supervised Convolutional Neural Network classifier for mapping the subglacial hydrology of Antarctica

Next, the deep learning techniques are applied to tackle the core science problem on locating subglacial water in Antarctica.
The neural network architecture is conceptually similar to those used by self-driving cars to locate objects of interest in images.
By combining several geographic layers together, and having an inventory of known subglacial lake positions, we can train a neural network to learn and identify subglacial lakes.
Given time-series data over longer periods, it may be possible to see how a subglacial hydrological network drains, fills or re-routes itself over time.

### Chapter 4 - Ice Flow Modelling with Deep Learning: Using data and physics based neural networks to solve Full Stokes equations

Finally, our focus shifts towards an in depth look at how neural networks can improve ice sheet models.
This line of research is motivated by how neural network calculations can be an order of magnitude faster on modern Graphical Processing Units compared to CPUs.
Translating the Full Stokes equations into a neural network format requires not only careful mathematical formulation, but also a lot of data from paleo- and modern day observations to train the network.
A successful re-implementation of numerical ice sheet models to an efficient neural network model will allow faster runtimes and hopefully lead to more reliable predictions on the future of the Antarctic Ice Sheet.

### Chapter 5 - Conclusions

## Timeline

| Month | TODO                                         |
|:-----:|:-------------------------------------------- |




# Acknowledgements

This project would not be possible without the academic and technical support from the Antarctic Research Centre.
Many thanks to my supervisors Dr. Huw Horgan and Dr. Brian Anderson for providing inspiration and helpful guidance in reviewing earlier drafts of this proposal.
I would also like to acknowledge some of the short courses and public competitions I have participated in which taught me a lot of things about glaciology and deep learning.
A special mention goes to Dr. Regine Hock and others in the International Summer School in Glaciology for really opening my eyes to the world of glaciology.

## Funding

- Rutherford Discovery Fellowship
- Antarctic Research Centre Endowed Development Fund (for travel to Fairbanks, Alaska)

## Hardware

- Linux High Performance Computing cluster
- Graphical Processing Units (e.g. 4 Tesla K80 GPUs)

## Courses

- [Deep learning Specialization Coursera by Andrew Ng](https://www.coursera.org/specializations/deep-learning).
- [Fifth International Summer School in Glaciology at University of Alaska, Fairbanks](https://glaciers.gi.alaska.edu/courses/summer-school/2018).

## Competitions

- [Kaggle Statoil iceberg classification challenge](https://www.kaggle.com/c/statoil-iceberg-classifier-challenge).
- [Kaggle Data Science Bowl 2018](https://www.kaggle.com/c/data-science-bowl-2018).
- [New Zealand Space Challenge 2018](https://www.nzspacechallenge.com/).




# References
