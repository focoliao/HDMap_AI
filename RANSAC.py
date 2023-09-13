#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

def ransac(match_result, kp_des_real_time, kp_des_vibration, cur_path, real_time_img_path, real_img_path):
    best_match = 0
    best_inliers = None
    best_num_inliers = 0
    best_M = None
    best_good = []
    for i in range(len(match_result)):
        # store all the good matches. 存储所有好的match
        good = []
        for m,n in match_result[i]:
            if m.distance < 0.7*n.distance:
                good.append(m)
        src_pts = np.float32([ kp_des_real_time[0][0][m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp_des_vibration[i][0][m.trainIdx].pt for m in good ]).reshape(-1,1,2)
        M, inliers = cv.estimateAffinePartial2D(src_pts, dst_pts, cv.RANSAC) 
        if len(inliers) > best_num_inliers:
            best_num_inliers = len(inliers)
            best_match = i
            best_M = M
            best_good = good
            best_inliers = inliers.ravel().tolist()
    #画一下最匹配的两张图片:
    '''
    img1 = cv.imread(cur_path + real_time_img_path[0],0)          # 实时图片
    img2 = cv.imread(cur_path + real_img_path[best_match],0)      # 最佳匹配图片    

    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = best_inliers, # draw only inliers
                   flags = 2)

    img3 = cv.drawMatches(img1,kp_des_real_time[0][0],img2,kp_des_vibration[best_match][0],best_good,None,**draw_params)

    plt.imshow(img3, 'gray')
    plt.show()
    
    print('best_match_index:' + str(best_match) + '; best_num_inliers:' +  str(best_num_inliers))
    '''

    return best_match