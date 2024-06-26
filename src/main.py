from truck_path.optimal_path import assign_edges_to_vehicles
from drone_path.drone import test
from itertools import combinations
from truck_path.map import get_district_graph
import threading


def find_len(graph, path):
    res = 0
    for (u,v) in path:
        res += graph[u][v].get('length', 1)
    return res

def main():

    test()

    d1 = get_district_graph("Outremont")
    d2 = get_district_graph("Verdun")
    d3 = get_district_graph("Anjou")
    d4 = get_district_graph("Rivière-des-prairies-pointe-aux-trembles")
    d5 = get_district_graph("Le Plateau-Mont-Royal")

    Temp_vise_ = 10
    nb_d1_ = 1
    nb_d2_ = 1
    nb_d3_ = 1
    nb_d4_ = 1
    nb_d5_ = 1
    while True :
        max_temp = 0
        list_d1_ = assign_edges_to_vehicles(d1, [(u, v) for u, v, _ in d1.edges.data()] , nb_d1_, list(d1.nodes)[0])
        max_district_d1_ = max([find_len(d1,i) for i in list_d1_])
        print(f"max_district_d1_ is {max_district_d1_}")
        nb_t1_ = 0
        nb_t2_ = 0
        for i in list_d1_:
            path_len = find_len(d1,i)
            if find_len(d1,i) < Temp_vise_ * 10:
                nb_t1_ +=1
                max_temp = max(max_temp, path_len/10)
            else:
                nb_t2_ +=1
                max_temp = max(max_temp, path_len/20)

        list_d2_ = assign_edges_to_vehicles(d2, [(u, v) for u, v, _ in d2.edges.data()] , nb_d2_, list(d2.nodes)[0])
        max_district_d2_ = max([find_len(d2,i) for i in list_d2_])
        print(f"max_district_d2_ is {max_district_d2_}")
        for i in list_d2_:
            path_len = find_len(d2,i) 
            if path_len < Temp_vise_ * 10:
                nb_t1_ +=1
                max_temp = max(max_temp, path_len/10)
            else:
                nb_t2_ +=1
                max_temp = max(max_temp, path_len/20)
        
        # list_d3_ = assign_edges_to_vehicles(d3,[(u, v) for u, v, _ in d3.edges.data()] , nb_d3_, list(d3.nodes)[0])
        # max_district_d3_ = max([find_len(d3,i) for i in list_d3_])
        # print(f"max_district_d3_ is {max_district_d3_}")
        # for i in list_d3_:
        #     if find_len(d3,i) < Temp_vise_ * 10:
        #         nb_t1_ +=1
        #         max_temp = max(max_temp, find_len(d3,i)/10)
        #     else:
        #         nb_t2_ +=1
        #         max_temp = max(max_temp, find_len(d3,i)/20)
        
        # list_d4_ = assign_edges_to_vehicles(d4, [(u, v) for u, v, _ in d4.edges.data()], nb_d4_, list(d4.nodes)[0])
        # max_district_d4_ = max([find_len(d4,i) for i in list_d4_])
        # print(f"max_district_d4_ is {max_district_d4_}")
        # for i in list_d4_:
        #     if find_len(d4,i) < Temp_vise_ * 10:
        #         nb_t1_ +=1
        #         max_temp = max(max_temp, find_len(d4,i)/10)
        #     else:
        #         nb_t2_ +=1
        #         max_temp = max(max_temp, find_len(d4,i)/20)

        # list_d5_ = assign_edges_to_vehicles(d5, [(u, v) for u, v, _ in d5.edges.data()] , nb_d5_,list(d5.nodes)[0])
        # max_district_d5_ = max([find_len(d5,i) for i in list_d5_])
        # print(f"max_district_d5_ is {max_district_d5_}")
        # for i in list_d5_:
        #     if find_len(d5,i) < Temp_vise_ * 10:
        #         nb_t1_ +=1
        #         max_temp = max(max_temp, find_len(d5,i)/10)
        #     else:
        #         nb_t2_ +=1
        #         max_temp = max(max_temp, find_len(d5,i)/20)
        if (max(max_district_d1_,max_district_d2_)< Temp_vise_*20):
            if (Temp_vise_ <8):
                print(f"Liste de chemin {list_d1_+list_d2_}")
                print(f"Cout total = {nb_t1_ *(500 + 1.1 * Temp_vise_*10 + 1.1 * Temp_vise_ ) + nb_t2_ *(800 + 1.3 * Temp_vise_*10 + 1.3 * Temp_vise_)}")
                print(f"nombre de t1 = {nb_t1_} | nombre de t2 = {nb_t2_}")
                print(f"Temp = {max_temp}")
                return list_d1_+list_d2_
            else:
                print(f"Liste de chemin {list_d1_+list_d2_}")
                print(f"Cout total = { nb_t1_ *(500 + 1.1 * Temp_vise_*10 + 1.1 * 8 + 1.3 * (Temp_vise_-8) ) + nb_t2_ *(800 + 1.3 * Temp_vise_*10 + 1.3 * 8 + 1.5 * (Temp_vise_-8))}")
                print(f"Nombre de t1 = {nb_t1_} | Nombre de t2 = {nb_t2_}")
                print(f"Temps = {max_temp}h")
                return list_d1_+list_d2_
        if (max_district_d1_ > Temp_vise_ * 20):
            nb_d1_ += 1
        if (max_district_d2_ > Temp_vise_ * 20):
            nb_d2_ += 1
        # if (max_district_d3_ > Temp_vise_ * 20):
        #     nb_d3_ += 1
        # if (max_district_d4_ > Temp_vise_ * 20):
        #     nb_d4_ += 1
        # if (max_district_d5_ > Temp_vise_ * 20):
        #     nb_d5_ += 1
        print(f"d1 = {nb_d1_} |d2 ={nb_d2_} | t1 = {nb_t1_} | t2 = {nb_t2_}") 

main()
