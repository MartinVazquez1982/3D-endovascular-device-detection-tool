#!/bin/bash

#SBATCH --time=00:60:00
#SBATCH --nodes=1
#SBATCH --mem=5GB
#SBATCH --job-name=inference
#SBATCH --output=inference.out

nnUNetv2_predict_from_modelfolder -i '/home/mvazquez/frontend/source_user_image/user_image.nii.gz' -o '/home/mvazquez/frontend/source_inference' -m "/home/mvazquez/model" -f 0