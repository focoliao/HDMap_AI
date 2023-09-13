#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
from SingleDirectionApp import singleDirectionPreprocessing


def dataPreprocessing(cur_path, configuration_single_direction_s2n,configuration_single_direction_n2s,configuration_single_direction_e2w,configuration_single_direction_w2e, direction, step_number):
    
    if direction == 's2n':
        print('========数据预处理：南向北========')
        singleDirectionPreprocessing(cur_path, configuration_single_direction_s2n, step_number)
    elif direction == 'n2s':
        print('========数据预处理：北向南========')
        singleDirectionPreprocessing(cur_path, configuration_single_direction_n2s, step_number)
    elif direction == 'e2w':
        print('========数据预处理：东向西========')
        singleDirectionPreprocessing(cur_path, configuration_single_direction_e2w, step_number)
    elif direction == 'w2e':
        print('========数据预处理：西向东========')
        singleDirectionPreprocessing(cur_path, configuration_single_direction_w2e, step_number)
    else:
        print('Interesting, I have nothing to do ~ ~')
    
    return