# Algae Bloom Detection Using Sentinel-2 Imagery

# Project Overview
This project aims to detect potential algal bloom occurrences in river water using Sentinel-2 Level-2A satellite imagery and spectral indices derived from multispectral bands.
The study utilizes pre-processed Sentinel-2 imagery, including mosaicking, clipping, resampling, and spectral index generation amd ml modeling to identify areas with characteristics associated with algal blooms.

# Data Source
- Satellite Data
- Platform: Sentinel-2 Level-2A
- Source: Microsoft Planetary Computer
- Spatial Resolution:
B03 (Green): 10 m
B04 (Red): 10 m
B05 (Red Edge): 20 m (resampled to 10 m)
B08 (NIR): 10 m
B11 (SWIR): 20 m (resampled to 10 m)
- Acquisition Period
2025-04-16
- Cloud Cover: < 5%

# Libraries used
Python 3.x
Rasterio
NumPy
GeoPandas
Matplotlib
Pandas
Scikit-Learn
os

# Band Download
The following Sentinel-2 bands were downloaded:
catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1"
| Band | Description         | Resolution |
| ---- | ------------------- | ---------- |
| B03  | Green               | 10 m       |
| B04  | Red                 | 10 m       |
| B05  | Red Edge            | 20 m       |
| B08  | Near Infrared       | 10 m       |
| B11  | Short Wave Infrared | 20 m       |

# Image Preprocessing
Mosaic
Multiple Sentinel-2 tiles covering the study area were mosaicked.
Tiles used:

43RBK
43RBJ
43RCK
43RCJ
42RZP

Resampling
Bands B05 and B11 were resampled from 20 m to 10 m spatial resolution.

Clipping
All mosaicked bands were clipped using the study area boundary.

# Spectral Indices
Floating Algae Index (FAI)
Used to detect floating algae and surface bloom formations.

Normalized Difference Chlorophyll Index (NDCI)
Used as a proxy indicator of chlorophyll concentration.

Normalized Difference Turbidity Index (NDTI)
Used to assess suspended sediments and turbidity.

# A Random Forest classification workflow was explored using:
Features:
NDCI
NDTI
FAI

Classes:
Algae Bloom -1
Non-Algae Bloom -2

Training data were extracted from manually digitized sample locations.