import networkx as nx
from scipy.optimize import linear_sum_assignment

# à faire
def eurilize_graph(graph):
    """
    Si nombre de noeud a degré impair est impair
        ajouter un noeud de degré impair
    Si les edges ne sont pas connecté
        les connecter
    retourner le graph
    """
    # Step 1: Identify vertices of odd degree
    odd_degree_nodes = [v for v, d in graph.degree() if d % 2 != 0]
    print(f"Odd degree nodes: {odd_degree_nodes}")
    
    # Step 2: Create a complete graph of odd degree vertices with edge weights as shortest path distances
    subgraph = nx.Graph()
    for i, node1 in enumerate(odd_degree_nodes):
        for j, node2 in enumerate(odd_degree_nodes):
            if i < j:
                distance = nx.shortest_path_length(graph, node1, node2, weight='weight')
                subgraph.add_edge(node1, node2, weight=distance)
    
    # Step 3: Use the Hungarian algorithm to find the minimum weight matching
    weight_matrix = nx.to_numpy_matrix(subgraph, weight='weight')
    row_ind, col_ind = linear_sum_assignment(weight_matrix)
    min_weight_matching = [(odd_degree_nodes[i], odd_degree_nodes[j]) for i, j in zip(row_ind, col_ind)]
    print(f"Minimum weight matching: {min_weight_matching}")

    # Step 4: Add the edges from the minimum weight matching to the original graph
    for u, v in min_weight_matching:
        path = nx.shortest_path(graph, u, v, weight='weight')
        for i in range(len(path) - 1):
            graph.add_edge(path[i], path[i + 1], weight=graph[path[i]][path[i + 1]].get('weight', 1))
        
    if not nx.is_eulerian(graph):
        print("HMAR DINMOK")
        exit()

    return graph

# à faire
def find_eulerian_path(district, log=False):
    """
    Si graphe n est pas eulerian
        transformer le graphe en eulerian avec eulerize_graph
    sinon:
        chemin[]
        pile avec n'importe quel sommet de départ
        tant que chemin non visité:
            si sommet a des arrêtes non visité
                empiler le sommet sur la pile
                choisir un sommet non visité
                marquer l'arrête comme visité
                deplacer vers un voisin pas visité
            sinon:
                ajouter le sommet dans chemin 
                dépiler
    retourner le chemin
    """
    if log:
        print("Recherche de chemin en cours")
    path = nx.algorithms.euler.eulerian_circuit(eulerized_graph)
    if log:
        print("Chemin trouvé")
    return list(path)