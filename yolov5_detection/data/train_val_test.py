# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:45:48 2021

@author: Alice Liu
"""

import os
import random


wd = os.getcwd() 
print(wd)

trainval_percent = 0.9
train_percent = 0.9
trainfolder = 'train'
total_label = os.listdir(trainfolder)

num = len(total_label)
listn = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(listn, tv)
train = random.sample(trainval, tr)

if not os.path.exists('./dataset/'):
    os.makedirs('./dataset/')

ftrainval = open('dataset/trainval.txt', 'w')
ftrain = open('dataset/train.txt', 'w')
fval = open('dataset/val.txt', 'w')
ftest = open('dataset/test.txt', 'w')

for i in listn:
    name = total_label[i][:-4] + '\n'
    ftrainval.write(name)
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)  

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

# 返回當前工作目錄
wd = os.getcwd()

sets = ['train', 'test', 'val']
for image_set in sets:
    '''
    對所有的檔案資料集進行遍歷
    做了兩個工作：
　　　　１．講所有圖片檔案都遍歷一遍，並且將其所有的全路徑都寫在對應的txt檔案中去，方便定位
    '''
    image_ids = open('./dataset/%s.txt' % (image_set)).read().strip().split()
    # 開啟對應的train.txt 檔案對其進行寫入準備
    list_file = open('./%s.txt' % (image_set), 'w')
    # 將對應的檔案_id以及全路徑寫進去並換行
    for image_id in image_ids:
        list_file.write('./train/%s.png\n' % (image_id))
    # 關閉檔案`在這裡插入程式碼片`
    list_file.close()
