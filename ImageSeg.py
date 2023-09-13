#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
from PerspectiveTransform import perspectiveTransform
from AffineTransform import affineTransform
from PIL import Image, ImageDraw
import configuration
import numpy
import shutil

def imageSeg(img_path, polygon_list, pre, save_directory):
    # read image as RGB and add alpha (transparency)
    im = Image.open(img_path).convert("RGBA")
    # convert to numpy (for convenience)
    imArray = numpy.asarray(im)
    shutil.rmtree(save_directory)   #先清空文件夹
    os.makedirs(save_directory)     #再建立文件夹
    for i in range(len(polygon_list)):
        # create mask
        maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
        ImageDraw.Draw(maskIm).polygon(polygon_list[i], outline=1, fill=1)
        mask = numpy.array(maskIm)
        # assemble new image (uint8: 0-255)
        newImArray = numpy.empty(imArray.shape,dtype='uint8')
        # colors (three first columns, RGB)
        newImArray[:,:,:3] = imArray[:,:,:3]
        # transparency (4th column)
        newImArray[:,:,3] = mask*255
        # back to Image from numpy
        newIm = Image.fromarray(newImArray, "RGBA")
        image_save_path = save_directory + pre + str(i) + configuration.img_format
        newIm.save(image_save_path)

    return