===========================================================================

Beyond outliers and on to micro-clusters: Vision-guided Anomaly Detection
Authors: Wenjie Feng, Shenghua Liu, Christos Faloutsos, Bryan Hooi,
                Huawei Shen, and Xueqi Cheng

Version: 1.0
Python: 2.7
Date: July 9, 2017
Main Contact: Wenjie Feng  
            ( fengwenjie@ict.ac.cn / wenchiehfeng.us@gmail.com )

This software is free of charge under research purposes.
For commercial purposes, please contact the author.

==========================================================================

EagleMine is a novel tree-based mining approach to recognize and
summarize the micro-clusters in the heatmap.

Inspired by the mechanism of human vision and cognitive system,
EagleMine detects and summarizes micro-clusters (dense blocks) in the heatmap
with a hierarchical tree structure (WaterLevelTree), and reports the suspiciousness
score of each micro-cluster (based on the deviation from the normal).

For the large graph, the heatmap can be constructed with correlated features
of graph nodes, and the micro-clusters correspond to node groups,
some of them deviating from the majority and contain anomaly / suspicious objects
with high probability.

Correlated features of graph nodes can be:
(in / out) Degree, # Triangle, PageRank, Hubness / Authority, Coreness, etc.


EagleMine has the following properties:
  - automatic summarization: automatically summarizes the heatmap
    derived from correlated graph features, and recognizes node
    groups forming disjointed dense areas as human vision does;
  - effectiveness: detects interpretable groups, and outperforms the 
    baselines, achieving better performance both in quantitative 
    (i.e., code length for compact model description) and qualitative 
    (i.e., consistent with vision-based judgment) comparisons;
  - anomaly detection: spots, and even explains anomalies on real data
    by identifying suspicious micro-clusters, and achieves higher
    accuracy compared with the state-of-the-art methods;
  - scalable: EagleMine is scalable, with nearly linear time complexity
    in the number of graph nodes, and can deal with more correlated
    features in multi-dimensional space.


 For detailed information, see 'user-guide.pdf'

 For demo, type 'make'
