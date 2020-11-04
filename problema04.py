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

    global visitado, pred, ordem

    for u in range ( len(grafo) ):
        pred.append(-1)
        ordem.append(-1)
        low.append(999)

    pred[raiz] = raiz

    DFS_Corte(grafo, raiz)


def DFS_Corte (grafo, raiz):
    global visitado, count, ord, low, pred, cortes

    visitado.append(raiz)
    count = count + 1
    ordem[raiz] = count
    low[raiz] = count

    print('VISITADO', visitado)
    print('COUNT', count)
    print('ORDEM', ordem[raiz])
    print('LOW', low[raiz])

    print('ADJ', grafo[raiz])


    for v in grafo[raiz]:
        if v not in visitado:
            pred[v] = raiz
            DFS_Corte(grafo,v)
            print('LOW V',low[v])
            print('ORDEM V', ordem[v])
            if (low[v] == ordem[v]):
                cortes.append(v)
            low[raiz] = min(low[raiz], low[v])
            if ordem[raiz] == 1 and len(grafo[raiz])>1:
                cortes.append(raiz)
        else:
            if v != pred[raiz]:
                low[raiz] = min(low[raiz], ordem[v])

# inicialização das variáveis
n = 1               #numero de vertices - numero de amigos
m = 0               #numero de arestas  - os amigos sao amigos no haiku
count = 0
grafo = []          #matriz para armazenar a lista de adjacentes
ordem = []
pred = []
visitado = []
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
print ('LOW ', low)
print ('VISITADO ', visitado)
print('PRED', pred)
print ("# de alvos possiveis:",len(cortes))
for i in range (len(cortes)):
    print(cortes[i])
