class Grafo:
    def __init__(self, n):
        self.n = n
        # Matriz de adjacência para capacidades
        self.capacidade = [[0] * n for _ in range(n)]
        
    def adicionar_aresta(self, u, v, cap):
        self.capacidade[u][v] = cap
