#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from ImageSeg import imageSeg
import os
from shapely.ops import triangulate
from shapely.geometry import MultiPoint

def preSegment(cur_path, img_path, shapes, pre_segment_save_directory, pre, display_img):
    
    #2. 采用Delaunay Triangulation对点集进行三角分割
    src_segment_polygon_list = []
    for i in range(len(shapes)):
        src_segment_polygon_list.append(shapes[i]['points_coord'])

    if display_img == 1:
        #3. 分割原始图像并保存
        imageSeg(cur_path+img_path, src_segment_polygon_list, pre=pre, save_directory=cur_path+pre_segment_save_directory)
        # 加载分割后的图像并显示
        files = os.listdir(cur_path+pre_segment_save_directory)
        files.sort()    #文件名排序
        plt.figure()
        for file in files:
            if file == '.DS_Store':
                pass
            else:
                img_segment = cv.imread(cur_path + pre_segment_save_directory + '/' + file, cv.IMREAD_UNCHANGED)
                plt.imshow(img_segment,cmap = 'gray')

        plt.show()

    return shapes
