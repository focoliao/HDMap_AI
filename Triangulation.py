#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
from scipy.spatial import Delaunay
import numpy as np
import pandas as pd

def triangulation(save_img_points_path,save_hd_points_path):
    #读取存储的图像选点
    df_img_points = pd.read_csv(save_img_points_path)
    points_img = []
    for i in range(len(df_img_points)):
        img_points_tmp = eval(df_img_points['img_points'][i])
        for j in range(len(img_points_tmp)):
            points_img.append((img_points_tmp[j][0], img_points_tmp[j][1]))

    #读取存储的高精地图选点
    df_hd_points = pd.read_csv(save_hd_points_path)
    points_hd = []
    for i in range(len(df_hd_points)):
        points_hd.append((df_hd_points['img_location_x'][i], df_hd_points['img_location_y'][i]))
    
    print('points_img length:' + str(len(points_img)))
    print('points_hd length:' + str(len(points_hd)))

    #2. 采用Delaunay Triangulation对点集进行三角分割
    points = np.array(points_hd)
    triangles = Delaunay(points)
    shapes_img = []
    shapes_hd = []
    #3. 根据simplices生成source和hd对应的匹配shapes
    for i in range(len(triangles.simplices)):
        points_coord_src = [points_img[triangles.simplices[i,0]],points_img[triangles.simplices[i,1]],points_img[triangles.simplices[i,2]]]
        points_coord_hd = [points_hd[triangles.simplices[i,0]],points_hd[triangles.simplices[i,1]],points_hd[triangles.simplices[i,2]]]
        shapes_img.append({'shape_id': i,  'points_num': 3,'shape_style': 'polygon','points_coord':points_coord_src})
        shapes_hd.append({'shape_id': i,  'points_num': 3,'shape_style': 'polygon','points_coord':points_coord_hd})

    return shapes_img, shapes_hd
