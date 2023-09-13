#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

def fnn(des_real_time,des_vibration):
    #1. 创建Flann匹配器:
    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)

    #2. 添加需要匹配的描述子到FNN匹配器中:
    descriptors1 = np.float32(des_real_time)
    descriptors2 = np.float32(des_vibration)
    #3. 使用KNN匹配来获得实时图像描述子与预训练描述子集合之间的匹配:
    matches = flann.knnMatch(queryDescriptors = descriptors1,
                                 trainDescriptors = descriptors2,
                                 k = 2)     # des_real_time是实时图像的描述子,des是其进行匹配的描述子集合，k是返回的最近邻个数

    return matches