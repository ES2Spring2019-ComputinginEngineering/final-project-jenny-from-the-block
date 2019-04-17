#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:02:14 2019

@author: Yassi Khorsandian & Allison Choi
"""
from PIL import Image 
import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

def openImage(pic):
    im = np.array(imageio.imread(pic))
    plt.figure()
    plt.imshow(im)
    plt.show()
  
openImage("PopulationScaled.png")
openImage("SunScaled.png")

def getPixelData(pic, RGBA, width, height):
    picData = np.zeros((width, height))
    pix = pic.load()
    for i in range(width):
        for j in range(height):
            picData[i,j] = pix[i,j][RGBA]
    return picData

picture = Image.open('PopulationScaled.png') 
poppixeldata = getPixelData(picture, 1, 613, 451)
picture2 = Image.open("SunScaled.png")
sunpixeldata = getPixelData(picture2, 0, 613, 451)

def graphPixelData():
    ratio = sunpixeldata/poppixeldata
    plt.figure()
    plt.plot(ratio, "ko")
    plt.ylabel("Sunlight to population ratio")
    plt.xlabel("Pixel Index?") 
    plt.show()
    
graphPixelData()

    