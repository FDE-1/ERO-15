def cost(time, estime_length):
    """
    graph_ = newGraph(type,time,price)
    cheap_truck = 1
    while estimate_time(G,cheap_truck) < time:
        cheap_truck++
        graph_.add(cheap_truck, estimate_time(G,cheap_truck), cheap_truck*estimate_length*gaz_cheap)
    expensive_truck= 1
    while estimate_time(G,expensive_truck) < time:
        expensive_truck++
        graph_.add(expensive, estimate_time(G,expensive_truck), expensive_truck*estimate_truck*gaz_expensive)
    min_price = distance_min(graph(expensive_truck),graph(cheap_truck)) nb_cheap = graph.where(expensive_truck) == min_price
    nb_expensive = graphe.where(expensive_truck) == min_price
    return (nb_cheap,nb_expensive,min_price)
    """
    gaz_cheap = 1.1
    price_cheap = estimate_length*gaz_cheap
    gaz_expensive = 1.3
    price_expensive = estimate_truck*gaz_expensive
    cheap_truck_number = 1
    expensive_truck_number = 1
    graph_ = newGraph(type,time,price)
    while (estimate_time_cheap_truck = estimate_time(graph_,cheap_truck_number)) < time:
        cheap_truck_number += 1
        graph_.add(cheap_truck_number, estimate_time_cheap_truck, cheap_truck_number*price_cheap)
    while (estimate_time_expensive_truck = estimate_time(graph_,expensive_truck_number)) < time:
        expensive_truck_number += 1
        graph_.add(expensive_truck_number, estimate_time_expensive_truck, expensive_truck_number*price_expensive)
    min_price = distance_min(graph(expensive_truck_number),graph(cheap_truck_number))
    nb_cheap = graph.where(expensive_truck_number) == min_price
    nb_expensive = graphe.where(expensive_truck_number) == min_price
    return (nb_cheap,nb_expensive,min_price) 
