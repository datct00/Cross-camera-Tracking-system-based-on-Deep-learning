### This code will creat TrackEval/data/gt/aic23 folder structure
### It move labels.txt and seqinfo.ini of each camera to the corresponding folder

import os 
import shutil

SOURCE_DIR = "/home/hoangtv/data/Phong_Dat/aic23/src/top2git/outputs/matching/validation/"
DES_DIR = "/home/hoangtv/data/Phong_Dat/aic23/src/top2git/TrackEval/data/trackers/mot_challenge/aic23-test/data/"



for dirs, sub_dirs, files in os.walk(SOURCE_DIR): 
    for file in files: 
        if file == 'label.txt':
            cam = dirs.split("/")[-1]
            src_txt_file = os.path.join(dirs, file)
            src_ini_file = os.path.join(dirs, "seqinfo.ini")
            des_folder = os.path.join(DES_DIR, cam)
            if not os.path.exists(des_folder):
                os.mkdir(des_folder)    
            #Copy seqinfo.ini to des_folder
            shutil.copy(src_ini_file, os.path.join(des_folder, "seqinfo.ini"))
            #Copy labels to des_folder with name is gt.txt
            final_des_folder = os.path.join(des_folder, "gt")
            shutil.copy(src_txt_file, os.path.join(final_des_folder, "gt.txt"))
            with open(os.path.join(final_des_folder,"gt.txt"), "r") as f:
                #This file have each line 
                # <frame>,<ID>,<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,1,-1,-1,-1
                # Convert to  
                # <frame>,<ID>,<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,-1,-1,-1,-1
                # Then write to new gt.txt
                lines = f.readlines()
                new_lines = []
                for line in lines:
                    line = line.split(",")
                    line[6] = "-1"
                    new_lines.append(",".join(line))
                    
                with open(os.path.join(final_des_folder,"gt.txt"), "w") as f:
                    f.writelines(new_lines)
                    