import networkx as nx

def is_eulerian(graph):
    return nx.is_eulerian(G)

# à faire
def eurilize_graph(graph):
    """
    Si nombre de noeud a degré impair est impair
        ajouter un noeud de degré impair
    Si les edges ne sont pas connecté
        les connecter
    retourner le graph
    """

# à faire
def find_eulerian_path(district):
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