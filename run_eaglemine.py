#!/usr/bin/python2.7
# -*- coding=utf-8 -*-

########################################################################################
# Beyond outliers and on to micro-clusters: Vision-guided Anomaly Detection
# Authors: Wenjie Feng, Shenghua Liu, Christos Faloutsos, Bryan Hooi,
#                 and Huawei Shen, and Xueqi Cheng
#
#  Project: eaglemine
#      eaglemine_model.py
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
# EagleMine Algorithm interface
#
# example:
#   python run_eaglemine.py output/histogram.out output/node2hcel.out \
#                           output/hcel2avgfeat.out 4 dtmnorm 1 2 2 output/
#
###########################################################

# sys
import warnings
import argparse

# project
from src.eaglemine_main import eaglemine

warnings.filterwarnings("ignore")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="'EagleMine' algorithm",
                                     usage="python eaglemine_main.py [in_hist] [in_node2hcel] [in_hcel2avgfeat] "
                                           "[desc_voc] [degidx] [mode] [mix_comps] [outs]")
    parser.add_argument("in_hist", type=str, help="input path of histogram. "
                                              "The record in histogram should be in the format 'x,y,z,...,val', "
                                              "denoting that the cell (x, y, z, ...) affiliates with value 'val'")
    parser.add_argument("in_node2hcel", type=str, help="input path of the file mapping the node to histogram cell")
    parser.add_argument("in_hcel2avgfeat", type=str, help="input path of the file mapping the histogram cell to "
                                                         "the average features and #points [see example]")
    parser.add_argument('strict', type=int, default=4, help="how strict should the anderson-darling test for normality. "
                                                             "0: not at all strict; 4: very strict")
    parser.add_argument("desc_voc", type=str, choices=["dtmnorm", "dmgauss"], default="dtmnorm", help="model vocabulary")
    parser.add_argument("wt_featidx", type=int, default=0, help="feature index as weight for suspiciousness metric")
    parser.add_argument("mode", type=int, help="the dimensions of features (the histogram)")
    parser.add_argument("mix_comps", type=int, default=2, help="# mixture component for describing the major island")
    parser.add_argument("outs", type=str, help="output path of result")

    args = parser.parse_args()

    eaglemine(args.in_hist, args.in_node2hcel, args.in_hcel2avgfeat, args.outs, args.strict,
              args.desc_voc, args.wt_featidx, args.mode, args.mix_comps)
