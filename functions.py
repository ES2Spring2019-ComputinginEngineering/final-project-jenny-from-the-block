#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:02:14 2019

@author: Yassi Khorsandian & Allison Choi
"""
import imageio
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageFilter

#Opens the image in form of an array
def openImage(pic):
    im = np.array(imageio.imread(pic))
    plt.figure()
    plt.imshow(im)
    plt.show()

#Finds the RGBA pixel data of image & returns as an array 
def getPixelData(pic, RGBA, width, height):
    picData = np.zeros((width, height))
    pix = pic.load()
    for i in range(width):
        for j in range(height):
            picData[i,j] = pix[i,j][RGBA]
    return picData

#Blurs image to reduce noise
def convolveImage(picture):  
    blurred_image = picture.filter(ImageFilter.BLUR)
    plt.figure()
    plt.imshow(blurred_image) 
    plt.show()
    blurred_image.save("convPop.png")

#Finds ratio of sunlight/population & returns as an array
def findRatio(sunpixeldata, poppixeldata):
    width,height = poppixeldata.shape
    ratio = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            if poppixeldata[i,j] < 50:
                ratio[i,j] = 0
            else:
                ratio[i,j] = sunpixeldata[i,j]/poppixeldata[i,j]
    return ratio

#Finds the maximum value of the ratios & the index of the point with maximum value
def findMaxIndex(ratio):
    width,height = ratio.shape
    maximum = np.max(ratio)
    ind = 0
    ind2 = 0
    for i in range(width-1):
            for j in range(height-1):
                if ratio[i,j] == maximum:
                    ind = i
                    ind2 = j
    return maximum, ind, ind2    

#Graphs the sunlight & population ratio 
def graphPixelData1(sunpixeldata, poppixeldata, ratio):
    width,height = poppixeldata.shape
    plt.figure()
    plt.plot(ratio, "ko")
    plt.ylabel("Sunlight to population ratio")
    plt.xlabel("Pixel Index") 
    plt.show()
    
#Graphs the sunlight & population ratio
def graphPixelData2(pic, ratio):
    im = np.array(imageio.imread(pic))
    width,height = ratio.shape
    for i in range(width-1):
        for j in range(height-1):
            im[j,i,0]=ratio[i,j]*30
            im[j,i,1]=0
            im[j,i,2]=0
    plt.figure()
    plt.imshow(im)
    plt.show()
    
#Places a an indicator at the point with the maximum ratio
def placeIndicator(pic,ratio):
    maximum, ind, ind2 = findMaxIndex(ratio)
    im = np.array(imageio.imread(pic))
    width,height = ratio.shape
    for i in range(width-1):
        for j in range(height-1):
            im[j,i,0]=ratio[i,j]*30
            im[j,i,1]=0
            im[j,i,2]=0
    plt.figure()
    plt.imshow(im)
    plt.plot(ind2,ind, "b*")
    plt.show()