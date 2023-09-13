#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

def perspectiveTransform(src, dst, image_src, img_dst):
    # 读取图片
    image = image_src

    # 原始点坐标
    pts1 = np.float32(src)
    # 变换后的点坐标
    pts2 = np.float32(dst)

    # 生成透视变换矩阵
  
    matrix = cv.getPerspectiveTransform(pts1, pts2)

    # 进行透视变换
    result = cv.warpPerspective(image, matrix, img_dst.shape[:2][::-1])  
    
    return matrix, result