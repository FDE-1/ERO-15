from map import get_district_graph
from eulerize import eurilize_graph
import networkx as nx

# à faire
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
    graph = get_district_graph(district).to_undirected()
    if (not nx.is_eulerian(graph)):
        result = eurilize_graph(graph)
    circuit = nx.algorithms.euler.eulerian_circuit(result)
    return list(circuit)
    
find_drone_path("Outremont")
