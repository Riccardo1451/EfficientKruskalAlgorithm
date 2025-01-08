import time
import random
from multiprocessing import Process, Manager
class Kruskal:
    def __init__(self, vertices):  # Inizializza numero di vertici, archi e l'mst finale
        self.V = vertices
        self.edges = []
        self.mst = []
    def get_edges(self):
        return self.edges

    def add_edge(self, u, v, weight):  # Crea un arco dati due vertici ed un peso
        self.edges.append((u, v, weight))

    # DSU (Disjoint Set Union) package
    def find_leader(self, parent, i):
        if parent[i] == i:
            return i
            # riassegnazione del nodo padre
            # path compression

        return self.find_leader(parent, parent[i])

    def union(self, parent, rank, x, y):  # Unisce due sets utilizzando il rank
        # Collega il grafo con il rank più piccolo all'altro
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        # Se i rank sono uguali, decido una root e le aumento il rank di 1
        else:
            parent[y] = x
            rank[x] += 1

    def naiveKruskal(self):

        result = []

        # Ordinare tutti gli archi in non-decreasing ordine secondo il loro peso (weight)
        E = sorted(self.edges, key=lambda item: item[2])

        #Inizializzati
        # Creo il sottoinsieme di V di tutti elementi singoli
        parent = list(range(self.V))
        rank = [0] * self.V


        # Dalla teoria dei grafi ci saranno meno di V-1 archi

        for u,v,weight in E:
            # Prendo l'arco più piccolo (ordinati)
            x = self.find_leader(parent, u)
            y = self.find_leader(parent, v)
            #Se l'inclusione di questo arco non crea cicli, allora includerlo e incrementare l'indice
            if x != y:
                result.append((u,v,weight))
                self.union(parent, rank, u, v)

        return result
    def twoBranchesKruskal(self, k):
        result = []
        #Dove k è il valore di mezzo per dividere i due sottoinsiemi
        E1 = [edge for edge in self.edges if edge[2] < k]
        E2 = [edge for edge in self.edges if edge[2] >= k]

        #Come nel metodo naive ordiniamo gli archi
        E1 = sorted(E1, key=lambda item: item[2])
        E2 = sorted(E2, key=lambda item: item[2])

        #Inizializzati
        parent = list(range(self.V))
        rank = [0] * self.V

        #Stesso processo per il sottoinsieme E1
        for u, v, weight in E1:
            x = self.find_leader(parent, u)
            y = self.find_leader(parent, v)
            if x != y:
                result.append((u,v,weight))
                self.union(parent, rank, x, y)

        #Processa E2
        for u, v, weight in E2:
            x = self.find_leader(parent, u)
            y = self.find_leader(parent, v)
            if x != y:
                result.append((u,v,weight))
                self.union(parent, rank, x, y)

        return result

# Utilizzo
g = Kruskal(1000)

edges = set()
while len(edges) < 20000:
    u = random.randint(0,999)
    v = random.randint(0,999)
    if u != v: #Assicuriamoci che non si autoreferenzi
        weight = random.randint(1,100)
        edges.add((u,v,weight))

#Aggiungiamo gli archi creati al grafo
for u, v, weight in edges:
    g.add_edge(u, v, weight)

start = time.time()
mst_naive = g.naiveKruskal()
end = time.time()
elapsed_time_naive = (end-start) * 1000

start = time.time()
mst_twoBranch = g.twoBranchesKruskal(50)
end = time.time()
elapsed_time_tb = (end-start) * 1000

print("Original graph: ")
for u,v,weight in g.get_edges():
    print(f"{u} --- {v} == {weight}")

print(f"\nMST with naive Kruskal, tekes {elapsed_time_naive:.5f}ms: ")
for u, v, weight in mst_naive:
    print(f"{u} --- {v} == {weight}")

print(f"\nMST with two branches Kruskal, takes {elapsed_time_tb:.5f}ms: ")
for u, v, weight in mst_twoBranch:
    print(f"{u} --- {v} == {weight}")

print(f"In conclusion the naive version takes: {elapsed_time_naive:.5f}ms while the two branches version takes: {elapsed_time_tb:.5f}ms")
