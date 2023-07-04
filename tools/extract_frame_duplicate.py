import os
import json
import numpy as np
import PIL.Image as Image
# from src.utils.opt import *
# import src.utils.utils as util
import cv2
from multiprocessing import Pool
from sys import stdout

ROLES = ["train","val"] # or 'val'

ROOT_DATA_DIR = {
    "train": "dataset/train/",
    "val": "dataset/validation/"
    }
OUTPUT_DIRS = {
    "train": "yolov6/images/train/",
    "val": "yolov6/images/val/"
}

chosen_cam = {
    "train": ["c008","c009","c020","c021","c030", "c031","c036","c037", "c053", "c054", "c059", "c060", "c065", "c066", "c082", "c083", "c088", "c089", "c106", "c107"],
    "val": ["c025", "c026", "c041", "c042", "c071", "c072", "c094", "c095", "c112", "c113"] 
}

fprint, endl = stdout.write, "\n"

IMAGE_FORMAT = ".jpg"  # ".png"
quality = 60

def video2image(parameter_set):
    role, scenario, camera, camera_dir = parameter_set
    fprint(f"[Processing] {scenario} {camera}{endl}")
    imgs_dir = f"{camera_dir}/img1"
    if not os.path.exists(imgs_dir):
        os.makedirs(imgs_dir)
    cap = cv2.VideoCapture(f"{camera_dir}/video.mp4")
    current_frame = 1
    ret, frame = cap.read()
    while ret:
        frame_file_name = f"{scenario}_{camera}_{str(current_frame).zfill(6)}{IMAGE_FORMAT}"
        # cv2.imwrite(f"{imgs_dir}/{frame_file_name}", frame)
        frame = frame[:, :, ::-1]
        image = Image.fromarray(frame)
        image.save(f"{OUTPUT_DIRS[role]}/{frame_file_name}", 
                    "JPEG", 
                    optimize = True, 
                    quality = quality)
        ret, frame = cap.read()
        current_frame += 1
    fprint(f"[Done] {role} {scenario} {camera}{endl}")


def main():
    parameter_sets = []
    for each_role in ROLES:
        role_dir = f"{ROOT_DATA_DIR[each_role]}"
        scenarios = os.listdir(role_dir)
        for each_scenario in scenarios:
            scene = each_scenario
            scenario_dir = f"{role_dir}/{each_scenario}"
            cameras = os.listdir(scenario_dir)
            # cameras = ["c019"]
            for each_camera in cameras:
                cam = each_camera
                if "map" in each_camera:
                    continue
                if each_camera not in chosen_cam[each_role]: 
                    continue
                camera_dir = f"{scenario_dir}/{each_camera}"                
                parameter_sets.append(
                    [each_role, each_scenario, each_camera, camera_dir]
                )

    pool = Pool(processes=24)
    pool.map(video2image, parameter_sets)
    pool.close()


if __name__ == "__main__":
    main()
