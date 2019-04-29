"""
Authors: @YassiKhorsandian & @Allison Choi
"""
# IMPORT STATEMENTS
from PIL import Image
from functions import openImage, getPixelData, convolveImage, graphPixelData1, graphPixelData2, findRatio, findMaxIndex, placeLocator

#Importing the images and opening them as arrays
openImage("PopulationScaled.png")
openImage("SunScaled.png")

#Getting pixel data from image RGBA values
picture = Image.open('PopulationScaled.png') 
poppixeldata = getPixelData(picture, 1, 613, 451)
picture2 = Image.open("SunScaled.png")
sunpixeldata = getPixelData(picture2, 0, 613, 451)

#Image processing
convolveImage(picture)
picture3 = Image.open('convPop.png')
CONVpoppixeldata = getPixelData(picture3, 1, 613, 451)
#conPopData = getPixelData(convPop, 1, 451, 613)

#Finding ratio of sunlight/population & maximum value with its index
ratio = findRatio(sunpixeldata, CONVpoppixeldata)
maximum, ind, ind2 = findMaxIndex(ratio)
print("Maximum Ratio: ", maximum)
print("Index of Point with Maximum Ratio: (", ind, ",", ind2, ")")

#Graphing data
graphPixelData1(sunpixeldata, CONVpoppixeldata, ratio)
graphPixelData2("PopulationScaled.png", ratio)
placeLocator("PopulationScaled.png", ratio)