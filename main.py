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
import configuration, configurationMisc, configuration_s2n, configuration_n2s, configuration_e2w, configuration_w2e
from PixMatch import pixMatch
from RANSAC import ransac
from VehicleDetection import vehicleDetection
from ResultDisplay import traceDisplay, trackDisplay
from SingleDirectionApp import singleDirectionApp
from MultiFusion import multiFusion_normal, multiFusion_3D, multiFusion_3D_frames
import os, datetime
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import Misc
from DataPreprocessing import dataPreprocessing
from HDPositioning import hdPositioning


cur_path = os.getcwd()  #当前程序绝对路径
hd_arrow_1_path = configuration.hd_arrow_1_path
img_arrow_1_path = configuration.img_arrow_1_path
base_img_path = configuration.base_img_path
hd_img_path = configuration.hd_img_path
edge_detection_save_directory = configuration.edge_detection_save_directory

real_img_path = configuration.real_img_path
real_time_img_path = configuration.real_time_img_path
real_time_video_path = configuration.real_time_video_path

media_type = configuration.media_type



if __name__=="__main__": 
    
    '''
    #==STEP3-1:采用Canny边缘检测算法，对base_img进行边缘提取
    
    print('STEP3-1:开始进行Canny边缘检测算法 -- 当前时间:' + str(datetime.datetime.now()))
    threshold_step = 10
    step_width = 10
    low_threshold_start = 10
    high_threshold_start = 20
    canny(cur_path, base_img_path, edge_detection_save_directory, threshold_step, step_width, low_threshold_start, high_threshold_start)
    print('STEP3-1:Canny边缘检测算法计算结束 -- 当前时间:' + str(datetime.datetime.now()))
    
    
    #==STEP3-2 ~ STEP4-2:连接图形，匹配图形--针对已匹配部分
    
    print('STEP3-2 ~ STEP4-2:开始连接图形、匹配图形[已匹配] -- 当前时间:' + str(datetime.datetime.now()))
    #连接并分割原始图形
    preSegment(cur_path, configuration.base_img_path, configuration.step3_2_edge_image_path, configuration.src_match_shapes, configuration.pre_segment_src_save_directory, configuration.pre_segment_src_pre)
    #连接并分割高精地图图形
    preSegment(cur_path, configuration.hd_img_path, configuration.hd_img_path, configuration.dst_match_shapes, configuration.pre_segment_dst_save_directory, configuration.pre_segment_dst_pre)
    print('STEP3-2 ~ STEP4-2:连接图形、匹配图形结束[已匹配] -- 当前时间:' + str(datetime.datetime.now()))

    
    #==STEP4-3:通过仿射变换，计算高精地图图形与图像图形之间的像素匹配关系
    print('STEP4-3:开始高精地图图形与图像像素匹配[已匹配] -- 当前时间:' + str(datetime.datetime.now()))
    pixMatch(cur_path, 
             configuration.base_img_path,
             configuration.hd_img_path,
             configuration.src_match_shapes, 
             configuration.dst_match_shapes, 
             configuration.pre_segment_src_save_directory, 
             configuration.pre_segment_dst_save_directory,
             configuration.pre_segment_src_pre,
             configuration.lookup_matrix_directory,
             function_type = 0)     # 0:做图形变换、显示；1:做图形变换、显示、计算查找矩阵
    print('STEP4-3:结束高精地图图形与图像像素匹配[已匹配] -- 当前时间:' + str(datetime.datetime.now()))
    
    
    #==STEP4-5-1:连接图形，匹配图形--针对非已匹配部分
    
    print('STEP4-5-1:开始连接图形、匹配图形[非已匹配] -- 当前时间:' + str(datetime.datetime.now()))
    #连接并分割原始图形
    preSegment(cur_path, configuration.base_img_path, configuration.step3_2_edge_image_path, configuration.src_unmatch_shapes, configuration.pre_segment_src_save_directory, configuration.pre_segment_src_pre)
    #连接并分割高精地图图形
    preSegment(cur_path, configuration.hd_img_path, configuration.hd_img_path, configuration.dst_unmatch_shapes, configuration.pre_segment_dst_save_directory, configuration.pre_segment_dst_pre)
    print('STEP4-5-1:连接图形、匹配图形结束[非已匹配] -- 当前时间:' + str(datetime.datetime.now()))
    
    
    
    #==STEP4-5-2:通过仿射变换，计算高精地图图形与图像图形之间的像素匹配关系
    print('STEP4-5-2:开始高精地图图形与图像像素匹配[非已匹配] -- 当前时间:' + str(datetime.datetime.now()))
    pixMatch(cur_path, 
             configuration.base_img_path,
             configuration.hd_img_path,
             configuration.src_unmatch_shapes, 
             configuration.dst_unmatch_shapes, 
             configuration.pre_segment_src_save_directory, 
             configuration.pre_segment_dst_save_directory,
             configuration.pre_segment_src_pre,
             configuration.lookup_matrix_directory,
             function_type = 0)     # 0:做图形变换、显示；1:做图形变换、显示、计算查找矩阵
    print('STEP4-5-2:结束高精地图图形与图像像素匹配[非已匹配] -- 当前时间:' + str(datetime.datetime.now()))
    
   
    #==STEP4-6:通过仿射变换，计算高精地图图形与图像图形之间的像素匹配关系
    print('STEP4-6:开始高精地图图形与图像像素匹配[已匹配+非已匹配] -- 当前时间:' + str(datetime.datetime.now()))
    pixMatch(cur_path, 
             configuration.base_img_path,
             configuration.hd_img_path,
             configuration.src_match_shapes + configuration.src_unmatch_shapes, 
             configuration.dst_match_shapes + configuration.dst_unmatch_shapes, 
             configuration.pre_segment_src_save_directory, 
             configuration.pre_segment_dst_save_directory,
             configuration.pre_segment_src_pre,
             configuration.lookup_matrix_directory,
             function_type = 1)     # function_type: 0:做图形变换、显示；1:做图形变换、显示、计算查找矩阵
    print('STEP4-6:结束高精地图图形与图像像素匹配[已匹配+非已匹配] -- 当前时间:' + str(datetime.datetime.now()))

   
    #==STEP5-10:采用FREAK算法，预先准备多张抖动图像的FREAK描述子
    
    print('STEP5-10:开始抖动库FREAK描述子计算 -- 当前时间:' + str(datetime.datetime.now()))
    kp_des_vibration = freak_kp_des(cur_path, real_img_path)
    print('STEP5-10:结束抖动库FREAK描述子计算 -- 当前时间:' + str(datetime.datetime.now()))
    
    #==对实时图片进行fnn匹配
    #（1）STEP6-1:计算实时图像的FREAK描述子
    print('STEP6-1:开始real_time_img FREAK描述子计算 -- 当前时间:' + str(datetime.datetime.now()))
    kp_des_real_time = freak_kp_des(cur_path, real_time_img_path)
    print('STEP6-1:结束real_time_img FREAK描述子计算 -- 当前时间:' + str(datetime.datetime.now()))
    #（2）STEP6-2:计算match结果
    print('STEP6-2:开始real_time_img和抖动库FREAK描述子匹配计算 -- 当前时间:' + str(datetime.datetime.now()))
    match_result = []
    for i in range(len(kp_des_vibration)):
        match_result.append(fnn(kp_des_real_time[0][1], kp_des_vibration[i][1]))
    print('STEP6-2:结束real_time_img和抖动库FREAK描述子匹配计算 -- 当前时间:' + str(datetime.datetime.now()))
    
    #==STEP6-3:采用RANSAC求解最佳的平移和旋转变换  
    print('STEP6-3:开始real_time_img和抖动库最佳匹配计算 -- 当前时间:' + str(datetime.datetime.now())) 
    best_match_index = ransac(match_result, kp_des_real_time, kp_des_vibration, cur_path, real_time_img_path, real_img_path)
    print('STEP6-3:结束real_time_img和抖动库最佳匹配计算 -- 当前时间:' + str(datetime.datetime.now()))
    print('最佳匹配图片序号为:' + str(best_match_index + 1))

    
    #==STEP7:车辆目标图像定位
    #step7-1:车辆目标图像定位
    # media_type: 0: image; 1: video; detection_type: 0 ==> box;  1 ==> segment
    if configuration.media_type == 0 and configuration.detection_type == 0:
        vehicleDetection(configuration.media_type, cur_path + real_time_img_path[0], cur_path + configuration.box_save_track_path, configuration.detection_type) 
    elif configuration.media_type == 1 and configuration.detection_type == 0:
        vehicleDetection(configuration.media_type, cur_path + real_time_video_path, cur_path + configuration.box_save_trace_path, configuration.detection_type) 
    elif configuration.media_type == 0 and configuration.detection_type == 1:
        vehicleDetection(configuration.media_type, cur_path + real_time_img_path[0], cur_path + configuration.seg_save_track_path, configuration.detection_type) 
    elif configuration.media_type == 1 and configuration.detection_type == 1:
        vehicleDetection(configuration.media_type, cur_path + real_time_video_path, cur_path + configuration.seg_save_trace_path, configuration.detection_type) 
    else:
        pass
    
    
    #step7-2:车辆目标图像定位在图像上的显示
    # media_type: 0: image; 1: video; detection_type: 0 ==> box;  1 ==> segment
    if configuration.media_type == 0 and configuration.detection_type == 0:
        trackDisplay(cur_path+configuration.real_time_img_path[0], 
                     cur_path+configuration.hd_img_path,
                     cur_path+configuration.box_save_track_path,
                     cur_path+configuration.lookup_matrix_directory+configuration.lookup_matrix_path,
                     coord_type = 0,
                     detection_type =0)
    elif configuration.media_type == 1 and configuration.detection_type == 0:
        traceDisplay(cur_path+configuration.base_img_path, 
                     cur_path+configuration.hd_img_path,
                     cur_path+configuration.save_trace_path,
                     cur_path+configuration.lookup_matrix_directory+configuration.lookup_matrix_path,
                     coord_type = 0,
                     detection_type =0)
    elif configuration.media_type == 0 and configuration.detection_type == 1:
        trackDisplay(cur_path+configuration.real_time_img_path[0], 
                     cur_path+configuration.hd_img_path,
                     cur_path+configuration.seg_save_track_path,
                     cur_path+configuration.lookup_matrix_directory+configuration.lookup_matrix_path,
                     coord_type = 0,
                     detection_type =1)
    elif configuration.media_type == 1 and configuration.detection_type == 1: 
        traceDisplay(cur_path+configuration.base_img_path, 
                     cur_path+configuration.hd_img_path,
                     cur_path+configuration.seg_save_trace_path,
                     cur_path+configuration.lookup_matrix_directory+configuration.lookup_matrix_path,
                     coord_type = 0,
                     detection_type =1)
    else:
        pass
    
    
    #==STEP8:车辆目标空间位置计算及显示
    # media_type: 0: image; 1: video; detection_type: 0 ==> box;  1 ==> segment
    if configuration.media_type == 0 and configuration.detection_type == 0:
        trackDisplay(cur_path+configuration.real_time_img_path[0], 
                     cur_path+configuration.hd_img_path,
                     cur_path+configuration.box_save_track_path,
                     cur_path+configuration.lookup_matrix_directory+configuration.lookup_matrix_path,
                     coord_type = 1,    # coord: 0:原始坐标；1:变换后坐标
                     detection_type =0)     
    elif configuration.media_type == 1 and configuration.detection_type == 0:
        traceDisplay(cur_path+configuration.base_img_path, 
                     cur_path+configuration.hd_img_path,
                     cur_path+configuration.box_save_trace_path,
                     cur_path+configuration.lookup_matrix_directory+configuration.lookup_matrix_path,
                     coord_type = 1,    # coord: 0:原始坐标；1:变换后坐标
                     detection_type =0)    
    elif configuration.media_type == 0 and configuration.detection_type == 1:
        trackDisplay(cur_path+configuration.real_time_img_path[0], 
                     cur_path+configuration.hd_img_path,
                     cur_path+configuration.seg_save_track_path,
                     cur_path+configuration.lookup_matrix_directory+configuration.lookup_matrix_path,
                     coord_type = 1,
                     detection_type =1)
    elif configuration.media_type == 1 and configuration.detection_type == 1: 
        traceDisplay(cur_path+configuration.base_img_path, 
                     cur_path+configuration.hd_img_path,
                     cur_path+configuration.seg_save_trace_path,
                     cur_path+configuration.lookup_matrix_directory+configuration.lookup_matrix_path,
                     coord_type = 1,
                     detection_type =1)
    else:
        pass
    
    '''

    ####################其他乱七八糟的工具，包含测试代码#######################
    #Misc.test_shapely()
    #Misc.test_getCoord(cur_path+configuration.hd_img_path)
    #test_image_path = ['/images/3d_n2s_original.jpg', '/images/3d_n2s_segment.png', '/images/3d_n2s_3d_detection.png']     #['/images/3d_s2n_original.jpg', '/images/3d_s2n_segment.png', '/images/3d_s2n_3d_detection.png']
    #Misc.test_image(cur_path,test_image_path)
    #Misc.video_trim(cur_path, configurationMisc.screen_capture_video_path)

    #Misc.img_format_transform(cur_path, '/images/fusion_result/' + configuration.flow_type + '/png/','/images/fusion_result/' + configuration.flow_type + '/jpg/')
    #Misc.img_to_video(cur_path, '/images/fusion_result/' + configuration.flow_type + '/jpg/', '/videos/3D_fusion_result_' +  configuration.flow_type + '.mp4', framerate=4 )
    
    #Misc.img_format_transform(cur_path, '/img_tmp/img_for_detect/turn_flow/turn_flow_png/s2n/','/img_tmp/img_for_detect/turn_flow/turn_flow_jpg/s2n/')
    #Misc.img_format_transform(cur_path, '/img_tmp/img_for_detect/turn_flow/turn_flow_png/n2s/','/img_tmp/img_for_detect/turn_flow/turn_flow_jpg/n2s/')
    #Misc.img_format_transform(cur_path, '/img_tmp/img_for_detect/turn_flow/turn_flow_png/e2w/','/img_tmp/img_for_detect/turn_flow/turn_flow_jpg/e2w/')
    #Misc.img_format_transform(cur_path, '/img_tmp/img_for_detect/turn_flow/turn_flow_png/w2e/','/img_tmp/img_for_detect/turn_flow/turn_flow_jpg/w2e/')
    ######################################################################

    #singleDirectionApp(cur_path, configuration_s2n)
    #singleDirectionApp(cur_path, configuration_n2s)
    #singleDirectionApp(cur_path, configuration_e2w)
    #singleDirectionApp(cur_path, configuration_w2e)

    '''
    stage = 'MultiFusion' # 'DataPreprocessing', 'VehicleDetection', 'HDPositioning', 'MultiFusion'
    direction = 'w2e'   # 's2n', 'n2s', 'e2w', 'w2e'  
    if stage == 'DataPreprocessing':
        step_number = 2     # 1:验证流程第一步：在图像上选点; 2: 验证流程第二步：在高精地图上选点; 3:三角分割+仿射变换等
        #第一部分：数据预处理，得到的结果是各方向的映射矩阵(存储为csv)
        print('/\/\/\ 第一部分 /\/\/\：数据预处理 -- 当前时间:' + str(datetime.datetime.now()) +  ' /\/\/\ ' )
        dataPreprocessing(cur_path, configuration_s2n,configuration_n2s,configuration_e2w,configuration_w2e,direction = direction, step_number = step_number)
    elif stage == 'VehicleDetection':
        #第二部分：图像识别，得到的结果是各方向图像识别的结果(存储为csv)
        pass
    elif stage == 'HDPositioning':
        #第三部分：单方向车辆目标高精度空间定位(存储为csv)
        print('/\/\/\ 第三部分 /\/\/\：单方向车辆目标高精度空间定位 -- 当前时间:' + str(datetime.datetime.now()) +  ' /\/\/\ ' )
        hdPositioning(cur_path, configuration_s2n,configuration_n2s,configuration_e2w,configuration_w2e,direction = direction)        # 's2n', 'n2s', 'w2e'
    elif stage == 'MultiFusion':
        #第四部分：多方向融合(存储为csv)
        print('/\/\/\ 第四部分 /\/\/\：多方向融合 -- 当前时间:' + str(datetime.datetime.now()) +  ' /\/\/\ ' )
        #multiFusion_normal(cur_path, configuration.media_type, configuration_s2n,configuration_n2s,configuration_e2w,configuration_w2e)
        #multiFusion_3D(cur_path, configuration, configuration_s2n,configuration_n2s,configuration_e2w,configuration_w2e)
        multiFusion_3D_frames(cur_path, configuration, configuration_s2n,configuration_n2s,configuration_e2w,configuration_w2e)
    '''
    