import networkx as nx
from functions.drawings import draw_subtree
from functions.prims_functions import cost, min_prims_edges

G = nx.read_weighted_edgelist('data/G1.txt', nodetype = int)

def prims_algorithm(G, starting_node):
    
    T = nx.Graph()
    T.add_node(starting_node)
    
    while set(T.nodes()) != set(G.nodes()):
        e = min_prims_edges(G, T)
        T.add_edge(e[0], e[1], weight = cost(G, e))
        
    return T


