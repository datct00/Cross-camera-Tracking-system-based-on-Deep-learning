import json
import os
import shutil
# cam2scene = {'c001': 'S001','c002': 'S001','c003': 'S001','c004': 'S001','c005': 'S001','c006': 'S001','c007': 'S001','c014': 'S003','c015': 'S003','c016': 'S003','c017': 'S003','c018': 'S003','c019': 'S003','c047': 'S009','c048': 'S009','c049': 'S009','c050': 'S009','c051': 'S009','c052': 'S009','c076': 'S014','c077': 'S014','c078': 'S014','c079': 'S014','c080': 'S014','c081': 'S014','c100': 'S018','c101': 'S018','c102': 'S018','c103': 'S018','c104': 'S018','c105': 'S018','c124': 'S022','c125': 'S022','c126': 'S022','c127': 'S022','c128': 'S022','c129': 'S022','c118': 'S021','c119': 'S021','c120': 'S021','c121': 'S021','c122': 'S021','c123': 'S021'}
cam2scene = {"c025": "S005",
             "c026": "S005",
             "c027": "S005",
             "c028": "S005",
             "c029": "S005",
             "c041": "S008",
             "c042": "S008",
             "c043": "S008",
             "c044": "S008",
             "c045": "S008",
             "c046": "S008",
             "c071": "S013",
             "c072": "S013",
             "c073": "S013",
             "c074": "S013",
             "c075": "S013",
             "c094": "S017",
             "c095": "S017",
             "c096": "S017",
             "c097": "S017",
             "c098": "S017",
             "c099": "S017",
             "c112": "S020",
             "c113": "S020",
             "c114": "S020",
             "c115": "S020",
             "c116": "S020",
             "c117": "S020",}

# TMP_FOLDER = 'src/SCMT/tmp'
TMP_FOLDER = 'src/SCMT/tmp/validation'
# TRACKING_RESULT_FOLDER = 'outputs/tracking_results'
TRACKING_RESULT_FOLDER = 'outputs/tracking_results/validation'

try:
    os.makedirs(TRACKING_RESULT_FOLDER)
except:
    pass
for file in os.listdir(TMP_FOLDER):
    if not file.endswith('.txt'):
        continue
    scene = cam2scene[file.replace('.txt','')]
    # if 'S001' in scene: continue
    new_file = f'{scene}_{file}'
    shutil.copyfile(f'{TMP_FOLDER}/{file}', f'{TRACKING_RESULT_FOLDER}/{new_file}')
    print(f'Copied {file} to {new_file}')