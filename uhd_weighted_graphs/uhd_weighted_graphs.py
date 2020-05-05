from algorithms.prims import prims_algorithm
import networkx as nx

G = nx.read_weighted_edgelist('data/G1.txt', nodetype = int)

T = prims_algorithm(G, 3, draw = True, attrib = True)