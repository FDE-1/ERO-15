import networkx as nx

def cluster_edges(G, edges, start_node, n_vehicles):
    distances = [(edge, min(nx.shortest_path_length(G, start_node, edge[0]),
                             nx.shortest_path_length(G, start_node, edge[1]))) for edge in edges]
    sorted_by_distance = sorted(distances, key=lambda x: x[1])
    clusters = [[] for _ in range(n_vehicles)]
    for i, (edge, _) in enumerate(sorted_by_distance):
        clusters[i % n_vehicles].append(edge)
    return clusters

def optimize_route(G, edges, start_node):
    path = [start_node]
    unvisited_edges = list(edges)

    while unvisited_edges:
        try:
            last_node = path[-1]
            next_edge = min(unvisited_edges, key=lambda edge: nx.shortest_path_length(G, last_node, edge[0]))
            path_to_next_edge = nx.shortest_path(G, last_node, next_edge[0])
            path.extend(path_to_next_edge[1:])
            path.append(next_edge[1])
            unvisited_edges.remove(next_edge)
        except nx.NetworkXNoPath:
            continue

    return list(zip(path[:-1], path[1:]))

def assign_edges_to_vehicles(G, edges, n_vehicles, start_node):
    clusters = cluster_edges(G, edges, start_node, n_vehicles)
    vehicle_routes = [optimize_route(G, cluster, start_node) for cluster in clusters]
    return vehicle_routes

def test():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4), (3, 5), (4, 1)])
    edges_of_interest = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (2, 4)]
    number_of_vehicles = 5
    starting_node = 1
    routes = assign_edges_to_vehicles(G, edges_of_interest, number_of_vehicles, starting_node)
    print(routes)

test()
