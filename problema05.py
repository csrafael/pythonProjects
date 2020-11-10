# Rafael Carneiro Soares
# RA: 21059013
# Última alteração:10/11/2020
#
# - Objetivo principal: Identificar menor comprimento necessário para ligar
#   todas as coordenadas
#
# - Objetivo do programa: Identificar a AGM, apresentando o custo total
#   e suas arestas
#
# Descrição:

#Biblioteca importada apenas para o cálculo da distância
import math

# Calcula a distância euclidiana entre dois pontos cartesianos a e b
# Entrada:  tuplas a e b
# Saída:    valor da distância entre os pontos
#Complexidade: O(1)
def dist (a,b):
    d  = (a[0] - b[0])*(a[0] - b[0])
    d += (a[1] - b[1])*(a[1] - b[1])
    return math.sqrt(d)

# Troca posição de dois vértices na variável global da fila
# Entrada:  posição na fila dos vértices u (pai) e v(filho)
#Complexidade: O(1)
def heap_change (pai, filho):
    global fila_heap, posicao

    u = fila_heap[pai]['vertice']
    v = fila_heap[filho]['vertice']

    aux = fila_heap[pai]
    fila_heap[pai] = fila_heap[filho]
    fila_heap[filho] = aux

    posicao[u] = filho
    posicao[v] = pai

# Coloca uma nova menor distância para o vértice e ajusta a posição na fila
# Entrada:  índice n(posição do vértice na fila)  e novo valor de distância
#Complexidade: O(lg n)
def heap_decreaseKey (n, novoValor):
    global fila_heap
    if novoValor < fila_heap[n]['chave']:    #O(1)
        fila_heap[n]['chave'] = novoValor    #O(1)
        heap_fixUp(n)                        #O(lg n)

# Extrai o vértice de menor custo (será sempre a raiz) e corrige a heap
# Retorno: vértice de menor custo
#Complexidade: O(lg n)
def heap_extractMin ():
    global fila_heap, posicao

    heap_change(0,len(fila_heap)-1)     #O(1)
    u = fila_heap.pop()                 #O(1)
    # Identifica que o vértice já não está na heap
    posicao[u['vertice']] = -1          #O(1)
    heap_fixDown(0)                     #O(lg n)

    return u

# Corrige a Heap da raiz para as folhas
# Entrada:  posição do primeiro vértice a ser corrigido
#Complexidade: O(lg n)
def heap_fixDown(i):
    global fila_heap

    e = heap_leftChild(i)
    d = heap_rightChild(i)

    min = i

    if e < len(fila_heap) and fila_heap[e]['chave'] < fila_heap[i]['chave']:
        min = e

    if d < len(fila_heap) and fila_heap[d]['chave'] < fila_heap[min]['chave']:
        min = d

    if min != i:
        heap_change(i,min)
        heap_fixDown(min)

# Corrige a Heap da folha para a raiz
# Entrada:  posição do primeiro vértice a ser corrigido
#Complexidade: O(lg n)
def heap_fixUp (i):
    global fila_heap

    #O(lg n)
    while i > 0 and fila_heap[heap_parent(i)]['chave'] > fila_heap[i]['chave']:
        heap_change(heap_parent(i), i) #O(1)
        i = heap_parent(i)             #O(1)

# Retorna o índice do filho esquerdo do vértice, na heap, com base na heap
# iniciando em 0
#Entrada: índice i do vértice na heap
#Retorno: inteiro que representa o índice do filho esquerdo
#Complexidade: O(1)
def heap_leftChild(i):
    return ( (i+1) * 2 ) - 1

#Retorna o índice do pai do vértice, na heap, com base na heap iniciando com zero
#Entrada: índice i do vértice na heap
#Retorno: inteiro que representa o índice nó pai
#Complexidade: O(1)
def heap_parent(i):
    if i%2 == 0 :
        return math.floor(i/2) -1

    return math.floor(i/2)

# Retorna o índice do filho direito do vértice, na heap, com base na heap
# iniciando em 0
#Entrada: índice i do vértice na heap
#Retorno: inteiro que representa o índice do filho direito
#Complexidade: O(1)
def heap_rightChild(i):
    return (i+1) * 2

# Inicia o vértice i na heap
# Entrada: número do vértice
#Complexidade: O(1)
def heap_setNode (i):
    global fila_heap, INT_MAX
    vertice_heap = {}
    vertice_heap['chave'] = INT_MAX
    vertice_heap['pred'] = -1
    vertice_heap['vertice'] = i
    fila_heap.append(vertice_heap)

# Executa o algoritmo de prim para retornar a AGM
#O(n² lg n)
def prim ():
    global fila_heap, grafo, posicao, arestas_r, comprimento_r

    #O(n² lg n)
    while len(fila_heap) > 0:           #O(n)
        # Extrai o menor valor da heap
        u  = heap_extractMin()          #O(lg n)
        u_id = u['vertice']
        vertice_u = grafo[u_id]

        #verificação para garantir que não insira laços
        if u_id != u['pred']:
            comprimento_r += u['chave']

            if (u['pred'] < u_id):
                aresta = (u['pred'],u_id)
            else:
                aresta = (u_id,u['pred'])

            arestas_r.append(aresta)

        #laço que percorre os adjacentes do vértice
        #O (n lg n)
        for i in range(len(vertice_u['adj'])): #O(n)
            v = vertice_u['adj'][i]
            v_id = i
            v_dist = vertice_u['dist'][i]

            #Verifica se v está na heap
            if (posicao[v] == -1):
                continue

            v_fila = fila_heap[ posicao[v] ]

            if w(u_id,v_id) < v_fila['chave']:
                    v_fila['pred'] = u_id
                    heap_decreaseKey (posicao[v], w(u_id,v_id) ) #O(lg n)

# Apresenta o comprimento e as arestas ordenadas escolhidas pelo alg. de prim
# Complexidade: O(n lg n)
def result():
    global comprimento_r, arestas_r
    print("comprimento de cabeamento minimo: {:.4f}".format(comprimento_r))
    arestas_r = sorted(arestas_r) #O(n lg n)
    #O(n)
    for i in range(len(arestas_r)):
        print(str(arestas_r[i][0])+" "+str(arestas_r[i][1]))

# Define o grafo completo e as distâncias dos pares de vértices.
#Complexidade: O(n²)
def setGraph ():
    global grafo, n

    for u in range(n-1):
        # Se for a primeira execução, inicia adj e dist
        if u == 0:
            grafo[u]['adj'] = []
            grafo[u]['dist'] = []

        for v in range (n-u):
            # Se for a primeira execução, inicia adj e dist de todos os vértices
            if u == 0:
                grafo[v]['adj'] = []
                grafo[v]['dist'] = []

            if len(grafo[v+u]['adj']) == n:
                break

            if u == (v+u):
                continue

            u_coord = coordenadas[u]
            v_coord = coordenadas[v+u]

            grafo[u]['adj'].append(v+u)
            grafo[u]['dist'].append(dist(u_coord,v_coord))

            grafo[v+u]['adj'].append(u)
            grafo[v+u]['dist'].append(dist(u_coord,v_coord))

# Defini o ínicio do algoritmo de prim em zero
#Complexidade: O(1)
def setStart():
    global fila_heap
    fila_heap[0]['pred'] = 0
    fila_heap[0]['chave'] = 0

# Apresenta o peso da aresta uv
# Entrada: nomes(índices no grafo) dos vértices u e v
# retorna a distância entre os vértices u e v
#Complexidade: O(1)
def w (u,v):
    global grafo
    peso = grafo[u]['dist'][v]
    return peso

# Definição de variáveis globais
#inteiros
INT_MAX = 9999999   # constante para setar a chave da heap como infinito
n = 1               # quantidade de coordenadas a serem inseridas

#flutuantes
comprimento_r = 0.0 # comprimento total da AGM

#listas
arestas_r = []      # lista de tuplas para armazenar as arestas da AGM
coordenadas = []    # lista de tuplas para armazenar as coordenadas de cada nó
fila_heap = []      # lista que representa a heap
grafo = []          # matriz para armazenar a lista de adjacentes
posicao = []        # posição atual do vértice na heap de prioridade

n = int(input())

# Complexidade O(n)
for i in range(n):
    grafo.append({})
    posicao.append(i)
    heap_setNode(i)

    ponto = input()
    ponto = ponto.split(" ")

    x = int(ponto[0])
    y = int(ponto[1])

    coord = (x,y)
    coordenadas.append(coord)

setGraph()  #O(n²)
setStart()  #O(1)
prim()      #O(n² lg n)
result()    #O(n lg n)
