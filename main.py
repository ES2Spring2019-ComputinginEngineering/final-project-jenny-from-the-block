"""
Authors: @YassiKhorsandian & @Allison Choi
"""

# This files should not contain any function definitions


# IMPORT STATEMENTS
# importing PIL 
from PIL import Image 
import numpy as np
  
# Read image 
solarPic = Image.open('PopulationScaled.png') 
populationPic = Image.open('SunScaled.png')   
#solarPic.show() 
#populationPic.show()
  
solarData = np.zeros((613,451))
populationData = np.zeros((613,451))

solarPix = solarPic.load()
popPix = populationPic.load()
#print(popPix[1,2][1])
solarW, solarH = solarPic.size
populationW, populationH = populationPic.size

for i in range(solarW):
    for j in range(solarH):
        solarData[i,j] = solarPix[i,j][0]
        populationData[i,j] = popPix[i,j][1]


# DEMONSTRATION CODE
