import networkx as nx
from drone_path.district_map import get_district_graph
from drone_path.eulerize import eulerize_undirected
import threading

global_cost = 0
cost_lock = threading.Lock()

def find_len(graph, path):
    res = 0
    for (u, v) in path:
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
    global global_cost

    if log:
        print(f"Charging {district}")
    
    graph = get_district_graph(district).to_undirected()
    
    if log:
        print(f"Finished Charging {district}")
    
    if not nx.is_eulerian(graph):
        if log:
            print(f"Eulerizing {district}")
        graph = eulerize_undirected(graph, log=log)
        if log:
            print(f"Finished Eulerizing {district}")
    
    if log:
        print(f"Searching the Eulerian circuit of {district}")
    
    circuit = nx.algorithms.euler.eulerian_circuit(graph)
    res = list(circuit)
    
    if log:
        print(f"Finished the search of the Eulerian circuit of {district}")
        total_len = find_len(graph, res)
        cost = total_len * 0.01

        with cost_lock:
            global_cost += cost
        print(f"Full distance of {district} is {total_len}")
    return res, cost

def test():
    districts = ["Outremont", "Verdun", "Anjou", "Rivière-des-prairies-pointe-aux-trembles", "Le Plateau-Mont-Royal"]
    threads = []

    for district in districts:
        thread = threading.Thread(target=find_drone_path, args=(district,), kwargs={"log": True})
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"The global cost is {global_cost}")

