#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.image as mpimg
from matplotlib.patches import Polygon
import numpy as np
from SingleDirectionApp import singleDirectionPreprocessing


def multiFusion_normal(cur_path, media_type, configuration_single_direction_s2n,configuration_single_direction_n2s,configuration_single_direction_e2w,configuration_single_direction_w2e):
    #2.加载背景图片
    img = mpimg.imread(cur_path + configuration_single_direction_s2n.hd_img_path)
    plt.figure('多路叠加结果')
    plt.imshow(img)

    #3.显示多方向叠加结果
    if media_type == 0: # media_type: 0: image; 1: video
        #3.1 读取南向北结果并显示
        df_s2n = pd.read_csv(cur_path + configuration_single_direction_s2n.hd_save_track_path)
        for i in range(len(df_s2n)):
            if (eval(df_s2n['contour'][i])) != []:
                plt.gca().add_patch(Polygon(eval(df_s2n['contour'][i]),color='r', alpha=0.5))
                #contour_list_s2n = eval(df_s2n['contour'][i])
                #[x_s2n, y_s2n] = contour_list_s2n[int(len(contour_list_s2n)/2)]
                #plt.text(x_s2n , y_s2n, df_s2n['uni_id'][i], color = "r") #显示唯一编号，以更方便对应
        #3.2 读取北向南结果，数据旋转180度并显示
        df_n2s = pd.read_csv(cur_path + configuration_single_direction_n2s.hd_save_track_path)
        for i in range(len(df_n2s)):
            if (eval(df_n2s['contour'][i])) != []:
                #以南向北为底，北向南需要旋转180度显示
                contour_new_n2s = configuration_single_direction_n2s.HD_size-np.array(eval(df_n2s['contour'][i]))
                plt.gca().add_patch(Polygon(contour_new_n2s,color='g', alpha=0.5))
                #contour_list_n2s = eval(df_n2s['contour'][i])
                #[x_n2s, y_n2s] = np.array(configuration_single_direction_n2s.HD_size)-contour_list_n2s[int(len(contour_list_n2s)/2)]
                #plt.text(x_n2s , y_n2s, df_n2s['uni_id'][i], color = "g") #显示唯一编号，以更方便对应
        #3.3 读取东向西结果，数据旋转270度并显示
        df_e2w = pd.read_csv(cur_path + configuration_single_direction_e2w.hd_save_track_path)
        for i in range(len(df_e2w)):
            if (eval(df_e2w['contour'][i])) != []:
                #以南向北为底，东向西需要旋转270度显示
                contour_old = np.array(eval(df_e2w['contour'][i]))
                contour_new_x = contour_old[:,1]    # 新x为原y
                contour_new_y = configuration_single_direction_e2w.HD_size[1] - contour_old[:,0]    #新y为Y0-原x
                contour_new_e2w = np.concatenate((contour_new_x.reshape(len(contour_new_x),1),contour_new_y.reshape(len(contour_new_y),1)), axis=1) #拼接成矩阵
                plt.gca().add_patch(Polygon(contour_new_e2w,color='y', alpha=0.5))
                #contour_list_e2w = eval(df_e2w['contour'][i])
                #[x_e2w, y_e2w] = np.array(configuration_single_direction_e2w.HD_size)-contour_list_e2w[int(len(contour_list_e2w)/2)]
                #plt.text(x_e2w , y_e2w, df_e2w['uni_id'][i], color = "g") #显示唯一编号，以更方便对应
        #3.4 读取西向东结果，数据旋转90度并显示
        df_w2e = pd.read_csv(cur_path + configuration_single_direction_w2e.hd_save_track_path)
        for i in range(len(df_w2e)):
            if (eval(df_w2e['contour'][i])) != []:
                plt.gca().add_patch(Polygon(eval(df_w2e['contour'][i]),color='b', alpha=0.5))
        plt.show()
    
    return

def multiFusion_3D(cur_path, configuration, configuration_single_direction_s2n,configuration_single_direction_n2s,configuration_single_direction_e2w,configuration_single_direction_w2e):
    #2.加载背景图片
    img = mpimg.imread(cur_path + configuration_single_direction_s2n.hd_img_path)
    plt.figure('多路叠加结果')
    plt.imshow(img)

    #3.显示多方向叠加结果
    if configuration.media_type == 0: # media_type: 0: image; 1: video
        #3.1 读取南向北结果并显示
        df_s2n = pd.read_csv(cur_path + configuration_single_direction_s2n.hd_trace_3D_path)
        for i in range(len(df_s2n)):
            if (eval(df_s2n['contour'][i])) != []:
                plt.gca().add_patch(Polygon(eval(df_s2n['contour'][i]),color='r', alpha=0.5))
                contour_list_s2n = eval(df_s2n['contour'][i])
        #3.2 读取北向南结果，数据旋转180度并显示
        df_n2s = pd.read_csv(cur_path + configuration_single_direction_n2s.hd_trace_3D_path)
        for i in range(len(df_n2s)):
            if (eval(df_n2s['contour'][i])) != []:
                #以南向北为底，北向南需要旋转180度显示
                contour_new_n2s = configuration_single_direction_n2s.HD_size-np.array(eval(df_n2s['contour'][i]))
                plt.gca().add_patch(Polygon(contour_new_n2s,color='g', alpha=0.5))
        #3.3 读取东向西结果，数据逆时针旋转90度并显示
        df_e2w = pd.read_csv(cur_path + configuration_single_direction_e2w.hd_trace_3D_path)
        for i in range(len(df_e2w)):
            if (eval(df_e2w['contour'][i])) != []:
                #以南向北为底，东向西需要逆时针旋转90度显示(下面转换算法只适合正方形)
                contour_old = np.array(eval(df_e2w['contour'][i]))
                contour_new_x = contour_old[:,1]    # 新x为原y
                contour_new_y = configuration_single_direction_e2w.HD_size[1] - contour_old[:,0]    #新y为Y0-原x
                contour_new_e2w = np.concatenate((contour_new_x.reshape(len(contour_new_x),1),contour_new_y.reshape(len(contour_new_y),1)), axis=1) #拼接成矩阵
                plt.gca().add_patch(Polygon(contour_new_e2w, color='y', alpha=0.5))
        #3.4 读取西向东结果，数据顺时针旋转90度并显示
        df_w2e = pd.read_csv(cur_path + configuration_single_direction_w2e.hd_trace_3D_path)
        for i in range(len(df_w2e)):
            if (eval(df_w2e['contour'][i])) != []:
                #以南向北为底，东向西需要顺时针旋转90度显示(下面转换算法只适合正方形)
                contour_old = np.array(eval(df_w2e['contour'][i]))
                contour_new_x = configuration_single_direction_w2e.HD_size[0] - contour_old[:,1]    #新x为X0-原y
                contour_new_y = contour_old[:,0]    # 新y为原x
                contour_new_w2e = np.concatenate((contour_new_x.reshape(len(contour_new_x),1),contour_new_y.reshape(len(contour_new_y),1)), axis=1) #拼接成矩阵
                plt.gca().add_patch(Polygon(contour_new_w2e,color='b', alpha=0.5))
        plt.show()
    return

def multiFusion_3D_frames(cur_path, configuration, configuration_single_direction_s2n,configuration_single_direction_n2s,configuration_single_direction_e2w,configuration_single_direction_w2e):
    

    #2. 加载各方向结果
    df_s2n = pd.read_csv(cur_path + configuration_single_direction_s2n.hd_trace_3D_path)
    df_n2s = pd.read_csv(cur_path + configuration_single_direction_n2s.hd_trace_3D_path)
    df_e2w = pd.read_csv(cur_path + configuration_single_direction_e2w.hd_trace_3D_path)
    df_w2e = pd.read_csv(cur_path + configuration_single_direction_w2e.hd_trace_3D_path)

    max_length = max(len(df_s2n),len(df_n2s),len(df_e2w),len(df_w2e))
    for i in range(max_length):
        print('Frame number: ' + str(i+1))
        # 加载背景图片
        img = mpimg.imread(cur_path + configuration_single_direction_s2n.hd_img_path)
        plt.figure('多路叠加结果，第' + str(i) + '帧')
        plt.imshow(img)
        if i < len(df_s2n):
            if (eval(df_s2n['contours'][i])) != []:
                countours_tmp = eval(df_s2n['contours'][i])
                for item in countours_tmp:
                    plt.gca().add_patch(Polygon(item,color='r', alpha=0.5))
        if i < len(df_n2s):
            if (eval(df_n2s['contours'][i])) != []:
                countours_tmp = eval(df_n2s['contours'][i])
                for item in countours_tmp:
                    #以南向北为底，北向南需要旋转180度显示
                    contour_new_n2s = configuration_single_direction_n2s.HD_size-np.array(item)
                    plt.gca().add_patch(Polygon(contour_new_n2s,color='g', alpha=0.5))
        if i < len(df_e2w):
            if (eval(df_e2w['contours'][i])) != []:
                countours_tmp = eval(df_e2w['contours'][i])
                for item in countours_tmp:
                    #以南向北为底，东向西需要逆时针旋转90度显示(下面转换算法只适合正方形)
                    contour_old = np.array(item)
                    contour_new_x = contour_old[:,1]    # 新x为原y
                    contour_new_y = configuration_single_direction_e2w.HD_size[1] - contour_old[:,0]    #新y为Y0-原x
                    contour_new_e2w = np.concatenate((contour_new_x.reshape(len(contour_new_x),1),contour_new_y.reshape(len(contour_new_y),1)), axis=1) #拼接成矩阵
                    plt.gca().add_patch(Polygon(contour_new_e2w, color='y', alpha=0.5))
        if i < len(df_w2e):
            if (eval(df_w2e['contours'][i])) != []:
                countours_tmp = eval(df_w2e['contours'][i])
                for item in countours_tmp:
                    #以南向北为底，东向西需要顺时针旋转90度显示(下面转换算法只适合正方形)
                    contour_old = np.array(item)
                    contour_new_x = configuration_single_direction_w2e.HD_size[0] - contour_old[:,1]    #新x为X0-原y
                    contour_new_y = contour_old[:,0]    # 新y为原x
                    contour_new_w2e = np.concatenate((contour_new_x.reshape(len(contour_new_x),1),contour_new_y.reshape(len(contour_new_y),1)), axis=1) #拼接成矩阵
                    plt.gca().add_patch(Polygon(contour_new_w2e,color='b', alpha=0.5))
        
        #mpimg.imsave(cur_path + configuration.fusion_save_directory + 'fusion_frame_' + str(i) + '.png', img)
        plt.savefig(cur_path + configuration.fusion_save_directory + 'img' + '%05d' % (i+1)  + '.png', dpi=200)
        #plt.show()
        plt.close()    

    return