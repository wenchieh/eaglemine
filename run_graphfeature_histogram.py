#!/usr/bin/python2.7
# -*- coding=utf-8 -*-

########################################################################################
# Beyond outliers and on to micro-clusters: Vision-guided Anomaly Detection
# Authors: Wenjie Feng, Shenghua Liu, Christos Faloutsos, Bryan Hooi,
#                 and Huawei Shen, and Xueqi Cheng
#
#  Project: eaglemine
#      run_graphfeature_histogram.py
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
# The interface for generating histogram for correlated features of graph node
#   like out-/in-degree vs. hubness/authority, etc.
#   (Considering visualization, we only give an example for TWo-dimensional case here,
#   but its can be extended to multi-dimensional features)
#
# example:
#   python run_graphfeature_histogram.py example/outd2hub_feature.out \
#                                        1 Hubness Out-degree output ',' '#'
#
###########################################################

# sys
import os
import argparse

# third-party lib
import numpy as np

# project
from src.graph2histogram import histogram_construct, histogram_view


hist_fn = 'histogram.out'
nodde2hcel = 'node2hcel.out'
hcel2avgfeat = 'hcel2avgfeat.out'
heatmap = 'heatmap.png'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Construct histogram for correlated features (TWO-dimension)",
                                     usage="python run_graphfeature_histogram.py [ins], [degidx] "
                                           "[x_lab] [y_lab] [delimiter] [comments] [outs]")
    parser.add_argument("ins", type=str, help="input path of correlated features of graph nodes."
                                              "Each line of file corresponding to two feature of one node")
    parser.add_argument("degidx", type=int, default=0, help="feature index if contain (in/out-) degree for graph else 0")
    parser.add_argument("x_lab", type=str, help="feature label for x axis")
    parser.add_argument("y_lab", type=str, help="feature label for y axis")
    parser.add_argument("outs", type=str, help="output path of result")
    parser.add_argument("delimiter", type=str, default=',', help="delimiter of the input")
    parser.add_argument("comments", type=str, default='%', help="comments character of the input")
    args = parser.parse_args()

    mode = 2
    ofn_hist = os.path.join(args.outs, hist_fn)  # result of feature-to-histogram
    ofn_node2hcel = os.path.join(args.outs, nodde2hcel)  # result of point to cell of histogram
    ofn_hcel2avgfeat = os.path.join(args.outs, hcel2avgfeat)  # result of average feature of each cell in histogram
    ofn_heatmap_viz = os.path.join(args.outs, heatmap)  # result of histogram view

    if args.degidx > 2:
        print("Invalid input argument for [degree-index]: {}".format(args.degidx))
        exit()

    graph_ndft = np.loadtxt(args.ins, float, args.comments, args.delimiter)
    histogram_construct(graph_ndft, args.degidx, ofn_hist, ofn_node2hcel, ofn_hcel2avgfeat, mode)
    histogram_view(ofn_hist, args.x_lab, args.y_lab, ofn_heatmap_viz)
