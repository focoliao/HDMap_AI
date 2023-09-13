#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Foco Liao'

#1. 导入必要的库,如OpenCV、numpy等:
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
from ultralytics import YOLO
import pandas as pd
#from pymono3d.torch_utils import detect

def vehicleDetection(media_type, real_time_media_path, save_path, detection_type):
    
    #track_data = {'id':[],'x_lu':[],'y_lu':[],'x_rd':[],'y_rd':[], 'x_center':[], 'y_center':[]}
    #trace_data = {'targets':[]}
    
    if detection_type == 0:  # detection_type: 0 ==> box;  1 ==> segment
        track_data = {'id':[],'x_lu':[],'y_lu':[],'x_rd':[],'y_rd':[], 'x_center':[], 'y_center':[]}
        trace_data = {'targets':[]}

        # Load a model
        model = YOLO('yolov8n.pt')  # load an official detection model
        #model = YOLO('yolov8n-seg.pt')  # load an official segmentation model
        #model = YOLO('path/to/best.pt')  # load a custom model

        # Track with the model
        #results = model.track(source=real_time_video_path, show=True) 
        #results = model.track(source=real_time_media_path, show=True, tracker="bytetrack.yaml", save=True, save_txt=True)
        if media_type == 0: # image
            results = model.track(source=real_time_media_path, show=True, tracker="bytetrack.yaml", save=True)
            for result in results:                                         # iterate results
                ids = result.boxes.id.cpu().numpy().astype(int)            # get ids
                boxes = result.boxes.cpu().numpy()                         # get boxes on cpu in numpy
                for box, id in zip(boxes,ids):                             # iterate boxes
                    r = box.xyxy[0].astype(int)                            # get corner points as int
                    track_data['id'].append(id)                               
                    track_data['x_lu'].append(r[0])
                    track_data['y_lu'].append(r[1])
                    track_data['x_rd'].append(r[2])
                    track_data['y_rd'].append(r[3])
                    track_data['x_center'].append((r[0]+r[2])/2)
                    track_data['y_center'].append((r[1]+r[3])/2)
            pd.DataFrame(track_data).to_csv(save_path) #写回csv
        elif media_type == 1: # video
            results = model.track(source=real_time_media_path, show=True, stream=True, tracker="bytetrack.yaml", save_txt=True, save=True)
            for result in results:                                         # iterate results
                ids = result.boxes.id.cpu().numpy().astype(int)            # get ids
                boxes = result.boxes.cpu().numpy()                         # get boxes on cpu in numpy
                content = []
                for box, id in zip(boxes,ids):                                          # iterate boxes
                    r = box.xyxy[0].astype(int)                            # get corner points as int
                    content.append({'obj_ID':id,'x_lu':r[0],'y_lu':r[1],'x_rd':r[2],'y_rd':r[3],'x_center':(r[0]+r[2])/2, 'y_center':(r[1]+r[3])/2})
                trace_data['targets'].append(content)
            pd.DataFrame(trace_data).to_csv(save_path) #写回csv
    elif detection_type == 1:    # detection_type: 0 ==> box;  1 ==> segment
        track_data = {'id':[],'contour':[]}
        trace_data = {'targets':[]}
        # Load a model
        #model = YOLO('yolov8n.pt')  # load an official detection model
        model = YOLO('yolov8n-seg.pt')  # load an official segmentation model
        #model = YOLO('path/to/best.pt')  # load a custom model

        # Track with the model
        #results = model.track(source=real_time_video_path, show=True) 
        #results = model.track(source=real_time_media_path, show=True, tracker="bytetrack.yaml", save=True, save_txt=True)
        if media_type == 0: # image
            results = model.track(source=real_time_media_path, show=True, tracker="bytetrack.yaml", save=True)
            for result in results:                                         # iterate results
                ids = result.boxes.id.cpu().numpy().astype(int)            # get ids
                masks = result.masks                                       # get masks
                for mask, id in zip(masks,ids):                             # iterate masks
                    track_data['id'].append(id)
                    contour = []
                    for xy in mask.xy:
                        points = xy.astype(int)
                        for point in points:
                            contour.append(point.tolist())
                    track_data['contour'].append(contour)    
            pd.DataFrame(track_data).to_csv(save_path) #写回csv
        elif media_type == 1: # video
            results = model.track(source=real_time_media_path, show=True, stream=True, tracker="bytetrack.yaml", save_txt=True, save=True)
            for result in results:                                         # iterate results
                ids = result.boxes.id.cpu().numpy().astype(int)            # get ids
                #boxes = result.boxes.cpu().numpy()                         # get boxes on cpu in numpy
                #content = []
                #for box, id in zip(boxes,ids):                                          # iterate boxes
                #    r = box.xyxy[0].astype(int)                            # get corner points as int
                #    content.append({'obj_ID':id,'x_lu':r[0],'y_lu':r[1],'x_rd':r[2],'y_rd':r[3],'x_center':(r[0]+r[2])/2, 'y_center':(r[1]+r[3])/2})
                #trace_data['targets'].append(content)
                masks = result.masks                                       # get masks
                content = []
                for mask, id in zip(masks,ids):                             # iterate masks
                    track_data['id'].append(id)
                    contour = []
                    for xy in mask.xy:
                        points = xy.astype(int)
                        for point in points:
                            contour.append(point.tolist())
                    content.append({'obj_ID':id,'contour':contour})
                trace_data['targets'].append(content)
            pd.DataFrame(trace_data).to_csv(save_path) #写回csv
    else:
        pass
    return results