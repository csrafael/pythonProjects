# Rafael Carneiro Soares
# RA: 21059013
# Última alteração:01/11/2020
#
# - Objetivo principal:
#
# .
#
# - Objetivo do programa:
#
#
# - Descrição:
#
#
#
#

def min (x, y):
    if x < y:
        return x

    return y


def DFS (grafo, raiz):

    global nVisitado, pred, ordem

    for u in range ( len(grafo) ):
        nVisitado.append(u)
        pred.append(-1)
        ordem.append(-1)
        low.append(-1)

    pred[raiz] = raiz

    DFS_Corte(grafo, raiz)


def DFS_Corte (grafo, u):
    global nVisitado, count, ord, low, pred, cortes

    count = count + 1
    ordem[u] = count
    low[u] = count

    nVisitado.remove(u)

    if len(grafo[u])>2 and pred[u] == u:
        cortes.append(u)

    for v in grafo[u]:
        if v in nVisitado:
            pred[v] = u
            DFS_Corte(grafo,v)

            if low[v] == ordem[v] and len(grafo[u])>=2 and u not in cortes:
                cortes.append(u)

            low[u] = min(low[u], low[v])
        else:
            if v != pred[u]:
                low[u] = min(low[u], ordem[v])

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
nVisitado = []
cortes = []
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

print ("# de alvos possiveis:",len(cortes))
for i in range (len(cortes)):
    print(cortes[i])
