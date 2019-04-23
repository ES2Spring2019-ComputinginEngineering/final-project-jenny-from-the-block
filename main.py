"""
Authors: @YassiKhorsandian & @Allison Choi
"""

# This files should not contain any function definitions


# IMPORT STATEMENTS
from PIL import Image 
from functions import openImage, getPixelData, convolveImage, graphPixelData

#Importing the images and opening them as arrays
openImage("PopulationScaled.png")
openImage("SunScaled.png")

#Getting pixel data from image RGBA values
picture = Image.open('PopulationScaled.png') 
poppixeldata = getPixelData(picture, 1, 613, 451)
picture2 = Image.open("SunScaled.png")
sunpixeldata = getPixelData(picture2, 0, 613, 451)

#Image processing
convPop = convolveImage(poppixeldata, "BuGn")
convSun = convolveImage(sunpixeldata, "YlOrRd")

#Graphing ratio of sun/population
graphPixelData(sunpixeldata, poppixeldata)