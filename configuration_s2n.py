#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'foco_liao'

import configuration

image_size = configuration.image_size
HD_size = configuration.HD_size

img_path_4_selection = ['/images/s2n_selection_img1.png','/images/s2n_selection_img2.png','/images/s2n_selection_img3.png']
hd_img_path_4_selection = ['/images/hd_img_s2n.png']

base_img_path = '/images/s2n_base_img.png'
hd_img_path = '/images/hd_img_s2n.png'

screen_path = '/images/screen.png'
edge_detection_save_directory = '/runs/edgeDetection/'
pre_segment_src_save_directory = '/runs/preSegmentSrc/s2n/'
pre_segment_src_pre = 'src_segment_s2n'
img_format = '.png'

save_img_points_path = '/csvs/selected_img_points_s2n.csv'
save_hd_points_path = '/csvs/selected_hd_points_s2n.csv'

pre_segment_dst_save_directory = '/runs/preSegmentDst/s2n/'
pre_segment_dst_pre = 'dst_segment_s2n'

step3_2_edge_image_path = '/images/step3-2_edge_image.jpg'

lookup_matrix_directory = '/runs/lookupMatrix/s2n/'

lookup_matrix_path = '/csvs/lookup_matrix_s2n.csv'

real_time_img_path = ['/images/s2n_real_time_img.png']   #实时图像的相对路径

real_time_video_path = '/videos/s2n_detection_video.mp4'

box_save_track_path = '/csvs/box_track_data_image_s2n.csv' #识别后的车辆位置写回csv地址-box
box_save_trace_path = '/csvs/box_trace_data_video_s2n.csv' #识别后的车辆轨迹写回csv地址-box

seg_save_track_path = '/csvs/seg_track_data_image_s2n.csv' #识别后的车辆位置写回csv地址-segment
seg_save_trace_path = '/csvs/seg_trace_data_video_s2n.csv' #识别后的车辆轨迹写回csv地址-segment

hd_save_track_path = '/csvs/hd_track_data_image_s2n.csv' #识别后的车辆位置写回csv地址-hd map
hd_save_trace_path = '/csvs/hd_trace_data_video_s2n.csv' #识别后的车辆轨迹写回csv地址-hd map

hd_trace_3D_path = '/csvs/hd_trace_3D_s2n.csv' #识别后的车辆轨迹写回csv地址-hd map

csvs_directory_3D = '/csvs/3D_result/s2n/' #存储3D检测结果的csv目录


media_type = configuration.media_type  # media_type: 0: image; 1: video
detection_type = 1   # detection_type: 0 ==> box;  1 ==> segment

video_rescale = [1,1]

process_type = 0 # : 1 ==> test,显示切割后图像;  0 ==> real,不显示切割后图像