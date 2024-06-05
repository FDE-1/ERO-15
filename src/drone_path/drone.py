import networkx as nx
import numpy as np
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
import sys 
from map import get_district_graph
from networkx.drawing.nx_pydot import write_dot
import threading
from itertools import combinations

from joblib import Parallel, delayed
import multiprocessing

import networkx as nx
from itertools import combinations
from functools import lru_cache

def eulerize(G):
    if G.order() == 0:
        raise nx.NetworkXPointlessConcept("Cannot Eulerize null graph")
    if not nx.is_connected(G):
        raise nx.NetworkXError("G is not connected")

    odd_degree_nodes = [n for n, d in G.degree() if d % 2 == 1]
    G = nx.MultiGraph(G)
    
    if len(odd_degree_nodes) == 0:
        return G

    # Use Johnson's algorithm for all-pairs shortest paths for sparse graphs
    all_pairs_shortest_paths = dict(nx.johnson(G))

    # Create a list of pairs (m, n) with their shortest path lengths
    odd_deg_pairs = [
        (m, n, len(all_pairs_shortest_paths[m][n]))
        for m, n in combinations(odd_degree_nodes, 2)
    ]
    
    # Sort pairs by path length
    odd_deg_pairs.sort(key=lambda x: x[2])

    # Use a greedy algorithm to find a matching
    matched = set()
    matching = []
    for m, n, length in odd_deg_pairs:
        if m not in matched and n not in matched:
            matched.add(m)
            matched.add(n)
            matching.append((m, n))

    # Add the paths to the graph
    for m, n in matching:
        path = all_pairs_shortest_paths[m][n]
        G.add_edges_from(nx.utils.pairwise(path))

    return G

def eurilize_graph(graph):
    return eulerize(graph)

# à faire

def find_len(graph, path,log=False):
    res = 0
    for (u,v) in path:
        if (log):
            print(f"u is {u} and v is {v} weight is {graph[u][v].get('weight', 1)}")
        res += graph[u][v].get('weight', 1)
    return res

def find_drone_path(district, log=False):
    """
    transformer le graphe en graphe non orienté
    vérifier si le graphe est eulerien, si non le transformé
    chercher les chemin pour les drones (faire du parallélisme si possible)
    """

    """
    transformer le graphe en graphe non orienté
    trouver le chemin eulerian
    retourner chemin
    """
    # print(f"Charging {district}")
    graph = get_district_graph(district).to_undirected()
    # print(f"Finished Charging {district}")
    if (not nx.is_eulerian(graph)):
        # print(f"Eularizing {district}")
        result = eurilize_graph(graph)
        # print(f"Finished Eularizing {district}")
    # print(f"Searching the eulerian circuit of {district}")
    circuit = nx.algorithms.euler.eulerian_circuit(result)
    # print(f"Finished the eulerian circuit of {district}")
    # print(f"Calculating len {district}")
    res= list(circuit)
    print(f"len for {district} is {find_len(graph,res)}")
    return res

t1 = threading.Thread(target=find_drone_path("Outremont"))
t2 = threading.Thread(target=find_drone_path("Verdun"))
t3 = threading.Thread(target=find_drone_path("Anjou"))
t4 = threading.Thread(target=find_drone_path("Rivière-des-prairies-pointe-aux-trembles"))
t5 = threading.Thread(target=find_drone_path("Le Plateau-Mont-Royal"))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()