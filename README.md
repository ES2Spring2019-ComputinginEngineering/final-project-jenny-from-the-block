# Solar Placement
The purpose of this project is to determine the best location for the placement of solar cells in the state of Oregon. The two main variables that are used to determine the practicality of certain regions for the placement of a solar cell include population density and the amount of sunlight received. The location with the maximum amount of sunlight and the smallest population would be optimal for the placement of solar cells.

## Instructions
Run the "main.py" file 


In order to find the optimal location for the placement of solar cells in a region other than the state of Oregon:
* Obtain scaled images containing population data in green pixels and sunglight data in red pixels
* Place these files in the same folder as the "main.py"
* Name the image containing population data "PopulationScaled.png" & the image containing the sunlight data "SunScaled.png"
* Run the "main.py" file


## File List
* **"main.py":** code driver that runs all of the functions, assigns variables, and displays the images and graphs
* "functions.py": contains all of the functions created during this project
* "SunScaled.png": image containing the sunlight data from the state of Oregon
* "PopulationScaled.png": image containing the population data from the state of Oregon
* "convPop.png": blurred/convolved version of the population image
* "SolarPlacement.mov": extra credit short video describing the project

## Overview of Code
* openImage: open the image of sunlight and population data
* getPixelData: obtain the RGBA values for each pixel of the imported images (as arrays)
* convolveImage: convolve the population image to reduce the noise
* findRatio: finding ratio of sunlight to population
* graphPixelData1: graphing ratio array versus pixel index
* graphPixelData2: creating new RGBA image from ratio array
* findMaxIndex: finding the location where the ration of sunlight to population is at a maximum
* placeIndicator: place an indicator on the map where the ideal solar farm placement would be
