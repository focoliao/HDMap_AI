#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from FNN import fnn
from FREAK import freak_kp_des
from Canny import canny
from PreSegment import preSegment
import configuration, configurationMisc
from PixMatch import pixMatch
from RANSAC import ransac
from VehicleDetection import vehicleDetection
from ResultDisplay import traceDisplay, trackDisplay, trackDisplay_3D
from Triangulation import triangulation
import os, datetime
from shapely.geometry import Point
from shapely.geometry import MultiPoint
from shapely.ops import triangulate, voronoi_diagram
from shapely.plotting import plot_polygon, plot_points
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle, Circle, Polygon
from ResultDisplay import display_triangulate
from PointsSelection import pointsSelection_img, pointsSelection_hd

class ClickData:
    def __init__(self, ax, background_image_path):
        self.points = []
        self.i = 0
        self.background_image_path = background_image_path
        self.ax = ax
        self.cid = ax.figure.canvas.mpl_connect('button_press_event', self.onclick)

    def onclick(self, event):
        if event.dblclick:
            self.i += 1
            print(self.i)
            self.points.append((event.xdata, event.ydata))
            plt.gca().add_patch(Circle((event.xdata, event.ydata),radius=1, linewidth=1,edgecolor='r',facecolor='None'))    #画一个小圈，以显示点选的位置
            plt.gca().add_patch(Circle((event.xdata, event.ydata),radius=5, linewidth=1,edgecolor='r',facecolor='None'))   #画一个大圈，以更明显地显示点选的位置
            plt.text(event.xdata, event.ydata, self.i, color = "r") #显示编号，以更方便对应
            #当点数大于2时，画出凸包
            #if len(self.points) > 2:
            #    hull = ConvexHull(self.points)
            #    hull_points=[]
            #    for i in range(len(hull.vertices)):
            #        hull_points.append(self.points[hull.vertices[i]])
            #    plt.gca().add_patch(Polygon(hull_points,color='forestgreen', alpha=0.5))
    
    def get_data(self):
        return self.points


def singleDirectionApp(cur_path, configuration_single_direction):
    '''
    #验证流程第一步：在图像上选点
    print('==> 验证流程第一步：在图像上选点 -- 当前时间:' + str(datetime.datetime.now()))
    #选点操作
    img = mpimg.imread(cur_path + configuration_single_direction.base_img_path)
    plt.figure('Base Image Selection')
    ax = plt.imshow(img)
    data_img = ClickData(ax, cur_path + configuration_single_direction.base_img_path)
    plt.show()
    points_img = data_img.get_data() 
    #显示Delaunay Triangulation三角分割效果
    #display_triangulate(points_img, cur_path+configuration_single_direction.base_img_path)
    
    #验证流程第二步：在高精地图上选点
    print('==> 验证流程第二步：在高精地图上选点 -- 当前时间:' + str(datetime.datetime.now()))
    #选点操作
    img = mpimg.imread(cur_path + configuration_single_direction.hd_img_path)
    plt.figure('HD Selection')
    ax = plt.imshow(img)
    data_hd = ClickData(ax, cur_path + configuration_single_direction.hd_img_path)
    plt.show()
    points_hd = data_hd.get_data() 
    
    #验证流程第三步：利用选择的点，通过Delaunay Triangulation方法进行三角分割，并获得分形
    print('==> 验证流程第三步：利用选择的点，通过Delaunay Triangulation方法进行三角分割，并获得分形 -- 当前时间:' + str(datetime.datetime.now()))
    shapes_img, shapes_hd = triangulation(points_img,points_hd)
    print(shapes_img)
    print(shapes_hd)
    #验证流程第四步：基于分形进行图像切割
    print('==> 验证流程第四步：基于分形进行图像切割 -- 当前时间:' + str(datetime.datetime.now()))
    #图形图形切割
    preSegment(cur_path, 
               configuration_single_direction.base_img_path,
               shapes_img, 
               configuration_single_direction.pre_segment_src_save_directory, 
               configuration_single_direction.pre_segment_src_pre,
               1)   # 0:不显示切割后图像；1:显示切割后图像
    #高精地图图形切割
    preSegment(cur_path, 
               configuration_single_direction.hd_img_path, 
               shapes_hd, 
               configuration_single_direction.pre_segment_dst_save_directory, 
               configuration_single_direction.pre_segment_dst_pre,
               configuration_single_direction.process_type)   # 0:不显示切割后图像；1:显示切割后图像

    #验证流程第五步：通过仿射变换，计算高精地图图形与图像图形之间的像素匹配关系，并存储映射矩阵
    print('==> 验证流程第五步：通过仿射变换，计算高精地图图形与图像图形之间的像素匹配关系 -- 当前时间:' + str(datetime.datetime.now()))
    pixMatch(cur_path, 
             configuration_single_direction.base_img_path,
             configuration_single_direction.hd_img_path,
             shapes_img, 
             shapes_hd, 
             configuration_single_direction.pre_segment_src_save_directory, 
             configuration_single_direction.image_size,
             configuration_single_direction.pre_segment_src_pre,
             configuration_single_direction.lookup_matrix_path,
             configuration_single_direction.process_type,   # 0:不显示切割后图像；1:显示切割后图像
             function_type = 1)     # 0:做图形变换、显示；1:做图形变换、显示、计算查找矩阵
    
    #验证流程第六步：车辆目标图像定位
    print('==> 验证流程第六步：车辆目标图像定位 -- 当前时间:' + str(datetime.datetime.now()))
    #==STEP7:车辆目标图像定位
    #step7-1:车辆目标图像定位
    # media_type: 0: image; 1: video; detection_type: 0 ==> box;  1 ==> segment
    if configuration_single_direction.media_type == 0 and configuration.detection_type == 0:
        vehicleDetection(configuration_single_direction.media_type, cur_path + configuration_single_direction.real_time_img_path[0], cur_path + configuration_single_direction.box_save_track_path, configuration_single_direction.detection_type) 
    elif configuration_single_direction.media_type == 1 and configuration.detection_type == 0:
        vehicleDetection(configuration_single_direction.media_type, cur_path + configuration_single_direction.real_time_video_path, cur_path + configuration_single_direction.box_save_trace_path, configuration_single_direction.detection_type) 
    elif configuration_single_direction.media_type == 0 and configuration.detection_type == 1:
        vehicleDetection(configuration_single_direction.media_type, cur_path + configuration_single_direction.real_time_img_path[0], cur_path + configuration_single_direction.seg_save_track_path, configuration_single_direction.detection_type) 
    elif configuration_single_direction.media_type == 1 and configuration.detection_type == 1:
        vehicleDetection(configuration_single_direction.media_type, cur_path + configuration_single_direction.real_time_video_path, cur_path + configuration_single_direction.seg_save_trace_path, configuration_single_direction.detection_type) 
    else:
        pass
    
    #验证流程第七步：车辆目标图像定位在图像上的显示
    print('==> 验证流程第七步：车辆目标图像定位在图像上的显示 -- 当前时间:' + str(datetime.datetime.now()))
    #step7-2:车辆目标图像定位在图像上的显示
    # media_type: 0: image; 1: video; detection_type: 0 ==> box;  1 ==> segment
    if configuration_single_direction.media_type == 0 and configuration_single_direction.detection_type == 0:
        trackDisplay(cur_path+configuration_single_direction.real_time_img_path[0], 
                     cur_path+configuration_single_direction.hd_img_path,
                     cur_path+configuration_single_direction.box_save_track_path,
                     cur_path+configuration_single_direction.hd_save_track_path,
                     cur_path+configuration_single_direction.lookup_matrix_path,
                     configuration_single_direction.image_size,
                     coord_type = 0,
                     detection_type =0)
    elif configuration_single_direction.media_type == 1 and configuration_single_direction.detection_type == 0:
        traceDisplay(cur_path+configuration_single_direction.base_img_path, 
                     cur_path+configuration_single_direction.hd_img_path,
                     cur_path+configuration_single_direction.save_trace_path,
                     cur_path+configuration_single_direction.lookup_matrix_path,
                     configuration_single_direction.image_size,
                     configuration_single_direction.video_rescale,
                     coord_type = 0,
                     detection_type =0)
    elif configuration_single_direction.media_type == 0 and configuration_single_direction.detection_type == 1:
        trackDisplay(cur_path+configuration_single_direction.real_time_img_path[0], 
                     cur_path+configuration_single_direction.hd_img_path,
                     cur_path+configuration_single_direction.seg_save_track_path,
                     cur_path+configuration_single_direction.hd_save_track_path,
                     cur_path+configuration_single_direction.lookup_matrix_path,
                     configuration_single_direction.image_size,
                     coord_type = 0,
                     detection_type =1)
    elif configuration_single_direction.media_type == 1 and configuration_single_direction.detection_type == 1: 
        traceDisplay(cur_path+configuration_single_direction.base_img_path, 
                     cur_path+configuration_single_direction.hd_img_path,
                     cur_path+configuration_single_direction.seg_save_trace_path,
                     cur_path+configuration_single_direction.lookup_matrix_path,
                     configuration_single_direction.image_size,
                     configuration_single_direction.video_rescale,
                     coord_type = 0,
                     detection_type =1)
    else:
        pass
    
    #验证流程第八步：车辆目标空间位置计算及显示
    print('==> 验证流程第八步：车辆目标空间位置计算及显示 -- 当前时间:' + str(datetime.datetime.now()))
    #==STEP8:车辆目标空间位置计算及显示
    # media_type: 0: image; 1: video; detection_type: 0 ==> box;  1 ==> segment
    if configuration_single_direction.media_type == 0 and configuration_single_direction.detection_type == 0:
        trackDisplay(cur_path+configuration_single_direction.real_time_img_path[0], 
                     cur_path+configuration_single_direction.hd_img_path,
                     cur_path+configuration_single_direction.box_save_track_path,
                     cur_path+configuration_single_direction.hd_save_track_path,
                     cur_path+configuration_single_direction.lookup_matrix_path,
                     configuration_single_direction.image_size,
                     coord_type = 1,    # coord: 0:原始坐标；1:变换后坐标
                     detection_type =0)     
    elif configuration_single_direction.media_type == 1 and configuration_single_direction.detection_type == 0:
        traceDisplay(cur_path+configuration_single_direction.base_img_path, 
                     cur_path+configuration_single_direction.hd_img_path,
                     cur_path+configuration_single_direction.box_save_trace_path,
                     cur_path+configuration_single_direction.lookup_matrix_path,
                     configuration_single_direction.image_size,
                     configuration_single_direction.video_rescale,
                     coord_type = 1,    # coord: 0:原始坐标；1:变换后坐标
                     detection_type =0)    
    elif configuration_single_direction.media_type == 0 and configuration_single_direction.detection_type == 1:
        trackDisplay(cur_path+configuration_single_direction.real_time_img_path[0], 
                     cur_path+configuration_single_direction.hd_img_path,
                     cur_path+configuration_single_direction.seg_save_track_path,
                     cur_path+configuration_single_direction.hd_save_track_path,
                     cur_path+configuration_single_direction.lookup_matrix_path,
                     configuration_single_direction.image_size,
                     coord_type = 1,
                     detection_type =1)
    elif configuration_single_direction.media_type == 1 and configuration_single_direction.detection_type == 1: 
        traceDisplay(cur_path+configuration_single_direction.base_img_path, 
                     cur_path+configuration_single_direction.hd_img_path,
                     cur_path+configuration_single_direction.seg_save_trace_path,
                     cur_path+configuration_single_direction.lookup_matrix_directory+configuration_single_direction.lookup_matrix_path,
                     configuration_single_direction.image_size,
                     configuration_single_direction.video_rescale,
                     coord_type = 1,
                     detection_type =1)
    else:
        pass
    '''

    #验证流程第九步：3D车辆目标空间位置计算及显示
    print('==> 验证流程第九步：3D车辆目标空间位置计算及显示 -- 当前时间:' + str(datetime.datetime.now()))
    #==STEP9:3D车辆目标空间位置计算及显示
    trackDisplay_3D(cur_path+configuration_single_direction.hd_img_path, 
                    cur_path+configuration_single_direction.csvs_directory_3D, 
                    configuration_single_direction.image_size, 
                    cur_path+configuration_single_direction.lookup_matrix_path,
                    cur_path+configuration_single_direction.hd_trace_3D_path)

    return


def singleDirectionPreprocessing(cur_path, configuration_single_direction, step_number):

    if step_number == 1:
        #验证流程第一步：在图像上选点
        print('==> 验证流程第一步：在图像上选点 -- 当前时间:' + str(datetime.datetime.now()))
        #选点操作
        pointsSelection_img(cur_path, configuration_single_direction.img_path_4_selection, configuration_single_direction.save_img_points_path)   
    elif step_number == 2:
        #验证流程第二步：在高精地图上选点
        print('==> 验证流程第二步：在高精地图上选点 -- 当前时间:' + str(datetime.datetime.now()))
        #选点操作
        pointsSelection_hd(cur_path, configuration_single_direction.hd_img_path_4_selection, configuration_single_direction.save_hd_points_path, configuration_single_direction.img_path_4_selection, configuration_single_direction.save_img_points_path) 
    else:
        #验证流程第三步：利用选择的点，通过Delaunay Triangulation方法进行三角分割，并获得分形
        print('==> 验证流程第三步：利用选择的点，通过Delaunay Triangulation方法进行三角分割，并获得分形 -- 当前时间:' + str(datetime.datetime.now()))
        shapes_img, shapes_hd = triangulation(cur_path+configuration_single_direction.save_img_points_path,cur_path+configuration_single_direction.save_hd_points_path)

        #验证流程第四步：基于分形进行图像切割
        print('==> 验证流程第四步：基于分形进行图像切割 -- 当前时间:' + str(datetime.datetime.now()))
        #图形图形切割
        preSegment(cur_path, 
                   configuration_single_direction.base_img_path,
                   shapes_img, 
                   configuration_single_direction.pre_segment_src_save_directory, 
                   configuration_single_direction.pre_segment_src_pre,
                   configuration_single_direction.process_type)   # 0:不显示切割后图像；1:显示切割后图像
        #高精地图图形切割
        preSegment(cur_path, 
                   configuration_single_direction.hd_img_path, 
                   shapes_hd, 
                   configuration_single_direction.pre_segment_dst_save_directory, 
                   configuration_single_direction.pre_segment_dst_pre,
                   configuration_single_direction.process_type)   # 0:不显示切割后图像；1:显示切割后图像

        #验证流程第五步：通过仿射变换，计算高精地图图形与图像图形之间的像素匹配关系，并存储映射矩阵
        print('==> 验证流程第五步：通过仿射变换，计算高精地图图形与图像图形之间的像素匹配关系 -- 当前时间:' + str(datetime.datetime.now()))
        pixMatch(cur_path, 
                 configuration_single_direction.base_img_path,
                 configuration_single_direction.hd_img_path,
                 shapes_img, 
                 shapes_hd, 
                 configuration_single_direction.pre_segment_src_save_directory, 
                 configuration_single_direction.image_size,
                 configuration_single_direction.pre_segment_src_pre,
                 configuration_single_direction.lookup_matrix_path,
                 configuration_single_direction.process_type,   # 0:不显示切割后图像；1:显示切割后图像
                 function_type = 1)     # 0:做图形变换、显示；1:做图形变换、显示、计算查找矩阵

    return

def singleDirectionHDPositioning(cur_path, configuration_single_direction):

    #验证流程第九步：3D车辆目标空间位置计算及显示
    print('==> 验证流程第九步：3D车辆目标空间位置计算及显示 -- 当前时间:' + str(datetime.datetime.now()))
    #==STEP9:3D车辆目标空间位置计算及显示
    trackDisplay_3D(cur_path+configuration_single_direction.hd_img_path, 
                    cur_path+configuration_single_direction.csvs_directory_3D, 
                    configuration_single_direction.image_size, 
                    cur_path+configuration_single_direction.lookup_matrix_path,
                    cur_path+configuration_single_direction.hd_trace_3D_path)
    
    return