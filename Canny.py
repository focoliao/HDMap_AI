#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

def canny(cur_path, base_img_path, edge_detection_save_directory, threshold_step, step_width, low_threshold_start, high_threshold_start):
    #2. 读取输入图像:
    img_path = cur_path + base_img_path #拼接图像路径
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    directory = cur_path + edge_detection_save_directory    # Image directory
    os.chdir(directory)     # Change the current directory to specified directory 
    assert img is not None, "file could not be read, check with os.path.exists()"

    #3. 高斯滤波降噪:
    blur = cv.GaussianBlur(img, (5, 5), 0)  

    #4. 双阈值检测和连接其他边缘,输出结果:
    low_threshold = []
    high_threshold = []
    for i in range(threshold_step):
        low_threshold.append(low_threshold_start + i*step_width)
        high_threshold.append(high_threshold_start + i*step_width)

    for i in range(threshold_step):
        edges = cv.Canny(blur, low_threshold[i], high_threshold[i])
        filename = 'low_threshold_' + str(low_threshold[i]) + '-' + 'high_threshold_' + str(high_threshold[i]) + '.jpg'
        cv.imwrite(filename, edges)

    os.chdir(cur_path)  #复原当前目录

    return
