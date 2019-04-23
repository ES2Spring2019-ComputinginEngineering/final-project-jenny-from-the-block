#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:02:14 2019

@author: Yassi Khorsandian & Allison Choi
"""
import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

def openImage(pic):
    im = np.array(imageio.imread(pic))
    plt.figure()
    plt.imshow(im)
    plt.show()

def getPixelData(pic, RGBA, width, height):
    picData = np.zeros((width, height))
    pix = pic.load()
    for i in range(width):
        for j in range(height):
            picData[i,j] = pix[i,j][RGBA]
    return picData

def convolveImage(pixeldata, color):
    kern = np.array([[-1, -1,-1],[0, 0, 0],[1, 1, 1]])
    blur = ndimage.convolve(pixeldata,kern)
    plt.figure()
    plt.imshow(blur, cmap = color) 
    plt.show()

def graphPixelData(sunpixeldata, poppixeldata):
    width,height = poppixeldata.shape
    ratio = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            if poppixeldata[i,j] == 0:
                ratio[i,j] = 0
            else:
                ratio[i,j] = sunpixeldata[i,j]/poppixeldata[i,j]
    plt.figure()
    plt.plot(ratio, "ko")
    plt.ylabel("Sunlight to population ratio")
    plt.xlabel("Pixel Index") 
    plt.show()