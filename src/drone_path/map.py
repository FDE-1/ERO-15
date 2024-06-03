import osmnx as ox

def get_district_graph(district):
    try:
        district_graph = nx.read_graphml(f"auto/{district}.graphml")
    except:
        outremont = ox.graph_from_place(f"{district}, Montréal, Canada", network_type='drive')
        ox.save_graphml(outremont, f"auto/{district}.graphml")
        district_graph = nx.read_graphml(f"auto/{district}.graphml")
    return district_graph