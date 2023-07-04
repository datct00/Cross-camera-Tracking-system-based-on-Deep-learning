import os 

role = "train" # or val



ROOT_DATADIR = {
    "train": "/home/hoangtv/data/Phong_Dat/aic23/dataset/train/",
    "val": "/home/hoangtv/data/Phong_Dat/aic23/dataset/validation/"
    }
OUTPUT_DIRS = {
    "train": "/home/hoangtv/data/Phong_Dat/aic23/dataset/yolov6/labels/train/",
    "val": "/home/hoangtv/data/Phong_Dat/aic23/dataset/yolov6/labels/val/"
}

chosen_cam = {
    "train": ["c008","c009","c020","c021","c030", "c031","c036","c037", "c053", "c054", "c059", "c060", "c065", "c066", "c082", "c083", "c088", "c089", "c106", "c107"],
    "val": ["c025", "c026", "c041", "c042", "c071", "c072", "c094", "c095", "c112", "c113"] 
}
w_max = 1920
h_max = 1080
for dirs, subdirs, files in os.walk(ROOT_DATADIR[role]):
    for file in files:
        if file.endswith(".txt"):
            read_file = open(os.path.join(dirs, file), "r")
            lines = read_file.readlines()
            scene = dirs.split("/")[-2]
            cam = dirs.split("/")[-1]
            if cam not in chosen_cam[role]: continue
            for line in lines:
                # input "<frame>,<ID>,<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,1,-1,-1,-1"
                # output yolo format "0 <center x> <center y> <width> <height>"
                line = line.split(",")
                frame = line[0].zfill(6)
                bbox_left = float(line[2])
                bbox_top = float(line[3])
                bbox_width = float(line[4])
                bbox_height = float(line[5])
                # Convert to yolo format
                center_x = (bbox_left + bbox_width / 2)/w_max
                center_y = (bbox_top + bbox_height / 2)/h_max
                width = bbox_width/w_max
                height = bbox_height/h_max
                #Write to txt file with name is S003_C001_frame.txt
                write_file = open(os.path.join(OUTPUT_DIRS[role], scene + "_" + cam + "_" + frame + ".txt"), "a")
                print("Convert: ", scene, cam, frame)
                #Write to txt file with format "0 <center x> <center y> <width> <height>"
                write_file.write("0 " + str(center_x) + " " + str(center_y) + " " + str(width) + " " + str(height) + "\n")
                write_file.close()

print("Number of files: ", len(os.listdir(OUTPUT_DIRS[role])))