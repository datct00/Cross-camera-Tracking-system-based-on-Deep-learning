import os 
import cv2
from collections import defaultdict
from functools import partial
# 120,3,1,1370,226,86,277,-1,-1
# cam_id, person_id, frame_id, x, y, w, h, -1, -1

RESULT_PATH = "/home/hoangtv/data/Phong_Dat/aic23/src/top2git/outputs/multi_matching/S003.txt"
ROOT_IMAGE = "/home/hoangtv/data/Phong_Dat/aic23/dataset/test/S003/"
OUTPUT_DIR = "/home/hoangtv/data/Phong_Dat/aic23/src/top2git/outputs/visualization/"
file = open(RESULT_PATH, "r")
lines = file.readlines()
cam_dir = os.listdir(ROOT_IMAGE)
history = defaultdict(partial(defaultdict,list))
for cam in cam_dir:
    count = 0
    for line in lines: 
        line = line.split(",")
        cam_id = 'c'+line[0].zfill(3)
        person_id = line[1]
        frame_id = line[2].zfill(6)+".jpg"
        x = line[3]
        y = line[4]
        w = line[5]
        h = line[6]
        #Convert to top, left, bottom, right
        top = y
        left = x
        bottom = int(y) + int(h)
        right = int(x) + int(w)

        if cam_id == cam:
            history[cam_id][frame_id].append([person_id, top, left, bottom, right])
            count += 1
        if count == 200: 
            break
    #Draw bounding box
    for frame_id in history[cam]:
        img = cv2.imread(os.path.join(ROOT_IMAGE, cam, "img1",frame_id))
        for person_id, top, left, bottom, right in history[cam][frame_id]:
            cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), 2)
            cv2.putText(img, person_id, (int(left), int(top)-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            cv2.putText(img, cam, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        cv2.imwrite(os.path.join(OUTPUT_DIR, cam+"_"+frame_id), img)           
file.close()