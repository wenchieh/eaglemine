#!/usr/bin/env bash

## EagleMine demo
echo [DEMO EagleMine] 'run EagleMine ...'
python run_eaglemine.py output/histogram.out output/node2hcel.out output/hcel2avgfeat.out \
	                         4 dtmnorm 1 2 2 output
python run_eaglemine_view.py output/histogram.out output/describe.out output/hcel2label.out \
	                         dtmnorm Hubness Out-degree output
echo [DEMO EagleMine] 'done!'
echo

# # WaterLevelTree demo
#echo [DEMO WaterLevelTree] 'run WaterLevelTree ...'
#python run_waterleveltree.py output/histogram.out output
#echo [DEMO WaterLevelTree] 'done!'
#echo