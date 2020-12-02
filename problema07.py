# Rafael Carneiro Soares
# RA: 21059013
# Última alteração:02/12/2020
#
# - Objetivo principal: Identificar o menor custo entre origem e destino
#   todas as coordenadas
#
# - Descrição: Apresenta o menor custo entre dois vértices u v, utilizando
# algoritmo de dijkstra com fila de prioridades binária.

#Biblioteca importada apenas para o cálculo de arredondamento
import math

# descrição: implementação do algoritmo de dijkstra utilizando uma heap binária
# entrada: número do vértice de origem
# retorno: nenhum
def dijkstra (s):
    global digrafo, fila_heap

    heap_decreaseKey(s,0)
    fila_heap[0]['pred'] = s

    while len(fila_heap) > 0:
        u  = heap_extractMin()
        digrafo[u['vertice']]['pred'] = u['pred']
        digrafo[u['vertice']]['custo'] = u['chave']

        vertice_u = digrafo[u['vertice']]

        for v in range(len(vertice_u['saida'])):
            relax(u['vertice'],v)

# descrição: atualiza o predecessor e o custo na fila de prioridades
# entrada: número do vértice de origem
# retorno: nenhum
def relax(u_id,v_id):
    global digrafo,fila_heap

    v = digrafo[u_id]['saida'][v_id]

    if posicao[v] == -1:
        return

    if fila_heap[posicao[v]]['chave'] > digrafo[u_id]['custo'] + w(u_id,v_id):
        fila_heap[posicao[v]]['pred'] = u_id
        heap_decreaseKey(posicao[v], digrafo[u_id]['custo'] + w(u_id,v_id))

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
    global fila_heap, MAX
    vertice_heap = {}
    vertice_heap['chave'] = MAX
    vertice_heap['pred'] = -1
    vertice_heap['vertice'] = i
    fila_heap.append(vertice_heap)

# Apresenta o peso da aresta uv
# Entrada: nomes(índices no digrafo) dos vértices u e v
# retorna a distância entre os vértices u e v
#Complexidade: O(1)
def w (u,v):
    global digrafo
    peso = digrafo[u]['w'][v]
    return peso

# Definição de variáveis globais
# inteiros
MAX = float("inf")  # representação de infinito positivo
n = 1               # quantidade de vértices
m = 0               # quantidade de arestas
o = -1              # origem
d = -1              # destino

fila_heap = []      # lista que representa a heap
posicao = []        # posição atual do vértice na heap de prioridade
digrafo = {}        # matriz para armazenar a lista de adjacentes

n = int(input())
m = int(input())

for i in range(n):
    digrafo[i] = {}
    digrafo[i]['v'] = i
    digrafo[i]['saida'] = []
    digrafo[i]['w'] = []
    digrafo[i]['custo'] = MAX
    posicao.append(i)

    heap_setNode(i)

for i in range(m):
    arco = input()
    arc = arco.split(" ")

    u = int(arc[0])
    v = int(arc[1])
    custo_uv = float(arc[2])

    #adiciona os vértices nas listas de adjacentes
    digrafo[u]['saida'].append(v)
    digrafo[u]['w'].append(custo_uv)

extremos = input()
extremo = extremos.split(" ")

o = int(extremo[0])
d = int(extremo[1])

dijkstra(o)

if digrafo[d]['custo'] == MAX:
    print('ERRO: 3.1415')
else:
    print(digrafo[d]['custo'])
