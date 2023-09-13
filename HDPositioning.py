#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
from SingleDirectionApp import singleDirectionHDPositioning


def hdPositioning(cur_path, configuration_single_direction_s2n,configuration_single_direction_n2s,configuration_single_direction_e2w,configuration_single_direction_w2e, direction):
    
    if direction == 's2n':
        print('========高精定位：南向北========')
        singleDirectionHDPositioning(cur_path, configuration_single_direction_s2n)
    elif direction == 'n2s':
        print('========高精定位：北向南========')
        singleDirectionHDPositioning(cur_path, configuration_single_direction_n2s)
    elif direction == 'e2w':
        print('========高精定位：东向西========')
        singleDirectionHDPositioning(cur_path, configuration_single_direction_e2w)
    elif direction == 'w2e':
        print('========高精定位：西向东========')
        singleDirectionHDPositioning(cur_path, configuration_single_direction_w2e)
    else:
        print('Interesting, I have nothing to do ~ ~')
    
    return