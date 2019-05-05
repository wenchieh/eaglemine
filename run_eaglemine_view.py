#!/usr/bin/python2.7
# -*- coding=utf-8 -*-

########################################################################################
# Beyond outliers and on to micro-clusters: Vision-guided Anomaly Detection
# Authors: Wenjie Feng, Shenghua Liu, Christos Faloutsos, Bryan Hooi,
#                 and Huawei Shen, and Xueqi Cheng
#
#  Project: eaglemine
#      run_eaglemine_view.py
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
#
# EagleMine Algorithm interface
# example:
#   python run_eaglemine_view.py output/histogram.out output/describe.out \
#                                output/hcel2label.out dtmnorm Hubness Out-degree output
#
###########################################################

__author__ = 'wenchieh'

# sys
import os
import argparse
import warnings
warnings.filterwarnings("ignore")

# project
from src.views_viz import cluster_view, describe_view

viz_clsv = 'viz_cluster.png'
viz_desc = 'viz_describe.png'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Cluster view of the EagleMine result for 'two' dimensional histogram, "
                                                 "the output includes the viz_cluster.png and viz_describes.png",
                                     usage="python run_eaglemine_view.py in_hist in_desc in_hcel2lab desc_voc x_lab y_lab outs")
    parser.add_argument("in_hist", type=str, help="input path of histogram")
    parser.add_argument("in_desc", type=str, help="input path of describe result from ealgemine model")
    parser.add_argument("in_hcel2lab", type=str, help="input path of label of each cell in histogram from eaglemine model")
    parser.add_argument("desc_voc", type=str, choices=["dtmnorm", "dmgauss"], default="dtmnorm", help="model vocabulary")
    parser.add_argument("x_lab", type=str, help="feature label of x axis")
    parser.add_argument("y_lab", type=str, help="feature label of y axis")
    parser.add_argument("outs", type=str, help="output path of result")
    args = parser.parse_args()

    cluster_view(args.in_hcel2lab, os.path.join(args.outs, viz_clsv))
    describe_view(args.in_hist, args.in_desc, args.desc_voc, args.x_lab, args.y_lab, os.path.join(args.outs, viz_desc))
