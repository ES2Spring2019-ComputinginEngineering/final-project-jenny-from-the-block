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

def getPixelData(pic, RGBA):
    width, height = pic.size()
    picData = np.zeros(width, height)
    pix = pic.load()
    for i in range(width):
        for j in range(height):
            picData[i,j] = pix[i,j][RGBA]
    return picData

picture = Image.open('PopulationScaled.png') 
getPixelData(picture, 1)