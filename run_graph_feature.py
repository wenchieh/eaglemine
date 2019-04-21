#!/usr/bin/python2.7
# -*- coding=utf-8 -*-

########################################################################################
#  Tool for extracting graph node's features.
#    like out-/in-degree, hubness/authoritativeness, pagerank, #triangles etc.
#
#   Here we only provide an example for
#        out-/in-degree vs. hubness/authority features for bipartite graph, and
#   .    degree vs. pagerank features for unipartite graph
#   The user can refer to BipartiteGraph and UnipartiteGraph for other possible features.
#   Besides, other user-defined feature also can be used for EagleMine algorithm.
#
#   Inputs:
#       infn_edgelist: the 1st input argument
#             The input filename of the graph with edgelist format: u,v
#       startzero: the 2nd input parameter (True/ False)
#             Indicating if the node index (us and vs) starting 0.
#       gtype: the 3rd input parameter
#             graph type ['bip', 'unip']
#       outpath: the 4th input parameter
#             The output path of results.
#
# Example:
#   python run_graph_feature.py example/example.graph True bip example
#
###########################################################

# sys
import os
import time
import argparse

# project
from src.utils.loader import Loader
from src.tools.graph import BipartiteGraph, UnipartiteGraph

outd2hub, ind2aut = 'outd2hub_feature', 'ind2aut_feature'
deg2pgrk = 'deg2pgrk'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compute graph node features",
                                     usage="python run_graph_feature.py [in_edgelist] [startszero] [gtype] [outs]")
    parser.add_argument("in_edgelist", type=str, help="input path of graph edgelist")
    parser.add_argument("startzero", type=bool, help="is the node index start ZERO")
    parser.add_argument("gtype", choices={"bip", "unip"}, help="graph type: 'unip': unipartite, 'bip': bipartite")
    parser.add_argument("outs", type=str, help="input path of result")
    args = parser.parse_args()

    loader = Loader()
    print("loading graph edgelist  ...")
    edgelist = loader.load_edgelist(args.in_edgelist, dtype=int, idstartzero=args.startzero)
    print("done!")

    if args.gtype == "bip":
        print("bipartite graph feature extraction")
        start_t = time.time()
        bi_graph = BipartiteGraph()
        bi_graph.set_edgelist(edgelist)
        bi_graph.get_node_degree()
        bi_graph.get_hits_score()
        print("done @{}(s)".format(time.time() - start_t))
        print("saving result")
        with open(os.path.join(args.outs, outd2hub), 'w') as ofp:
            ofp.writelines("# {},{}\n".format(len(bi_graph.src_outd), 0))
            for src in range(len(bi_graph.src_outd)):
                ofp.writelines("{},{}\n".format(bi_graph.src_outd[src], bi_graph.src_hub[src]))
            ofp.close()

        with open(os.path.join(args.outs, ind2aut), 'w') as ofp:
            ofp.writelines("# {},{}\n".format(len(bi_graph.dest_ind), 0))
            for dest in range(len(bi_graph.dest_ind)):
                ofp.writelines("{},{}\n".format(bi_graph.dest_ind[dest], bi_graph.dest_auth[dest]))
            ofp.close()

        print("done!")

    if args.gtype == "unip":
        print("unipartite graph feature extraction")
        start_t = time.time()
        uni_graph = UnipartiteGraph()
        uni_graph.set_edgelist(edgelist)
        uni_graph.get_node_degree()
        uni_graph.get_pagerank()
        print("done @{}(s)".format(time.time() - start_t))
        print("saving result")
        with open(os.path.join(args.outs, outd2hub), 'w') as ofp:
            ofp.writelines("# {},{}\n".format(uni_graph.n_src, 0))
            for id in range(uni_graph.n_src):
                ofp.writelines("{},{}\n".format(uni_graph.degree[id], uni_graph.pagerank[id]))
            ofp.close()
        print("done!")
