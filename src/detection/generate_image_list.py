import os
TARGET_DIR = '/home/hoangtv/data/Phong_Dat/aic23/detection/validation/images'

from sys import stdout
from pathlib import Path

def main():
    images = os.listdir(TARGET_DIR)
    f_synthetic = open("./synthetic.txt", "w")
    f_real = open("./track1_S001.txt", "w")
    for image in images:
        IMAGE_PATH = os.path.join(TARGET_DIR, image)
        if 'S001' in image:
            f_real.write(IMAGE_PATH)
            f_real.write("\n")
        else:
            f_synthetic.write(IMAGE_PATH)
            f_synthetic.write("\n")
if __name__ == "__main__":
    main()