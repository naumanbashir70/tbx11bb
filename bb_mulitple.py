# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:06:00 2021

@author: NaumanBashir
"""


import xml.etree.ElementTree as ET
import cv2

import os


path_img = "tb/"  #images path
path_xml = "xml/" #xml path


if not os.path.exists('tb_bb'):
    os.makedirs('tb_bb')
    
    

def read_content(xml_file: str):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_with_all_boxes = []

    for boxes in root.iter('object'):

        filename = root.find('filename').text

        ymin, xmin, ymax, xmax = None, None, None, None

        ymin = int(boxes.find("bndbox/ymin").text)
        xmin = int(boxes.find("bndbox/xmin").text)
        ymax = int(boxes.find("bndbox/ymax").text)
        xmax = int(boxes.find("bndbox/xmax").text)

        list_with_single_boxes = [xmin, ymin, xmax, ymax]
        list_with_all_boxes.append(list_with_single_boxes)
  
    return filename, list_with_all_boxes

##-----------------------------------------------------------------------------

def main_bb(img, xml):
    
    image = cv2.imread(img) 
    #Comment the below line if you using High-resolution(3000 × 3000) dataset.
    image = cv2.resize(image, (2840, 2827)) 
    name, boxes = read_content(xml)
    
    temp = []
    
    for i in range(len(boxes)):
        
        temp = boxes[i]
        
        start_point = (temp[0], temp[3]) 
        end_point = (temp[2], temp[1]) 
          
        
        # Change color in BGR
        if i==0:
            color = (255, 0, 0)
        if i==1:
            color = (0, 255, 0)
          
        # Line thickness of 10 px 
        thickness = 10
        
        # Using cv2.rectangle() method 
        # Draw a rectangle with blue line borders of thickness of 2 px 
        image = cv2.rectangle(image, start_point, end_point, color, thickness) 
    
    #Comment the below line if you using High-resolution(3000 × 3000) dataset.
    image = cv2.resize(image, (512, 512)) 
    
    cv2.imwrite("tb_bb/"+name+".png", image)
    # cv2.imshow("img", image)
    # cv2.waitKey(0)

##-----------------------------------------------------------------------------


img_dirs = os.listdir( path_img )
xml_dirs = os.listdir( path_xml )


for item in img_dirs:
    if os.path.isfile(path_img+item):
        
        print("Processing image: ", item)
        fi, ei = os.path.splitext(path_img+item)
        fx, ex = os.path.splitext(path_xml+item)

        img = fi+ei
        xml = fx+".xml"

        main_bb(img, xml)








