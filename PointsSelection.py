#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Circle
import pandas as pd

class ClickData:
    def __init__(self, ax, points_history, background_image_path):
        self.points = points_history
        self.i = 0
        self.background_image_path = background_image_path
        self.ax = ax
        self.cid = ax.figure.canvas.mpl_connect('button_press_event', self.onclick)
        tmp_points = self.points
        for i in range(len(tmp_points)):
            plt.gca().add_patch(Circle(tmp_points[i],radius=1, linewidth=1,edgecolor='r',facecolor='None'))    #画一个小圈，以显示点选的位置
            plt.text(tmp_points[i][0], tmp_points[i][1], self.i + 1, color = "r") #显示编号，以更方便对应
            self.i += 1

    def onclick(self, event):
        if event.dblclick:
            self.i += 1
            print(self.i)
            self.points.append((event.xdata, event.ydata))
            plt.gca().add_patch(Circle((event.xdata, event.ydata),radius=1, linewidth=1,edgecolor='r',facecolor='None'))    #画一个小圈，以显示点选的位置
            plt.gca().add_patch(Circle((event.xdata, event.ydata),radius=5, linewidth=1,edgecolor='r',facecolor='None'))   #画一个大圈，以更明显地显示点选的位置
            plt.text(event.xdata, event.ydata, self.i, color = "r") #显示编号，以更方便对应
    
    def get_data(self):
        return self.points


def pointsSelection_img(cur_path, img_path, save_points_path):
    df_history = pd.read_csv(cur_path+save_points_path)
    img, ax, data_img = [], [], []
    #选点操作，支持多图选点
    for i in range(len(img_path)):
        img.append(mpimg.imread(cur_path + img_path[i])) 
        plt.figure('Base Image Selection' + str(i))
        ax.append(plt.imshow(img[i]))
        if df_history['img_points'][i] != None:
            data_img.append(ClickData(ax[i], eval(df_history['img_points'][i]), cur_path + img_path[i]))
        else:
            data_img.append(ClickData(ax[i], [], cur_path + img_path[i]))
    plt.show()
    
    #多图结果存储数据汇总
    points_to_save = {'img_number': [], 'img_points':[]}
    for i in range(len(data_img)):
        points_to_save['img_number'].append(i)
        points_to_save['img_points'].append(data_img[i].get_data())
    
    #存储所选点
    df = pd.DataFrame(points_to_save,columns=['img_number', 'img_points'])
    df.to_csv(cur_path + save_points_path)   #存储hd轨迹
    
    return


def pointsSelection_hd(cur_path, hd_img_path, save_points_path, img_path_4_selection, save_img_points_path):
    # 为了方便对照，显示图像选点结果
    df_history = pd.read_csv(cur_path+save_img_points_path)
    for i in range(len(df_history)):
        img = mpimg.imread(cur_path + img_path_4_selection[i])
        plt.figure('Image Selection History:' + str(df_history['img_number'][i]))
        plt.imshow(img)
        points_i = eval(df_history['img_points'][i])
        for j in range(len(points_i)):
            plt.gca().add_patch(Circle(points_i[j],radius=1, linewidth=1,edgecolor='r',facecolor='None'))    #画一个小圈，以显示点选的位置
            #plt.gca().add_patch(Circle(points_i[j],radius=5, linewidth=1,edgecolor='r',facecolor='None'))   #画一个大圈，以更明显地显示点选的位置
            plt.text(points_i[j][0], points_i[j][1], j+1, color = "r") #显示编号，以更方便对应

    df_hd_history = pd.read_csv(cur_path+save_points_path)
    hd_points_history = []
    for i in range(len(df_hd_history)):
        hd_points_history.append([df_hd_history['img_location_x'][i],df_hd_history['img_location_y'][i]])

    #选点操作
    img = mpimg.imread(cur_path + hd_img_path[0]) 
    plt.figure('HD Image Selection')
    ax = plt.imshow(img)

    data_img = ClickData(ax, hd_points_history, cur_path + hd_img_path[0])

    plt.show()
    
    #选点结果存储
    points = data_img.get_data()

    points_to_save = {'img_location_x': [], 'img_location_y':[]}
    for i in range(len(points)):
        points_to_save['img_location_x'].append(points[i][0])
        points_to_save['img_location_y'].append(points[i][1])
    
    #存储所选点
    df = pd.DataFrame(points_to_save,columns=['img_location_x', 'img_location_y'])
    df.to_csv(cur_path + save_points_path)   #存储hd轨迹
    
    return
