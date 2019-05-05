#!/usr/bin/python2.7
# -*- coding=utf-8 -*-

########################################################################################
# Beyond outliers and on to micro-clusters: Vision-guided Anomaly Detection
# Authors: Wenjie Feng, Shenghua Liu, Christos Faloutsos, Bryan Hooi,
#                 and Huawei Shen, and Xueqi Cheng
#
#  Project: eaglemine
#      run_waterleveltree.py
#      Version:  1.0
#      Date: Dec. 17 2017
#      Main Contact: Wenchieh Feng (wenchiehfeng.us@gmail.com)
#
#      Copyright:
#        This software is free of charge under research purposes.
#        For commercial purposes, please contact the author.
#
#      Created by @wenchieh  on <12/17/2017>
#
#      Main contributor:  Wenjie Feng
#
# -------------------------------------------------------------------------------
#  WaterLevelTree Algorithm interface.
#       Constructing WaterLevelTree structure for general histogram data.
#
# example:
#   python run_waterleveltree.py example/histogram.dat output/
#
################################################################

# sys
import time
import argparse
import warnings
warnings.filterwarnings("ignore")

# third-party lib
import numpy as np

# project
from src.waterleveltree import waterleveltree


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="'WaterLevelTree' algorithm",
                                     usage="python run_waterleveltree.py ins outs")
    parser.add_argument("ins", type=str, help="input path of histogram. "
                                              "The record in histogram should be in the format 'x,y,z,...,val', "
                                              "denoting that the cell (x, y, z, ...) affiliates with value 'val'")
    parser.add_argument("outs", type=str, help="output path of result")
    args = parser.parse_args()

    print("loading data ...")
    histogram = np.loadtxt(args.ins, int, delimiter=',')
    print("running WaterLevelTree algorithm ...")
    start = time.time()
    waterleveltree(histogram, args.outs)
    print("done @{}".format(time.time() - start))
