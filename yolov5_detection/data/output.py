# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 00:15:01 2021

@author: Alice Liu
"""

import os
import cv2
import json
wd = os.getcwd() 
print(wd)
filepath = 'runs/detect/exp/labels/'

total_detect = os.listdir(filepath)
print(len(total_detect))

data = []
for nametxt in total_detect[:]:
    f = open(filepath + str(nametxt),'r')
    contents = f.readlines()
    f.close()
    img_name = str(nametxt[:-4])+'.png'
    im = cv2.imread('data/test/'+img_name)
    h, w, c = im.shape
    
    for content in contents:
        content = content.replace('\n','')
        item = content.split(' ')
        
        a = {"image_id": 0, "score": 0, "category_id": 0, "bbox": []}
        
        a['image_id'] = int(nametxt[:-4])
        
        a['category_id'] = int(item[0])
        
        yolox = float(item[1])
        yoloy = float(item[2])
        yolow = float(item[3])
        yoloh = float(item[4])
        
        cocox = (yolox - yolow / 2) * w
        cocoy = (yoloy - yoloh / 2) * h
        x = (yolox + yolow / 2) * w
        y = (yoloy + yoloh / 2) * h
        cocowidth = max(0, x-cocox)
        cocoheight = max(0, y-cocoy)
        
        a['bbox'] = tuple((cocox, cocoy, cocowidth, cocoheight))
        a['score'] = float(item[5])
        data.append(a)

ret = json.dumps(data, indent=4)
with open('answer.json', 'w') as fp:
    fp.write(ret)
fp.close()
print('answer.json is fin.')