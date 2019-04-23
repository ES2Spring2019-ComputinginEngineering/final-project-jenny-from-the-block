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

def convolveImage(pixeldata):  #Convolve each image 
    t = np.linspace(-1, 1, 5)
    bump = np.exp(-0.1*t**2)
    bump /= np.trapz(bump)
    kern = bump[:, np.newaxis] * bump[np.newaxis, :]
    blur = ndimage.convolve(pixeldata,kern)
    plt.figure()
    plt.imshow(blur) 
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