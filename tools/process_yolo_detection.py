import os

PATH = '/home/hoangtv/data/Phong_Dat/aic23/src/top2git/src/detection/runs/detect/exp20/labels'
print(os.listdir(PATH)[3])



scene_cam_files = dict()
for file in os.listdir(PATH):
    if not os.path.isfile(os.path.join(PATH, file)):
        continue
    scene, cam = file.split('_')[:2]
    scene_cam = scene + '_' + cam
    # print(scene, cam)
    if scene_cam not in scene_cam_files:
        scene_cam_files[scene_cam] = []
    scene_cam_files[scene_cam].append(file)

# print(scene_cam_files)
w_max = 1920
h_max = 1080
def process_scene_cam(param):
    results = []
    for file in param:
        f = open(os.path.join(PATH, file), 'r')
        frame_id = file.split('_')[-1].split('.')[0]
        f = f.readlines()
        for line in f:
            # 0 0.368229 0.331944 0.0197917 0.126852
            _, x_center,y_center,w,h,prob = line.split(' ')
            # Convert x,y,w,h YOLO to x,y,w,h COCO
            x_min = max(float(x_center) - float(w) / 2, 0)
            x_max = min(float(x_center) + float(w) / 2, 1)
            y_min = max(float(y_center) - float(h) / 2, 0)
            y_max = min(float(y_center) + float(h) / 2, 1)
            x_min = round(w_max* x_min)
            x_max = round(w_max * x_max)
            y_min = round(h_max* y_min)
            y_max = round(h_max * y_max)
            # x = x_center * w_max
            # y = y_center * h_max
            # w = w * w_max
            # h = h * h_max
            x = x_min
            y = y_min
            w = x_max - x_min
            h = y_max - y_min
            x, y, w, h = int(x), int(y), int(w), int(h)
            frame_id = int(frame_id)
            prob = float(prob)
            results.append([str(frame_id), '-1', str(x), str(y), str(w), str(h), str(prob), '-1', '-1', '-1'])
    return results

for scene_cam, files in scene_cam_files.items():
    print(scene_cam)
    results = process_scene_cam(files)
    with open(os.path.join('/home/hoangtv/data/Phong_Dat/aic23/src/top2git/datasets/detection/Yolo/yolo_validation',scene_cam + '.txt'), 'w') as f:
        for line in results:
            f.write(','.join(line) + '\n')