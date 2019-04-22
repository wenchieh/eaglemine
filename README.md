Beyond outliers and on to micro-clusters: Vision-guided Anomaly Detection
========================
**EagleMine** is a novel tree-based mining approach to recognize and summarize the micro-clusters in the heatmap.

>   Inspired by the mechanism of human vision and cognitive system,
    **EagleMine** detects and summarizes micro-clusters (dense blocks) in the heatmap with a hierarchical 
    tree structure (WaterLevelTree), 
    and reports the suspiciousness score of each micro-cluster (based on the deviation from the normal).

>   For the large graph, the heatmap can be constructed with correlated features of graph nodes, 
    and the micro-clusters correspond to node groups, some of them deviating from the majority 
    and contain anomaly / suspicious objects with high probability.

>   Correlated features of graph nodes can be: 
    (in / out) Degree, # Triangle, PageRank, Hubness / Authority, Coreness, etc.

---

Datasets
========================
The download links for the datasets used in the paper are available [here](https://anonymous.com)
  - Amazon ratings [graph](http://konect.uni-koblenz.de/networks/amazon-ratings).
  - Android App rating [graph](http://jmcauley.ucsd.edu/data/amazon/).
  - Beer Advocate [graph](http://snap.stanford.edu/data/web-BeerAdvocate.html).  [**REGRET**: No longer available as per request]
  - Tagged [graph](https://linqs-data.soe.ucsc.edu/public/social_spammer/).
  - Yelp [graph](https://www.yelp.com/dataset_challenge).
  - Youtube [graph](http://konect.uni-koblenz.de/networks/youtube-u-growth).


### Datasets statistic information

|     Name     |          Content         |         Size        |  Edge  |    Graph   |  Download  |
| ------------ | ------------------------ | ------------------- | ------ | ---------- | ---------- |
| Amazon       | User X Item X Ratings    | 2.14M X 1.23 M X 5  | 5.84M  | bipartite  | [Link](http://konect.uni-koblenz.de/downloads/tsv/amazon-ratings.tar.bz2) |
| Android      | User X Apps X Ratings    | 1.32M X 61.27K X 5  | 2.64M  | bipartite  | [Link](http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/ratings_Apps_for_Android.csv) |
| BeerAdvocate | User X Beer X Rating     | 33.37K X 65.91K X 4 | 1.57M  | bipartite  |      -     |
| Tagged       | User X User X Relation   | 2.73M X 4.65M       | 858M (only a part)  | unipartite | [Link](https://linqs-data.soe.ucsc.edu/public/social_spammer/)   |
| Yelp         | User X Business X Rating | 686K X 85.5K X 5    | 2.68M  | bipartite  | [Link](https://www.yelp.com/dataset_challenge/dataset)   |
| Youtube      | User X User              | 3.22M X 3.22M       | 9.37M  | unipartite | [Link](http://konect.uni-koblenz.de/downloads/tsv/youtube-u-growth.tar.bz2)   |
---

Environment
=======================
Python 2.7 is the only supported in current version.

To install required libraries, please type
```bash
./install_libs.sh
```
----

Building and Running EagleMine
========================
Please see [User Guide](user_guide.pdf)

---

Running Demo
========================

#### Graph Analysis

Demo for scratch graph features, please type 
```bash
make
```
In briefly, 
 + Firstly, we use ```run_graphfeature_histogram.py``` to generate histogram **H** 
   for _out-degree_ vs. _hubness_ node features of example graph **G**;
 + Then, EagleMine (```run_eaglemine.py```) takes the histogram **H** as input to 
   construct WaterLevelTree **T**, identifies and summaries micro-clusters _**C**_ in **H**, 
   and also measures the suspiciousness of each element in _**C**_.
 + At last, we provide view tools in ```run_eaglemine_view.py``` to visualize the micro-cluster
   detection result and model description (with DTM Gaussian vocabulary) result for heatmap **H**;
___

To extract node correlated features for example graph, please type
```bash
make graph
```
```run_graph_feature.py``` takes the edgelist-format directed graph as input and extracts _out / in- degree_ and 
_hubness / authoritaty_ feature for each nodes.
For the undirected unipartite graph (e.g. _Youtube_), it can extract _degree_ and _pagerank_ features.

**Note**: ```src/tools/graph.py``` provides interfaces for some common graph features. 
For the very large graph, user can use powerful graph analysis tools to extract features, 
like [graphlab](https://turi.com/), and ```src/tools/large_graph.py``` gives a simple example.


#### Heatmap demo
Heatmap analysis demo, please type
```bash
./demo
```
> EagleMine detects micro-clusters in given example heatmap (histogram)     
  please see the parameter explanation in ```run_eaglemine.py```.

---

### **NOTE**
The interfaces in ```run_*.py``` contains detail information and parameter explanation.
 * ```run_eaglemine.py```:  
    EagleMine algorithm consists of WaterLevelTree, TreeExplore, and suspicious measure. 
 * ```run_eaglemine_view.py```:  
    Visualization tools for the detection result and model description result of EagleMine
 * ```run_waterleveltree.py```:  
    WaterLevelTree algorithm, Construct raw-tree, and refine tree structure
    (contract, prune, and expand).
 * ```run_graph_feature.py```:  
    Simple tools for extracting correlated node features of graph.
    bipartite graph: _out / in- degree_ and _hubness / authoritaty_;    
    unipartite graph: _degree_ and _pagerank_;
 * ```run_graphfeature_histogram.py```  
    Tools for constructing histogram for graph features.

---

Reference
========================
If you use this code as part of any published research, please acknowledge the following papers.
```
@inproceedings{feng2019beyond,
  title={Beyond Outliers and on to Micro-clusters: Vision-Guided Anomaly Detection},
  author={Wenjie Feng, Shenghua Liu, Christos Faloutsos, Bryan Hooi, Huawei Shen, and Xueqi Cheng},
  booktitle={The 23rd Pacific-Asia Conference on Knowledge Discovery and Data Mining},
  pages={541--554},
  year={2019},
  organization={Springer}
}
```