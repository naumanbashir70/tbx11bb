# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:38:11 2021

@author: NaumanBashir
"""


import xml.etree.ElementTree as ET
import cv2

img = "tb0003.png"
xml = "tb0003.xml"

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


image = cv2.imread(img) 
image = cv2.resize(image, (2840, 2827)) 
name, boxes = read_content(xml)

temp = []

for i in range(len(boxes)):
  
    
    temp = boxes[i]
    start_point = (temp[0], temp[3]) 
    end_point = (temp[2], temp[1]) 
      
    
    # Blue color in BGR
    if i==0:
        color = (255, 0, 0)
    if i==1:
        color = (0, 255, 0)
  
    # Line thickness of 10 px 
    thickness = 10
    
    # Using cv2.rectangle() method 
    # Draw a rectangle with blue line borders of thickness of 2 px 
    image = cv2.rectangle(image, start_point, end_point, color, thickness) 


image = cv2.resize(image, (512, 512)) 

cv2.imwrite("img"+str(i)+".png", image)
cv2.imshow("img", image)
cv2.waitKey(0)