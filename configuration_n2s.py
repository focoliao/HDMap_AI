#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'foco_liao'

import configuration

image_size = configuration.image_size
HD_size = configuration.HD_size

img_path_4_selection = ['/images/n2s_selection_img1.png','/images/n2s_selection_img2.png','/images/n2s_selection_img3.png']
hd_img_path_4_selection = ['/images/hd_img_n2s.png']

base_img_path = '/images/n2s_base_img.png'
hd_img_path = '/images/hd_img_n2s.png'

screen_path = '/images/screen.png'
edge_detection_save_directory = '/runs/edgeDetection/'
pre_segment_src_save_directory = '/runs/preSegmentSrc/n2s/'
pre_segment_src_pre = 'src_segment_n2s'
img_format = '.png'

save_img_points_path = '/csvs/selected_img_points_n2s.csv'
save_hd_points_path = '/csvs/selected_hd_points_n2s.csv'

pre_segment_dst_save_directory = '/runs/preSegmentDst/n2s/'
pre_segment_dst_pre = 'dst_segment_n2s'

step3_2_edge_image_path = '/images/step3-2_edge_image.jpg'

lookup_matrix_directory = '/runs/lookupMatrix/n2s/'

lookup_matrix_path = '/csvs/lookup_matrix_n2s.csv'

real_time_img_path = ['/images/n2s_real_time_img.png']   #实时图像的相对路径

real_time_video_path = '/videos/n2s_detection_video.mp4'

box_save_track_path = '/csvs/box_track_data_image_n2s.csv' #识别后的车辆位置写回csv地址-box
box_save_trace_path = '/csvs/box_trace_data_video_n2s.csv' #识别后的车辆轨迹写回csv地址-box

seg_save_track_path = '/csvs/seg_track_data_image_n2s.csv' #识别后的车辆位置写回csv地址-segment
seg_save_trace_path = '/csvs/seg_trace_data_video_n2s.csv' #识别后的车辆轨迹写回csv地址-segment

hd_save_track_path = '/csvs/hd_track_data_image_n2s.csv' #识别后的车辆位置写回csv地址-hd map
hd_save_trace_path = '/csvs/hd_trace_data_video_n2s.csv' #识别后的车辆轨迹写回csv地址-hd map

hd_trace_3D_path = '/csvs/hd_trace_3D_n2s.csv' #识别后的车辆轨迹写回csv地址-hd map

csvs_directory_3D = '/csvs/3D_result/n2s/' #存储3D检测结果的csv目录

media_type = configuration.media_type  # media_type: 0: image; 1: video
detection_type = 1   # detection_type: 0 ==> box;  1 ==> segment

video_rescale = [1,1]

process_type = 0 # : 1 ==> test;  0 ==> real