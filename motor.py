from navegador import bfs

def edmonds_karp(grafo, s, t):
    n = grafo.n
    fluxo = [[0] * n for _ in range(n)]
    fluxo_maximo = 0
    parent = [-1] * n

    while bfs(n, grafo.capacidade, fluxo, s, t, parent):
        # Acha o gargalo (menor capacidade no caminho encontrado)
        caminho_fluxo = float('Inf')
        v = t
        while v != s:
            u = parent[v]
            caminho_fluxo = min(caminho_fluxo, grafo.capacidade[u][v] - fluxo[u][v])
            v = parent[v]

        # Atualiza o fluxo e o fluxo reverso
        v = t
        while v != s:
            u = parent[v]
            fluxo[u][v] += caminho_fluxo
            fluxo[v][u] -= caminho_fluxo
            v = parent[v]

        fluxo_maximo += caminho_fluxo
    return fluxo_maximo
