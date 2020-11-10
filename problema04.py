# Rafael Carneiro Soares
# RA: 21059013
# Última alteração:01/11/2020
#
# - Objetivo principal: Identificar terminais que causam desconexam de
#   pelo menos dois terminais
#
#
# - Objetivo do programa: Identificar vértices de corte nos componentes

#Função que retorna o mínimo entre duas entradas
def min (x, y):
    if x < y:
        return x

    return y

#função de inicialização de busca
def DFS (grafo, raiz):
    #identifica variáveis globais
    global nVisitado, pred, ordem

    #preenche as variaveis globais
    for u in range ( len(grafo) ):
        nVisitado.append(u)
        pred.append(-1)
        ordem.append(-1)
        low.append(-1)

    pred[raiz] = raiz

    #inicializa a busca em profundidade
    DFS_Corte(grafo, raiz)


def DFS_Corte (grafo, u):
    global nVisitado, count, ord, low, pred, cortes

    count = count + 1
    ordem[u] = count
    low[u] = count

    nVisitado.remove(u)

    for v in grafo[u]:
        if v in nVisitado:
            pred[v] = u
            DFS_Corte(grafo,v)
            #Identifica a aresta de corte e diz que u é vertice de corte.
            # neste momento já foi retornado se v é articulação.
            if low[v] == ordem[v] and len(grafo[u]) >=2 and u not in cortes:
                cortes.append(u)

            low[u] = min(low[u], low[v])
        else:
            if v != pred[u]:
                low[u] = min(low[u], ordem[v])

    #Condição para verificar se o nó raiz da árvore é um vértice de corte.
    #Observação: Por algum motivo que não fui capaz de identificar,
    #essa condição é satisfeita de maneira equivocada
    if pred[u] == u and len(grafo[u]) >2 and low[u]==ordem[u] and u not in cortes:
        i=1#cortes.append(u)

    #condição para continuar a verificar os demais vértices de um outro componente
    if len(nVisitado) > 0 and pred[u] == u:
        pred[nVisitado[0]] = nVisitado[0]
        DFS_Corte(grafo,nVisitado[0])

# inicialização das variáveis
n = 1               #numero de vertices - numero de amigos
m = 0               #numero de arestas  - os amigos sao amigos no haiku
count = 0
grafo = []          #matriz para armazenar a lista de adjacentes
ordem = []
pred = []
nVisitado = []      #
cortes = []         #lista que receberá as respostas
low = []

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

DFS(grafo,0)
cortes = sorted(cortes)
print ("# de alvos possiveis:",len(cortes))
for i in range (len(cortes)):
    print(cortes[i])
