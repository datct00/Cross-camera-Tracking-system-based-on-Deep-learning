from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2 
from collections import Counter 
from skimage.color import rgb2lab, deltaE_cie76
import os 
from utils import get_image, save_image
from tqdm import tqdm
import time
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_colors(image, number_of_colors):
    
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
    
    counts = Counter(labels)
    # sort to ensure correct color percentage
    counts = dict(sorted(counts.items()))
    
    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    return rgb_colors

def match_image_by_color(image, color, threshold = 60, number_of_colors = 10): 
    
    image_colors = get_colors(image, number_of_colors)
    selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

    select_image = False
    for i in range(number_of_colors):
        curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
        diff = deltaE_cie76(selected_color, curr_color)
        print(diff)
        if (diff < threshold):
            select_image = True
    
    return select_image

def find_person_images(unique_person_id: dict, color, threshold, colors_to_match):
    index = 0
    # unique_person_id: dict of unique person id
    #         unique_person_id = {
    #                 "person_id": {
    #                     "cam": []
    #                     "person_image": []
    #                 }
    #             }
    for person_id in unique_person_id:
        for image in unique_person_id[person_id]["person_image"]:
                print("Matching image of person_id:", person_id, "...")
                selected = match_image_by_color(image,
                                                color,
                                                threshold,
                                                colors_to_match)
                if (selected):
                    save_image(image, f"/home/hoangtv/data/Phong_Dat/aic23/src/top2git/src/web_app/{index}.jpg")
                    index += 1
    if (index == 0):
        print("No image found")
    else: 
        print("Found", index, "person images")


