# Rafael Carneiro Soares
# RA: 21059013
# Última alteração:18/10/2020
#
# - Objetivo principal: retornar ao Marvin se sua lista de convidados
# resultará numa festa ÉPICA, onde todos os convidados se conhecem.
#
# - Objetivo do programa: indentificar se o subgrafo induzido (lista de
# convidados) é completo. Desta forma, não estou considerando laços e
# arestas paralelas
#
# - Descrição: percorre as listas de convidados verificando completude
# por vacuidade. Em seguida, seleciona um vértice da lista para depois verificar
# se os demais vértices da lista estão presentes no conjunto de vértices
# adjacentes

#@Params    grafo definido por lista de adjacentes
#           listas de contatos no formato de matriz
def churrasEPICO (grafo, listaC):
    resultados = []

    #loop para percorrer listas de convidados
    for i in range(len(listaC)):
        #verifica se a lista de convidados é vazia ou se tem apenas um vértice
        if len(listaC[i]) == 1 or listaC[i][0] == 1 :
            resultados.append("SIM")
            continue

        resultado = "SIM"
        convidados = []

        #retira o primeiro vértice que define o tamanho da lista
        listaC[i].pop(0)
        convidados.extend(list(listaC[i]))

        #loop para percorrer os convidados da lista
        for j in range(len(listaC[i])):

            # retira o vértice da lista para não verificar se o próprio vertice
            # está contido na lista de adjacentes
            vertice = int(convidados.pop(j))
            amigos = grafo[vertice]

            # loop para verificar se os demais vertices da lista são vizinhos
            # do vertice em verificação
            for k in range(len(convidados)):
                if int(convidados[k]) not in amigos:
                    resultado = "NAO"
                    break

            # reinsere o vértice verificado na posição que estava anteriormente
            convidados.insert(j,vertice)

            # para de percorrer a lista atual se algum vértice não tem
            # todos os amigos
            if (resultado == "NAO"):
                break

        resultados.append(resultado)

    return resultados

# inicialização das variáveis
n = 1               #numero de vertices - numero de amigos
m = 0               #numero de arestas  - os amigos sao amigos no haiku
k = 0               #quantidade de lista de amigos
grafo = []          #matriz para armazenar a lista de adjacentes
guests = []         #listas de convidados
resultados = []     #lista que receberá os valores resultados

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

k = int(input())

for i in range(k):
    l = input()
    guests.append(l.split(" "))

resultados = churrasEPICO(grafo,guests)

for result in resultados:
    print(result)
