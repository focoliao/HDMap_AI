#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from ultralytics import YOLO
import pandas as pd
import json
from matplotlib.patches import Rectangle, Circle, Polygon
from shapely.plotting import plot_polygon, plot_points
from shapely.geometry import MultiPoint
from shapely.ops import triangulate
import os

colors_display=['#FFC0CB','#FFFFFF','#000000','#FF00FF','#555555','#666666','#111111','#222222','#333333','#444444','#00FFFF','#FF0000','#777777','#888888','#999999','#101010','#151515','#202020']
def trackDisplay(background_image_path, hd_image_path, save_track_path, hd_save_track_path, save_matrix_path, image_size, coord_type, detection_type):
    if coord_type == 0: # coord: 0:原始坐标；1:变换后坐标
        # 1.读取背景图片
        img_background = cv.imread(background_image_path, cv.IMREAD_UNCHANGED)
        plt.figure('Track Display - Source Map')
        plt.imshow(img_background,cmap = 'gray') #
        if detection_type == 0: # detection_type: 0 ==> box;  1 ==> segment
            # 2.读取定位数据
            df = pd.read_csv(save_track_path)
            # 3.将所有定位打印在背景图上
            for i in range(len(df)):
                plt.gca().add_patch(Rectangle((int(df['x_lu'][i]),int(df['y_rd'][i])),int(df['x_rd'][i])-int(df['x_lu'][i]),int(df['y_lu'][i])-int(df['y_rd'][i]),linewidth=1,edgecolor=colors[int(df['id'][i])%18],facecolor='none'))
            plt.show()
        elif detection_type == 1:   # detection_type: 0 ==> box;  1 ==> segment
            # 2.读取定位数据
            df = pd.read_csv(save_track_path)
            # 3.将所有定位打印在背景图上
            for i in range(len(df)):
                plt.gca().add_patch(Polygon(eval(df['contour'][i]),color=colors_display[int(df['id'][i])%18], alpha=0.5))
            plt.show()
        else:
            pass
    elif coord_type == 1: # coord: 0:原始坐标；1:变换后坐标
        # 1.读取背景图片
        img_background = cv.imread(hd_image_path, cv.IMREAD_UNCHANGED)
        plt.figure('Track Display - Source Map')
        plt.imshow(img_background,cmap = 'gray') #
        if detection_type == 0: # detection_type: 0 ==> box;  1 ==> segment
            # 2.读取定位数据
            df = pd.read_csv(save_track_path)
            # 3.将所有定位打印在背景图上
            # 构造一个image_size的矩阵
            rows = [(0,0)] * image_size[0]
            lookup_matrix_list = []
            for i in range(image_size[1]):
                lookup_matrix_list.append(rows)
            lookup_matrix = np.array(lookup_matrix_list)
            #读取提前存好的查找矩阵
            lookup_matrix_df = pd.read_csv(save_matrix_path) 
            #将dataframe转换成矩阵
            for i in range(image_size[1]):
                for j in range(image_size[0]):
                    lookup_matrix[i][j] = json.loads(lookup_matrix_df.loc[i,str(j)])
            #进行数据转换及显示
            for i in range(len(df)):
                [x_left_up, y_left_up] = lookup_matrix[int(df['y_lu'][i])][int(df['x_lu'][i])]   #左上角点[x_left_up, y_left_up];
                [x_right_down, y_right_down] = lookup_matrix[int(df['y_rd'][i])][int(df['x_rd'][i])] #右下角点[x_right_down, y_right_down]
                width = x_right_down - x_left_up    # 宽度 = x坐标：右-左 
                height = y_right_down - y_left_up   # 高度 = y坐标：下-上

                plt.gca().add_patch(Rectangle((x_left_up, y_right_down),width,height,linewidth=1,edgecolor=colors_display[int(df['id'][i])%18],facecolor='none'))
            plt.show()
        elif detection_type == 1:   # detection_type: 0 ==> box;  1 ==> segment
            # 2.读取定位数据
            df = pd.read_csv(save_track_path)
            # 3.将所有定位打印在背景图上
            # 构造一个image_size的矩阵
            rows = [(0,0)] * image_size[0]
            lookup_matrix_list = []
            for i in range(image_size[1]):
                lookup_matrix_list.append(rows)
            lookup_matrix = np.array(lookup_matrix_list)
            #读取提前存好的查找矩阵
            lookup_matrix_df = pd.read_csv(save_matrix_path) 
            #将dataframe转换成矩阵
            for i in range(image_size[1]):
                for j in range(image_size[0]):
                    lookup_matrix[i][j] = json.loads(lookup_matrix_df.loc[i,str(j)])
            #进行数据转换及显示
            for i in range(len(df)):
                contour = []
                for item in eval(df['contour'][i]):
                    [x, y] = lookup_matrix[int(item[1])][int(item[0])]
                    plt.gca().add_patch(Circle((x,y),linewidth=1,edgecolor=colors_display[int(df['id'][i])%18],facecolor=colors_display[int(df['id'][i])%18]))
                    if (x != 0) and (y != 0):
                        contour.append([x,y])
                df.loc[i,'contour'] = str(contour)  #将图像轨迹更新为hd轨迹
                if contour != []:
                    plt.gca().add_patch(Polygon(contour,color=colors_display[int(df['id'][i])%18], alpha=0.5))
            df.to_csv(hd_save_track_path)   #存储hd轨迹
            plt.show()
    return

def traceDisplay(background_image_path, hd_image_path, save_trace_path, save_matrix_path, image_size, video_rescale, coord_type, detection_type):
    if coord_type == 0: # coord: 0:原始坐标；1:变换后坐标
        # 1.读取背景图片
        img_background = cv.imread(background_image_path, cv.IMREAD_UNCHANGED)
        plt.figure('Trace Display - Source Map')
        plt.imshow(img_background,cmap = 'gray') #
        if detection_type == 0: # detection_type: 0 ==> box;  1 ==> segment
            # 2.读取轨迹数据
            df = pd.read_csv(save_trace_path)
            frames = {'targets':[]}
            for i in range(len(df)):
                cur_json = json.loads(df.targets[i]) # 读取当前时刻目标 => cur_json
                content = []
                for item in cur_json:
                    content.append({'obj_ID':item['obj_ID'],'x_lu':item['x_lu'],'y_lu':item['y_lu'],'x_rd':item['x_rd'],'y_rd':item['y_rd'],'x_center':item['x_center'], 'y_center':item['y_center']})
                frames['targets'].append(content)
            out_df = pd.DataFrame(frames,columns=['targets'])

            # 3.将所有轨迹点打印在背景图上
            for i in range(len(out_df['targets'])):
                for item in out_df['targets'][i]:
                    x0 = int(item['x_lu']) * video_rescale[0]
                    y0 = int(item['y_rd']) * video_rescale[1]
                    x_center = int(item['x_center']) * video_rescale[0]
                    y_center = int(item['y_center']) * video_rescale[1]
                    width = (int(item['x_rd'])-int(item['x_lu'])) * video_rescale[0]
                    height = (int(item['y_lu'])-int(item['y_rd'])) * video_rescale[1]
                    #plt.gca().add_patch(Rectangle((x0, y0),width,height,linewidth=1,edgecolor=colors[int(item['obj_ID'])%18],facecolor='none'))
                    plt.gca().add_patch(Circle((x_center, y_center),linewidth=1,edgecolor=colors[int(item['obj_ID'])%18],facecolor=colors[int(item['obj_ID'])%18]))
        elif detection_type == 1:   # detection_type: 0 ==> box;  1 ==> segment
            # 2.读取轨迹数据
            df = pd.read_csv(save_trace_path)
            frames = {'targets':[]}
            for i in range(len(df)):
                cur_json = json.loads(df.targets[i]) # 读取当前时刻目标 => cur_json
                content = []
                for item in cur_json:
                    content.append({'obj_ID':item['obj_ID'],'contour':item['contour']})
                frames['targets'].append(content)
            out_df = pd.DataFrame(frames,columns=['targets'])

            # 3.将所有轨迹点打印在背景图上
            for i in range(len(out_df['targets'])):
                for item in out_df['targets'][i]:
                    for contour in item['contour']:
                        contour_x, contour_y = contour[0] * video_rescale[0], contour[1] * video_rescale[1]
                        plt.gca().add_patch(Circle((contour_x, contour_y),linewidth=1,edgecolor=colors[int(item['obj_ID'])%18],facecolor=colors[int(item['obj_ID'])%18]))
        else:
            pass
        plt.show()
    elif coord_type == 1:   # coord: 0:原始坐标；1:变换后坐标
        lookup_matrix_df = pd.read_csv(save_matrix_path)
        lookup_matrix = np.array(lookup_matrix_df)
        # 1.读取背景图片
        img_background = cv.imread(hd_image_path, cv.IMREAD_UNCHANGED)
        plt.figure('Trace Display - HD Map')
        plt.imshow(img_background,cmap = 'gray') #
        if detection_type == 0: # detection_type: 0 ==> box;  1 ==> segment
            # 2.读取轨迹数据
            df = pd.read_csv(save_trace_path)
            frames = {'targets':[]}
            for i in range(len(df)):
                cur_json = json.loads(df.targets[i]) # 读取当前时刻目标 => cur_json
                content = []
                for item in cur_json:
                    content.append({'obj_ID':item['obj_ID'],'x_lu':item['x_lu'],'y_lu':item['y_lu'],'x_rd':item['x_rd'],'y_rd':item['y_rd'],'x_center':item['x_center'], 'y_center':item['y_center']})
                frames['targets'].append(content)
            out_df = pd.DataFrame(frames,columns=['targets'])
            # 3.将所有轨迹点打印在背景图上
            # 构造一个image_size的矩阵
            rows = [(0,0)] * image_size[0],
            lookup_matrix_list = []
            for i in range(image_size[1]):
                lookup_matrix_list.append(rows)
            lookup_matrix = np.array(lookup_matrix_list)
            #读取提前存好的查找矩阵
            lookup_matrix_df = pd.read_csv(save_matrix_path) 
            #将dataframe转换成矩阵
            for i in range(image_size[1]):
                for j in range(image_size[0]):
                    lookup_matrix[i][j] = json.loads(lookup_matrix_df.loc[i,str(j)])
            #进行数据转换及显示
            for i in range(len(out_df['targets'])):
                for item in out_df['targets'][i]:
                    #限制坐标范围，否则会出现超出查找表范围的错误
                    if round(int(item['y_lu']) * video_rescale[1]) < 0:
                        x_left_up_0 = 0
                    elif round(int(item['y_lu']) * video_rescale[1]) > image_size[1]-1:
                        x_left_up_0 = image_size[1]-1
                    else:
                        x_left_up_0 = round(int(item['y_lu']) * video_rescale[1])
                    #限制坐标范围，否则会出现超出查找表范围的错误
                    if round(int(item['x_lu']) * video_rescale[0]) < 0:
                        y_left_up_0 = 0
                    elif round(int(item['x_lu']) * video_rescale[0]) > image_size[0]-1:
                        y_left_up_0 = image_size[0]-1
                    else:
                        y_left_up_0 = round(int(item['x_lu']) * video_rescale[0])
                    #限制坐标范围，否则会出现超出查找表范围的错误
                    if round(int(item['y_rd']) * video_rescale[1]) < 0:
                        x_right_dow_0 = 0
                    elif round(int(item['y_rd']) * video_rescale[1]) > image_size[1]-1:
                        x_right_dow_0 = image_size[1]-1
                    else:
                        x_right_dow_0 = round(int(item['y_rd']) * video_rescale[1])
                    #限制坐标范围，否则会出现超出查找表范围的错误
                    if round(int(item['x_rd']) * video_rescale[0]) < 0:
                        y_right_down_0 = 0
                    elif round(int(item['x_rd']) * video_rescale[0]) > image_size[0]-1:
                        y_right_down_0 = image_size[0]-1
                    else:
                        y_right_down_0 = round(int(item['x_rd']) * video_rescale[0])
                    #限制坐标范围，否则会出现超出查找表范围的错误
                    if round(int(item['y_center']) * video_rescale[1]) > image_size[0]-1:
                        x_center_0 = image_size[0]-1
                    elif round(int(item['y_center']) * video_rescale[1]) < 0:
                        x_center_0 = 0
                    else:
                        x_center_0 = round(int(item['y_center']) * video_rescale[1])
                    #限制坐标范围，否则会出现超出查找表范围的错误
                    if round(int(item['x_center']) * video_rescale[0]) > image_size[1]-1:
                        y_center_0 = image_size[1]-1
                    elif round(int(item['x_center']) * video_rescale[0]) < 0:
                        y_center_0 = 0
                    else:
                        y_center_0 = round(int(item['x_center']) * video_rescale[0])

                    [x_left_up, y_left_up] = lookup_matrix[x_left_up_0][y_left_up_0]   #box左上角点[x_left_up, y_left_up];
                    [x_right_down, y_right_down] = lookup_matrix[x_right_dow_0][y_right_down_0] #box右下角点[x_right_down, y_right_down]
                    [x_center, y_center] = lookup_matrix[x_center_0][y_center_0]   #box中心点[x_center, y_center];
                    width = x_right_down - x_left_up    # 宽度 = x坐标：右-左 
                    height = y_right_down - y_left_up   # 高度 = y坐标：下-上
                    plt.gca().add_patch(Circle((x_center, y_center),10,edgecolor=colors[int(item['obj_ID'])%18],facecolor=colors[int(item['obj_ID'])%18]))
        elif detection_type == 1:   # detection_type: 0 ==> box;  1 ==> segment
            # 2.读取轨迹数据
            df = pd.read_csv(save_trace_path)
            frames = {'targets':[]}
            for i in range(len(df)):
                cur_json = json.loads(df.targets[i]) # 读取当前时刻目标 => cur_json
                content = []
                for item in cur_json:
                    content.append({'obj_ID':item['obj_ID'],'contour':item['contour']})
                frames['targets'].append(content)
            out_df = pd.DataFrame(frames,columns=['targets'])

            # 3.将所有轨迹点打印在背景图上
            # 构造一个image_size的矩阵
            rows = [(0,0)] * image_size[0]
            lookup_matrix_list = []
            for i in range(image_size[1]):
                lookup_matrix_list.append(rows)
            lookup_matrix = np.array(lookup_matrix_list)
            #读取提前存好的查找矩阵
            lookup_matrix_df = pd.read_csv(save_matrix_path) 
            #将dataframe转换成矩阵
            for i in range(image_size[1]):
                for j in range(image_size[0]):
                    lookup_matrix[i][j] = json.loads(lookup_matrix_df.loc[i,str(j)])
            #进行数据转换及显示
            for i in range(len(out_df['targets'])):
                for item in out_df['targets'][i]:
                    for contour in item['contour']:
                        #限制坐标范围，否则会出现超出查找表范围的错误
                        if round(int(contour[1]) * video_rescale[1]) < 0:
                            contour_x = 0
                        elif round(int(contour[1]) * video_rescale[1]) > image_size[1]-1:
                            contour_x = image_size[1]-1
                        else:
                            contour_x = round(int(contour[1]) * video_rescale[1])
                        #限制坐标范围，否则会出现超出查找表范围的错误
                        if round(int(contour[0]) * video_rescale[0]) < 0:
                            contour_y = 0
                        elif round(int(contour[0]) * video_rescale[0]) > image_size[0]-1:
                            contour_y = image_size[0]-1
                        else:
                            contour_y = round(int(contour[0]) * video_rescale[0])

                        plt.gca().add_patch(Circle((lookup_matrix[contour_x][contour_y]),linewidth=1,edgecolor=colors[int(item['obj_ID'])%18],facecolor=colors[int(item['obj_ID'])%18]))
        else:
            pass
        plt.show()
    else:
        pass
    return

colors=['#FF0000','#00ff00','#ffff00','#ff00ff','#00ffff','#000000']

def display_triangulate(points_list, background_image_path):
    if len(points_list) > 2:
        points = MultiPoint(points_list)
        triangles = triangulate(points)
        img_background = cv.imread(background_image_path, cv.IMREAD_UNCHANGED)
        plt.figure('Triangulation Display')
        plt.imshow(img_background,cmap = 'gray') #
        for i in range(len(triangles)):
            triangle = triangles[i]
            plot_polygon(triangle, add_points=False, color=colors[i%6])
        plot_points(points, color='GRAY')
        plt.show()

    return

def trackDisplay_3D(background_image_path, input_csvs_directory, image_size, save_matrix_path, hd_trace_3D_path):
    # 1.读取背景图片
    img_background = cv.imread(background_image_path, cv.IMREAD_UNCHANGED)
    plt.figure('3D Display')
    plt.imshow(img_background,cmap = 'gray') #
    # 2.读取查找矩阵
    # 构造一个image_size的矩阵
    rows = [(0,0)] * image_size[0]
    lookup_matrix_list = []
    for i in range(image_size[1]):
        lookup_matrix_list.append(rows)
    lookup_matrix = np.array(lookup_matrix_list)
    #读取提前存好的查找矩阵
    lookup_matrix_df = pd.read_csv(save_matrix_path) 
    #将dataframe转换成矩阵
    for i in range(image_size[1]):
        for j in range(image_size[0]):
            lookup_matrix[i][j] = json.loads(lookup_matrix_df.loc[i,str(j)])
    
    # 3.循环将结果显示在背景图上
    files = os.listdir(input_csvs_directory)
    files.sort()    #文件名排序
    hd_out_3D =  {'contours':[]}
    for file in files:
        if file == '.DS_Store':
            pass
        else:
            # 2.读取定位数据
            df = pd.read_csv(input_csvs_directory+file)
            #进行数据转换及显示
            contours = []
            for i in range(len(df)):
                contour = []
                target = json.loads(df.targets[i])
                arr = target['arr']
                positions = arr[0]['position']
                items = [[positions[0],positions[1]],[positions[2],positions[3]],[positions[4],positions[5]],[positions[6],positions[7]]]
                for item in items:
                    x_img = image_size[1]-1 if item[1] > image_size[1]-1 else (0 if item[1] < 0 else item[1])
                    y_img = image_size[0]-1 if item[0] > image_size[0]-1 else (0 if item[0] < 0 else item[0])
                    [x, y] = lookup_matrix[int(x_img)][int(y_img)]
                    plt.gca().add_patch(Circle((x,y),linewidth=1,edgecolor=colors_display[i%18],facecolor=colors_display[i%18]))
                    if (x != 0) and (y != 0):
                        contour.append([x,y])
                if contour != []:
                    plt.gca().add_patch(Polygon(contour,color=colors_display[i%18], alpha=0.3))
                    contours.append(contour)
                    
            hd_out_3D['contours'].append(contours)
    df_out = pd.DataFrame(hd_out_3D,columns=['contours'])
    df_out.to_csv(hd_trace_3D_path)   #存储hd轨迹
    plt.show()
    
    return