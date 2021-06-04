#!/usr/bin/env bash
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`
echo "${green} Initialising NVIDIA docker{$reset}"
docker run --gpus all nvidia/cuda:9.0-base nvidia-smi
