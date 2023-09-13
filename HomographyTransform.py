#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

def homographyTransform(src, dst, image_src, img_dst):
    # 读取图片
    image = image_src

    # 原始四个点坐标
    pts1 = np.float32(src)
    # 变换后的四个点坐标
    pts2 = np.float32(dst)

    # 3. RANSAC计算Homography变换矩阵
    matrix, status = cv.findHomography(pts1, pts2)

    # 4.将源图像进行变换，得到结果后，和目标图像叠加显示
    #result = cv.warpPerspective(image, matrix, img_dst.shape[:2][::-1]) 
    result = cv.warpPerspective(image, matrix, (img_dst.shape[1], img_dst.shape[0])) 
    
    
    return result