#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
from shapely.geometry import MultiPoint
from shapely.ops import triangulate
from shapely.plotting import plot_polygon, plot_points
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle, Circle
import configuration, configurationMisc
import os
from PIL import Image
import ffmpeg
import matplotlib


colors=['#FF0000','#00ff00','#ffff00','#ff00ff','#00ffff','#000000']

def display_triangulate(points_list):
    if len(points_list) > 2:
        points = MultiPoint(points_list)
        print(points)
        triangles = triangulate(points)
        background_image_path = os.getcwd() + configuration.hd_img_path
        img_background = cv.imread(background_image_path, cv.IMREAD_UNCHANGED)
        plt.figure('Track Display - Source Map')
        plt.imshow(img_background,cmap = 'gray') #
        for i in range(len(triangles)):
            triangle = triangles[i]
            plot_polygon(triangle, add_points=False, color=colors[i%6])
        plot_points(points, color='GRAY')
        plt.show()

    return

points = []
def onclick(event): 
    if event.dblclick:
        points.append((event.xdata, event.ydata))
        plt.gca().add_patch(Circle((event.xdata, event.ydata),radius=1, linewidth=1,edgecolor='r',facecolor='None'))
        plt.gca().add_patch(Circle((event.xdata, event.ydata),radius=10, linewidth=1,edgecolor='r',facecolor='None'))
        display_triangulate(points)
        print(points) 
        

class ClickData:
    def __init__(self, ax):
        self.xs = []
        self.ys = []
        self.cid = ax.figure.canvas.mpl_connect('button_press_event', self.onclick)

    def onclick(self, event):
        print('Clicked:', event.xdata, event.ydata)
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
    
    def get_data(self):
        return self.xs, self.ys

def test_getCoord(image_path):
    #图片路径
    img = mpimg.imread(image_path)
    plt.figure('Selection Map - Source Map')
    ax = plt.imshow(img)
    fig = ax.get_figure()
    data = ClickData(ax)
    plt.show()

    x, y = data.get_data() 
    print(x, y) 
    return

def test_image(cur_path, image_path):
    for i in range(len(image_path)):
        img_to_display =  mpimg.imread(cur_path + image_path[i])
        plt.figure('Image:' + str(i))
        plt.imshow(img_to_display) #
    plt.show()

    return

def img_format_transform(cur_path, input_images_directory, output_images_directory):

    files = os.listdir(cur_path+input_images_directory)
    files.sort()    #文件名排序
    for file in files:
        if file == '.DS_Store':
            pass
        else:
            img = Image.open(cur_path + input_images_directory + file)
            img = img.convert('RGB')
            img.save(cur_path + output_images_directory + str(file).replace('.png', '.jpg'), quality = 95)
    return

def img_to_video(cur_path, input_img_directory, output_video_save_path, framerate):

    # 编码为视频 
    (
        ffmpeg
        .input(cur_path + input_img_directory + '*.jpg', pattern_type='glob', framerate=framerate)
        .output(cur_path + output_video_save_path, vcodec='libx264', acodec='aac', audio_bitrate='128k')
        .overwrite_output()
        .run()
    )
    return


#视频分割，将一个视频的左上角、右上角、左下角、右下角分割成四个视频
def video_trim(cur_path, video_path):
    # 提取视频帧
    if len(os.listdir(cur_path + '/img_tmp/video_frames')) < 2:
        print('ffmpeg -i ' + cur_path + video_path + ' -r 30 ' + cur_path + '/img_tmp/video_frames/' + '/img%05d.png')
        os.system('ffmpeg -i ' + cur_path + video_path + ' -r 30 ' + cur_path + '/img_tmp/video_frames/' + '/img%05d.png') 

    # 定义裁剪区域
    left_top = (0.5, 0.5, 1726.5, 972.5)
    right_top = (1727.5, 0.5, 3453.5, 972.5) 
    left_bottom = (0.5, 1082.5, 1726.5, 2054.5)
    right_bottom = (1727.5, 1082.5, 3453.5, 2054.5)

    # 遍历图片序列
    if len(os.listdir(cur_path + '/img_tmp/left_top')) < 2:
        for img_name in os.listdir(cur_path + '/img_tmp/video_frames'):
            if img_name == '.DS_Store':
                pass
            else:
                img = Image.open(cur_path + '/img_tmp/video_frames/' + img_name)

                # 裁剪图片
                img_lt = img.crop(left_top)
                img_rt = img.crop(right_top)
                img_lb = img.crop(left_bottom) 
                img_rb = img.crop(right_bottom)

                # 保存裁剪图片
                img_lt.save(cur_path + '/img_tmp/' + 'left_top/' + img_name)
                img_rt.save(cur_path + '/img_tmp/' + 'right_top/' + img_name)
                img_lb.save(cur_path + '/img_tmp/' + 'left_bottom/' + img_name)
                img_rb.save(cur_path + '/img_tmp/' + 'right_bottom/' + img_name)

    # 编码为视频 
    #stream = ffmpeg.input(cur_path + '/img_tmp/' + 'left_top/img%05d.png')
    #stream = ffmpeg.hflip(stream)
    #stream = ffmpeg.output(stream, cur_path + 'left_top.mp4')
    #ffmpeg.run(stream)   
    (
        ffmpeg
        .input(cur_path + '/img_tmp/' + 'left_top/*.png', pattern_type='glob', framerate=30)
        .output(cur_path + '/left_top.mp4')
        .run()
    )
    ffmpeg.input(cur_path + '/img_tmp/' + 'right_top/*.png', pattern_type='glob', framerate=30).output(cur_path + '/right_top.mp4').run() 
    ffmpeg.input(cur_path + '/img_tmp/' + 'left_bottom/*.png', pattern_type='glob', framerate=30).output(cur_path + '/left_bottom.mp4').run()
    ffmpeg.input(cur_path + '/img_tmp/' + 'right_bottom/*.png', pattern_type='glob', framerate=30).output(cur_path + '/right_bottom.mp4').run()
    return

