# Rafael Carneiro Soares
# RA: 21059013
# Última alteração:27/10/2020
#
# - Objetivo principal: dada a malha aérea, determinar o menor número de voos
# diretos que ela precisa começar a operar a fim de transportar um passageiro
# entre todos os aeroportos operados por ela.
#
# - Objetivo do programa: Identificar a quantidade de componentes de um grafo e
# retornar a quantidade de arestas necessárias para ter apenas um componente.
#
# - Descrição:

#@Params    grafo definido por lista de adjacentes
def voosNecessarios (grafo):
    voos = 1 # número de componentes

    voos = contadorComponentes(grafo,0) - 1

    print ("# de novos voos:",voos)

def contadorComponentes (grafo, inicio):
    fila_busca = [inicio]
    naoVisitados = []
    componentes = 1

    for i in range (len(grafo)):
        naoVisitados.append(i)

    while len(fila_busca) > 0:
        vertice = fila_busca.pop(0)

        if vertice in naoVisitados:
            naoVisitados.remove(vertice)
            adjNaoVisitados = set(grafo[vertice]).intersection(naoVisitados)
            fila_busca.extend(adjNaoVisitados)

        if len(naoVisitados) > 0 and len(fila_busca) == 0:
            componentes += 1
            novoVertice = naoVisitados[0]
            fila_busca.append(novoVertice)

    return componentes

# inicialização das variáveis
n = 1               #numero de vertices - numero de amigos
m = 0               #numero de arestas  - os amigos sao amigos no haiku
grafo = []          #matriz para armazenar a lista de adjacentes

n = int(input())
m = int(input())

for i in range(n):
    grafo.append([])

for i in range(m):
    aresta = input()
    edges = aresta.split(" ")

    u = int(edges[0])
    v = int(edges[1])

    #adiciona os vértices nas listas de adjacentes
    grafo[u].append(v)
    grafo[v].append(u)

voosNecessarios(grafo)
