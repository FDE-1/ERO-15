import networkx as nx
from map import get_district_graph
from eulerize import eulerize_undirected
import threading
def find_len(graph, path):
    res = 0
    for (u,v) in path:
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
    if (log):
        print(f"Charging {district}")
    graph = get_district_graph(district).to_undirected()
    if (log):
        print(f"Finished Charging {district}")
    if (not nx.is_eulerian(graph)):
        if (log):
            print(f"Eularizing {district}")
        result = eulerize_undirected(graph,log=log)
        if (log):
            print(f"Finished Eularizing {district}")
    if (log):
        print(f"Searching the eulerian circuit of {district}")
    circuit = nx.algorithms.euler.eulerian_circuit(result)
    res= list(circuit)
    if (log):
        print(f"Finished the search of the eulerian circuit of {district}")
        len = find_len(graph,res)
        print(f"The len is {len}")
    return res

def test():
    
    d1 = threading.Thread(target=find_drone_path, args=("Outremont",), kwargs={"log": True})
    d2 = threading.Thread(target=find_drone_path, args=("Verdun",), kwargs={"log": True})
    d3 = threading.Thread(target=find_drone_path, args=("Anjou",), kwargs={"log": True})
    d4 = threading.Thread(target=find_drone_path, args=("Rivière-des-prairies-pointe-aux-trembles",), kwargs={"log": True})
    d5 = threading.Thread(target=find_drone_path, args=("Le Plateau-Mont-Royal",), kwargs={"log": True})

    d1.start()
    d2.start()
    d3.start()
    d4.start()
    d5.start()

    d1.join()
    d2.join()
    d3.join()
    d4.join()
    d5.join()