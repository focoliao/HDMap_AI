#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

def affineTransform(src, dst, image_src, img_dst):
    # 读取图片
    image = image_src

    # 原始三个点坐标
    pts1 = np.float32(src)
    # 变换后的三个点坐标
    pts2 = np.float32(dst)

    # 生成仿射变换矩阵
  
    matrix = cv.getAffineTransform(pts1, pts2)

    # 进行仿射变换
    result = cv.warpAffine(image, matrix, img_dst.shape[:2][::-1])
    
    return matrix, result

def affineTransform_get_matrix(src, dst):

    # 原始三个点坐标
    pts1 = np.float32(src)
    # 变换后的三个点坐标
    pts2 = np.float32(dst)

    # 生成仿射变换矩阵
  
    matrix = cv.getAffineTransform(pts1, pts2)
    
    return matrix