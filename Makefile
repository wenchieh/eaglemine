#
# Makefile for EAGLEMINE
#
# AUTHORS:
#   wenchieh feng
#
# Copyright (c), 2017-2019
#

all: clean histogram demo

clean:
	rm -rf output
	mkdir output
	find ./ -name *.pyc | xargs rm -rf
	@echo

graph:
	@echo [DEMO Feature] "extracting graph nodes feature ..."
	python run_graph_feature.py example/example.graph True bip example
	@echo [DEMO Feature] "done."
	@echo

histogram:
	@echo [DEMO Histogram] "graph node feature (out-degree vs. hubness) to histogram ..."
	python run_graphfeature_histogram.py example/outd2hub_feature 1 Hubness Out-degree output ',' '#'
	@echo [DEMO Histogram] "done."
	@echo

demo:
	-chmod u+x ./*.sh
	@echo [DEMO EagleMine] "running EagleMine ..."
	python run_eaglemine.py output/histogram.out output/node2hcel.out output/hcel2avgfeat.out \
	                        4 dtmnorm 1 2 2 output
	@echo [DEMO EagleMine] "done!"
	@echo
	@echo [DEMO View]
	python run_eaglemine_view.py output/histogram.out output/describe.out output/hcel2label.out \
	                             dtmnorm Hubness Out-degree output
	@echo [DEMO View] "done!"
	@echo "see result in ./output"
	@echo

tar:
	rm -rf output/*
	@echo [Packaging]
	./package.sh
	@echo [Packaging] "done."
	@echo
