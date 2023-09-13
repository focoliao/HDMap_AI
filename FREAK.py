#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os


def freak_kp_des(cur_path, real_img_path):
    des_freak = []
    for i in range(len(real_img_path)):
        #2. 读取输入图像:
        img_path = cur_path + real_img_path[i] #拼接图像路径
        img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"

        #3.FAST角点检测
        fast = cv.FastFeatureDetector_create()
        kp = fast.detect(img, None)

        #4.计算FREAK描述子
        freak = cv.xfeatures2d.FREAK_create()
        #freak = cv.DescriptorExtractor_create("FREAK")
        kp, des = freak.compute(img, kp)

        des_freak.append([kp,des])
    return des_freak


