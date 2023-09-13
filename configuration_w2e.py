#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'foco_liao'

import configuration

image_size = configuration.image_size
HD_size = [configuration.HD_size[1],configuration.HD_size[0]]

img_path_4_selection = ['/images/w2e_selection_img1.png','/images/w2e_selection_img2.png','/images/w2e_selection_img3.png']
hd_img_path_4_selection = ['/images/hd_img_w2e.png']

base_img_path = '/images/w2e_base_img.png'
hd_img_path = '/images/hd_img_w2e.png'

screen_path = '/images/screen.png'
edge_detection_save_directory = '/runs/edgeDetection/'
pre_segment_src_save_directory = '/runs/preSegmentSrc/w2e/'
pre_segment_src_pre = 'src_segment_w2e'
img_format = '.png'

save_img_points_path = '/csvs/selected_img_points_w2e.csv'
save_hd_points_path = '/csvs/selected_hd_points_w2e.csv'

pre_segment_dst_save_directory = '/runs/preSegmentDst/w2e/'
pre_segment_dst_pre = 'dst_segment_w2e'

step3_2_edge_image_path = '/images/step3-2_edge_image.jpg'

lookup_matrix_directory = '/runs/lookupMatrix/w2e/'

lookup_matrix_path = '/csvs/lookup_matrix_w2e.csv'

real_time_img_path = ['/images/w2e_real_time_img.png']   #实时图像的相对路径

real_time_video_path = '/videos/w2e_detection_video.mp4'

box_save_track_path = '/csvs/box_track_data_image_w2e.csv' #识别后的车辆位置写回csv地址-box
box_save_trace_path = '/csvs/box_trace_data_video_w2e.csv' #识别后的车辆轨迹写回csv地址-box

seg_save_track_path = '/csvs/seg_track_data_image_w2e.csv' #识别后的车辆位置写回csv地址-segment
seg_save_trace_path = '/csvs/seg_trace_data_video_w2e.csv' #识别后的车辆轨迹写回csv地址-segment

hd_save_track_path = '/csvs/hd_track_data_image_w2e.csv' #识别后的车辆位置写回csv地址-hd map
hd_save_trace_path = '/csvs/hd_trace_data_video_w2e.csv' #识别后的车辆轨迹写回csv地址-hd map

hd_trace_3D_path = '/csvs/hd_trace_3D_w2e.csv' #识别后的车辆轨迹写回csv地址-hd map

csvs_directory_3D = '/csvs/3D_result/w2e/' #存储3D检测结果的csv目录

media_type = configuration.media_type  # media_type: 0: image; 1: video
detection_type = 1   # detection_type: 0 ==> box;  1 ==> segment

video_rescale = [1,1]

process_type = 0 # : 1 ==> test;  0 ==> real