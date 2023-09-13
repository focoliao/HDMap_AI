#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from PerspectiveTransform import perspectiveTransform
from AffineTransform import affineTransform, affineTransform_get_matrix
from ImageSeg import imageSeg
from os.path import sep
import configuration
import os
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from scipy.io import savemat

def pixMatch(cur_path, src_img_path, dst_img_path,src_match_shapes, dst_match_shapes, pre_segment_src_save_directory, image_size, pre_segment_src_pre, lookup_matrix_path, display_img, function_type):

    # 1.读取两张图片，用于对比显示
    img_src_path = cur_path + src_img_path   #原始图像路径
    img_dst_path = cur_path + dst_img_path   #高精地图图像路径
    
    img_src = cv.imread(img_src_path, cv.IMREAD_UNCHANGED)
    img_dst = cv.imread(img_dst_path, cv.IMREAD_UNCHANGED)

    epsilon = 1e-15

    plt.figure('Source')
    plt.imshow(img_src,cmap = 'gray') #
    plt.figure('Target')
    plt.imshow(img_dst,cmap = 'gray') #

    rows = [(0,0)] * image_size[0]
    lookup_matrix_list = []
    # 2. 构造一个image_size的矩阵
    for i in range(image_size[1]):
        lookup_matrix_list.append(rows)
    lookup_matrix = np.array(lookup_matrix_list)
    # 3. 进行变换

    img_out_list = []
    for i in range(len(src_match_shapes)):  #len(src_match_shapes)
        print(i)
        if src_match_shapes[i]['points_num'] == 4:     # 当为四边形时，采用透视变换
            img_input_perspective = cv.imread(cur_path + pre_segment_src_save_directory + pre_segment_src_pre + str(src_match_shapes[i]['shape_id']) + configuration.img_format, cv.IMREAD_UNCHANGED)
            
            if display_img == 1:
                trans_matrix,img_output_perspective = perspectiveTransform(src_match_shapes[i]['points_coord'], dst_match_shapes[i]['points_coord'], img_input_perspective, img_dst)    
                img_out_list.append(img_output_perspective)
            elif display_img == 0:
                pass # 这里有些代码没写！！！！
            if function_type == 1:
                polygon = Polygon(src_match_shapes[i]['points_coord'])
                xmin, ymin, xmax, ymax = polygon.bounds
                for h_x in range(int(xmin), int(xmax)+1):
                    for k_y in range(int(ymin), int(ymax)+1):
                        point = Point(h_x,k_y)
                        if Point(point).distance(polygon) < epsilon:
                            result = np.dot(trans_matrix,np.array([h_x,k_y,1]).T)
                            x1 = result[0]/result[2]
                            y1 = result[1]/result[2]
                            lookup_matrix[k_y][h_x] = (round(x1), round(y1))        
        elif src_match_shapes[i]['points_num'] == 3:   # 当为三角形时，采用仿射变换   
            if display_img == 1: 
                img_input_affine = cv.imread(cur_path + pre_segment_src_save_directory + pre_segment_src_pre + str(src_match_shapes[i]['shape_id']) + configuration.img_format, cv.IMREAD_UNCHANGED)
                trans_matrix, img_output_affine = affineTransform(src_match_shapes[i]['points_coord'], dst_match_shapes[i]['points_coord'], img_input_affine, img_dst)
                img_out_list.append(img_output_affine)
            elif display_img == 0:
                trans_matrix = affineTransform_get_matrix(src_match_shapes[i]['points_coord'], dst_match_shapes[i]['points_coord'])
            else:
                pass
            if function_type == 1:
                polygon = Polygon(src_match_shapes[i]['points_coord'])
                xmin, ymin, xmax, ymax = polygon.bounds
                for h_x in range(int(xmin), int(xmax)+1):
                    for k_y in range(int(ymin), int(ymax)+1):
                        point = Point(h_x,k_y)
                        if Point(point).distance(polygon) < epsilon:
                            result = np.dot(trans_matrix,np.array([h_x,k_y,1]).T)
                            x1 = result[0]
                            y1 = result[1]
                            lookup_matrix[k_y][h_x] = (round(x1), round(y1))
        else:
            pass

    # 4.存储查找矩阵
    lookup_matrix_to_save = pd.DataFrame(lookup_matrix.tolist())
    lookup_matrix_to_save.to_csv(cur_path + lookup_matrix_path)
    #savemat(cur_path + lookup_matrix_directory +  configuration.lookup_matrix_path, lookup_matrix)
    
    if display_img == 1:
        # 5.将源图像进行变换，得到结果后，和目标图像叠加显示
        for i in range(len(img_out_list)):
            plt.imshow(img_out_list[i],cmap = 'gray')

        # 6.结果单独显示
        plt.figure('Result')
        for i in range(len(img_out_list)):
            plt.imshow(img_out_list[i],cmap = 'gray')

        plt.show()

    return