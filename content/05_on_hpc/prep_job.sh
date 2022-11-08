#!/bin/bash
#SBATCH --job-name=vis_prep
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=12G
#SBATCH --time=01:00:00
#SBATCH --partition=data

# make sure we have Singularity
module load singularity/3.5.2

# to get the image (need to be on a partition which has internet access --> data), run
singularity pull --disable-cache --dir "${PWD}" docker://pangeo/pangeo-notebook:2022.07.27

# print resource infos
jobinfo
