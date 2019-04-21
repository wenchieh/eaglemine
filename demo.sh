#!/usr/bin/env bash

## EagleMine demo
echo [DEMO EagleMine] 'run EagleMine ...'
python run_eaglemine.py example/histogram.out example/node2hcel.out example/hcel2avgfeat.out \
	                         4 dtmnorm 1 2 2 output
python run_eaglemine_view.py examplehistogram.out example/describe.out example/hcel2label.out \
	                         dtmnorm Hubness Out-degree output
echo [DEMO EagleMine] 'done!'
echo

## WaterLevelTree demo
echo [DEMO WaterLevelTree] 'run WaterLevelTree ...'
python run_waterleveltree.py example/histogram.out output
echo [DEMO WaterLevelTree] 'done!'
echo