from grafo import Grafo


def montar_grafo_eliminacao(lista_times, alvo_idx):
    """
    lista_times: lista de dicts [{'nome': 'Time', 'v': 10, 'r': 3, 'jogos': {1: 1, 2: 1}}, ...]
    alvo_idx: índice do time que queremos testar
    """
    n_times = len(lista_times)
    alvo = lista_times[alvo_idx]
    p_max_alvo = alvo['v'] + alvo['r']

    #1: Verificação Trivial
    for i, time in enumerate(lista_times):
        if time['v'] > p_max_alvo:
            return None, 0

            #2 Coletar confrontos entre adversários
    confrontos = []
    for i in range(n_times):
        for j in range(i + 1, n_times):
            if i != alvo_idx and j != alvo_idx:
                n_jogos = lista_times[i]['jogos'].get(j, 0)
                if n_jogos > 0:
                    confrontos.append(((i, j), n_jogos))

    #3: Definir Nós e Criar Objeto Grafo
    n_jogos = len(confrontos)
    n_adversarios = n_times - 1
    total_nos = 1 + n_jogos + n_adversarios + 1

    g = Grafo(total_nos)
    s, t = 0, total_nos - 1
    fluxo_necessario = 0

    # Mapeamento de times
    mapa_times = {}
    cont = 0
    for i in range(n_times):
        if i != alvo_idx:
            mapa_times[i] = n_jogos + 1 + cont
            cont += 1

    # 4: Construir Arestas no Objeto Grafo
    for idx, ((t1, t2), n_partidas) in enumerate(confrontos):
        no_jogo = idx + 1
        g.adicionar_aresta(s, no_jogo, n_partidas)
        fluxo_necessario += n_partidas
        g.adicionar_aresta(no_jogo, mapa_times[t1], float('inf'))
        g.adicionar_aresta(no_jogo, mapa_times[t2], float('inf'))

    for i in range(n_times):
        if i != alvo_idx:
            folga = p_max_alvo - lista_times[i]['v']
            g.adicionar_aresta(mapa_times[i], t, folga)

    return g, fluxo_necessario
