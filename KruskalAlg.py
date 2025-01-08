class KruskalMP:
    def __init__(self,vertices): #Inizializza numero di vertici, archi e l'mst finale
        self.V = vertices
        self.edges = []
        self.mst = []

    def add_edge(self,u,v, weight): #Crea un arco dati due vertici ed un peso
        self.edges.append((u,v,weight))

    def get_graph(self):
        return self.edges


#Utilizzo
g = KruskalMP(6)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
mst = g.get_graph()
for u, v, weight in mst:
    print(f"{u} --- {v} == {weight}")

