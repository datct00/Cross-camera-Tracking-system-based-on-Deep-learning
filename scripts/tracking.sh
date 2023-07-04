#!/bin/bash
DATASET_DIR="/home/hoangtv/data/Phong_Dat/aic23/dataset"
# DATASET_DIR=${DATASET_DIR}'/test'
DATASET_DIR=${DATASET_DIR}'/validation'

# prepare dataset
python src/SCMT/dataspace/AICITY_test/prepapre_folder_infor.py
# Move to tracking dir
cd src/SCMT/


echo "${DATASET_DIR}"

#scenes=(S003 S004 S009 S014 S021 S022 S001)
# scenes=(S003 S009 S014 S018 S021 S022 S001)
scenes=(S005 S008 S013 S017 S020)
for scene in "${scenes[@]}"
do
    # python run_aicity.py --scene "$scene" --feature_dir ../../output/transformer_feat --detection_dir ../../datasets/detection/Yolo --root_dataset "/home/hoangtv/data/Phong_Dat/aic23/dataset/test"
    python run_aicity.py --scene "$scene" --feature_dir ../../output/transformer_feat/validation --detection_dir ../../datasets/detection/Yolo/yolo_validation --root_dataset "${DATASET_DIR}"
done

## Move file to tracking result
cd ../../
python src/SCMT/move2trackingres.py