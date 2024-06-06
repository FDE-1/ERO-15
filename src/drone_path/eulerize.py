import networkx as nx
from itertools import combinations

def eulerize_undirected(G, log = False):
    """
    transformer le graphe non orienté en un graph orienté eulerian
    """
    if G.order() == 0:
        print("G.order est 0")
        exit(2)
    if not nx.is_connected(G):
        print("G est pas connecté")
        exit(2)
    nodes_ = [n for n, d in G.degree() if d % 2 == 1]
    G = nx.MultiGraph(G)
    
    if len(nodes_) == 0:
        return G
    if (log):
        print("Johnson algorithm")

    pairs_ = dict(nx.johnson(G))
    if (log):
        print("Creating list of shortests path")
    odd_ = [ (m, n, len(pairs_[m][n])) for m, n in combinations(nodes_, 2)]
    
    odd_.sort(key=lambda x: x[2])
    if (log):
        print("Matching algorithm")
    set_ = set()
    list_path_ = []
    for m, n, length in odd_:
        if m not in set_ and n not in set_:
            set_.add(m)
            set_.add(n)
            list_path_.append((m, n))
    if (log):
        print("Adding the path")
    for m, n in list_path_:
        path = pairs_[m][n]
        G.add_edges_from(nx.utils.pairwise(path))

    return G