# Environmental Summary – Algae Bloom Detection Using Sentinel-2 and Random Forest

## Objective

The objective of this project is to identify and map potential algal bloom occurrences in river water using Sentinel-2 imagery and a Random Forest machine learning classifier.

## Data & Methods

Sentinel-2 Level-2A imagery was processed to generate three spectral indices: Floating Algae Index (FAI), Normalized Difference Chlorophyll Index (NDCI), and Normalized Difference Turbidity Index (NDTI). The calculated indices were stacked. Multiple image tiles were mosaicked, resampled to a common 10 m resolution, and clipped to the study area boundary. Training samples representing algae and non-algae locations were collected and used to extract index values. A Random Forest classifier was trained using these samples, optimized through grid search, and applied to classify the entire study area.

## Results

The Random Forest model achieved an overall classification accuracy of 83%. Feature importance analysis indicated that the spectral indices effectively differentiated algae-affected and non-algae water regions. FAI contributed the most for algae detection. The resulting classification map identified the spatial distribution of potential algal bloom zones within the river system.

## Limitations

* Limited number of training samples may affect model generalization.
* Classification accuracy depends on the quality and representativeness of training data.
* No field-based validation of algal bloom occurrences was available.

## Conclusion

The study demonstrates the applicability of Sentinel-2-derived spectral indices and Random Forest classification for algal bloom detection. The workflow provides a reproducible and scalable approach for monitoring water quality and supporting environmental management of river ecosystems.
