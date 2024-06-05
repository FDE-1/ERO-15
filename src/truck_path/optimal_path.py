import networkx as nx

def find_paths_for_edges(G, edges, start_node):
    if not edges:
        return []

    path_edges = []
    current_node = start_node

    for edge in edges:
        if current_node != edge[0]:
            path_to_next_edge = nx.shortest_path(G, current_node, edge[0])
            path_edges.extend(zip(path_to_next_edge[:-1], path_to_next_edge[1:]))
        path_edges.append(edge)
        current_node = edge[1]

    return path_edges

def balanced_edge_assignment(edges, n_vehicles):
    vehicles = [[] for _ in range(n_vehicles)]
    for i, edge in enumerate(sorted(edges)):
        vehicles[i % n_vehicles].append(edge)
    return vehicles

def assign_edges_to_vehicles(G, edges, n_vehicles, start_node):
    vehicle_assignments = balanced_edge_assignment(edges, n_vehicles)
    vehicle_routes = [find_paths_for_edges(G, assignment, start_node) for assignment in vehicle_assignments]
    return vehicle_routes

def test():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4), (3, 5), (4, 1)])
    edges_of_interest = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4)]
    number_of_vehicule = 1
    starting_node = 2
    routes = assign_edges_to_vehicles(G, edges_of_interest, number_of_vehicule, starting_node)
    print(routes)
