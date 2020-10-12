def sortH(e):
  return e['h']

def backtrace(pais, inicio, fim):
    caminho = [fim]
    while caminho[-1] != inicio:
        caminho.append(pais[caminho[-1]])
    caminho.reverse()
    return caminho

def busca_largura (grafo, inicio, fim):
    fila_busca = [inicio]
    visitados = caminho = []
    pais = {}
    while len(fila_busca) > 0:
        vertice = fila_busca.pop(0)
        if fim in caminho:
            print("Caminho ", backtrace(pais,inicio,fim))
            break;

        elif vertice not in visitados:
            visitados.append(vertice)
            caminho.append(vertice)
            adjNaoVisitados = set(grafo[vertice]).difference(visitados)
            fila_busca.extend(adjNaoVisitados)
            for vizinho in adjNaoVisitados:
                pais[vizinho] = vertice

def busca_profundidade (grafo, inicio, fim, caminho):

    caminho.append(inicio)

    if caminho[-1] == fim:
        return caminho

    novoCaminho = []

    for i in grafo[inicio]:
        if i in caminho:
            continue

        novoCaminho = busca_profundidade(grafo, i, fim, caminho)

        if caminho[-1] == fim:
            break

    return novoCaminho

def busca_gulosa (grafo, inicio, caminho):
    vizinhos = []

    if (len(caminho)>0 and grafo[caminho[-1]]['h'] == 0):
        return caminho

    caminho.append(inicio)

    print("VERTICE ", grafo[inicio])
    print("HEURISTICA ", grafo[inicio]['h'])

    if (grafo[inicio]['h'] == 0):
        return caminho;


    for i in range(len(grafo[inicio]["vizinhos"])):
        vizinhos.append(grafo[ grafo[inicio]["vizinhos"][i] ])

    vizinhos.sort(key= lambda x:x['h'])

    return busca_gulosa(grafo,vizinhos[0]["v"],caminho)

def busca_aEstrela ():
    print("OI")
