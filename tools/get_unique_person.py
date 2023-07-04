import os 
from collections import defaultdict

ROOT = "/home/hoangtv/data/Phong_Dat/aic23/dataset/validation/"
scene_cam = defaultdict(lambda: defaultdict(set))

#walk through all files in the root directory
for root, dirs, files in os.walk(ROOT):
    for file in files:
        #if the file is a .txt file
        if file.endswith(".txt"):
            if file == 'unique_person.txt': continue
            f = open(os.path.join(root, file), 'r')
            #read the first line of the file
            lines = f.readlines()
            for line in lines:
                _,person_id,_,_,_,_,_,_,_,_ = line.split(',')
                person_id = int(person_id)
                scene = root.split('/')[-2]
                cam = root.split('/')[-1]
                print("Counting in scene {} cam {} adding person id {}".format(scene, cam, person_id))
                scene_cam[scene][cam].add(person_id)
                
#Write all the results to a file with format 
#Scene: 
#   Cam: number of unique person

with open(os.path.join(ROOT, 'unique_person.txt'), 'w') as f:
    for scene, cams in scene_cam.items():
        f.write(scene + ':\n')
        for cam, person_ids in cams.items():
            f.write('\t' + cam + ': ' + str(len(person_ids)) + '\n')
        f.write('\n')
        