#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from matplotlib.patches import Rectangle, Circle
import pandas as pd
from scipy.spatial import ConvexHull

colors=['#FFC0CB','#FFFFFF','#000000','#FF00FF','#555555','#666666','#111111','#222222','#333333','#444444','#00FFFF','#FF0000','#777777','#888888','#999999','#101010','#151515','#202020']

def test_cornersCal(background_image_path, save_track_path):
    '''用于测试'''
    # 1.读取背景图片
    img_background = cv.imread(background_image_path, cv.IMREAD_UNCHANGED)
    plt.figure('Track Display - Source Map')
    plt.imshow(img_background,cmap = 'gray') #
    # 2.读取定位数据
    df = pd.read_csv(save_track_path)
    # 3.将所有定位打印在背景图上
    for i in range(len(df)):
        
        
        for item in eval(df['contour'][i]):
            plt.gca().add_patch(Circle((item[0], item[1]),linewidth=1,edgecolor=colors[int(df['id'][i])%18],facecolor=colors[int(df['id'][i])%18]))
        
        corner1 = cornersCal(np.array(eval(df['contour'][i])))
        plt.gca().add_patch(Circle(corner1,linewidth=4,edgecolor='g',facecolor='g'))
    plt.show()
    return

def cornersCal(mask):
    hull = ConvexHull(mask)
    hull_points = mask[hull.vertices]
    
    p2 = hull_points[hull_points[:,1].argmax()]

    return p2