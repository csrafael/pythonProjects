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
# - Descrição: Utilizado um grafo representado por lista de adjacentes, por se
# tratar de grafos simples e desconexo, devido as condições do problema.
# Foi adaptado a BFS para contar quantas componentes já foram percorridas.
# Se não tiver mais ninguém na fila e a BFS não percorreu todos os nós do grafo,
# Então acrescente o contator e visite o próximo vértice não verificado.

#@Params    grafo definido por lista de adjacentes
def voosNecessarios (grafo):
    voos = 1 # número de componentes
    #sabendo que para um grafo de n componentes, serão necessárias n-1 arestas
    #para deixar o grafo conexo
    voos = contadorComponentes(grafo,0) - 1

    print ("# de novos voos:",voos)

#@Params    grafo - grafo definido por lista de adjacentes
#           inicio - número do vertice que será a raiz
def contadorComponentes (grafo, inicio):
    fila_busca = [inicio] # fila iniciada com vértice raiz
    naoVisitados = []     # Lista contendo vértices que não foram visitados
    componentes = 1       # Contador de componentes

    # insere todos os vértices em naoVisitados
    for i in range (len(grafo)):
        naoVisitados.append(i)

    while len(fila_busca) > 0:
        vertice = fila_busca.pop(0)

        # verifica se o nó já foi visitado
        if vertice in naoVisitados:
            naoVisitados.remove(vertice)
            # Compara a lista de adjacentes com os vértices não percorridos
            # Retornando apenas os vértices não verificados (intersecção)
            adjNaoVisitados = set(grafo[vertice]).intersection(naoVisitados)
            fila_busca.extend(adjNaoVisitados)

        #Verifica se algum vértice não foi visitado quando a fila está vazia
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
