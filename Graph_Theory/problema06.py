# Rafael Carneiro Soares
# RA: 21059013
# Última alteração:28/11/2020
#
# - Objetivo principal: Compilar as dependencias de forma ordenada
#
#
# - Objetivo do programa: Identificar a ordenação topológica do makefile

#   descrição:  Inicia a busca em profundidade
#   entrada:    valor numérico do vértice raíz
#   saída:      sem retorno
def DFS (v_inicial):
    global alvo, alvo_v,count_pos,count_pre, grafo, pos, pred, visitado

    count_pos = 1
    count_pre = 1

    #pred[v_inicial] = v_inicial
    DFS_search(v_inicial)

#   descrição:  Função recursiva da busca em profundidade
#   entrada:    valor numérico do vértice
#   saída:      sem retorno
def DFS_search(u):
    global alvo, alvo_v,count_pos,count_pre, grafo, pos, pred, visitado

    visitado[u] = True
    ordem[u] = count_pre
    count_pre += 1

    #busca o vértice atual para facilitar o acesso as dependênciaas/vizinhos de saída
    vertice_u = grafo[u]

    #percorre os vizinhos de saída de u
    for v in range(len(vertice_u['dependencias'])):
        dependencia_v = vertice_u['dependencias'][v]

        #verifica se a dependência foi apresentada como alvo/vertice
        if dependencia_v in grafo_v:
            vertice_v = grafo_v[dependencia_v]

            if visitado[vertice_v] == False:
                #pred[vertice_v] = u
                DFS_search(vertice_v)

    pos[u] = count_pos
    count_pos += 1

#   descrição:  remove ':' de uma string
#   entrada:    string
#   saída:      string sem ":"
def removeDots(linha):
    return linha.replace(':','')

#   descrição:  remove espaçamento inicial de uma string
#   entrada:    string
#   saída:      string sem espaçamento inicial
def removeTabs(linha):
    return linha.lstrip()

#   descrição:  ordena e imprime as instruções
#   entrada:    sem entrada
#   saída:      sem retorno
def sortedInstructions():
    global grafo, pos
    for i in sorted(range(len(pos)), key=lambda k: pos[k]):
        if (pos[i] == -1):
            continue
        vertice = grafo[i]
        for j in range(len(vertice['instrucoes'])):
            print(vertice['instrucoes'][j])

#   descrição:  Função principal que executa as entradas do programa e a chamada da DFS
#   entrada:    sem parâmetros de entrada
#   saída:      sem retorno
def main():
    global alvo, alvo_v, grafo,grafo_v, visitado

    while True:
        linha = input()
        palavra = linha.split(' ')
        ult_V = (len(grafo) - 1,0)[len(grafo)==0]

        if 'make ' in linha:
            alvo = palavra[1]

        elif ':' in linha:
            vertice = {}
            vertice['alvo'] = removeDots(palavra.pop(0))
            vertice['dependencias'] = palavra
            vertice['instrucoes'] = []
            vertice['v'] = len(grafo)

            if vertice['alvo'] == alvo:
                alvo_v = vertice['v']

            grafo[vertice['v']] = vertice
            grafo_v[vertice['alvo']] = vertice['v']

            visitado.append(False)
            ordem.append(-1)
            pos.append(-1)
            pred.append(-1)

        elif linha == 'FIM':
            break

        else:
            grafo[ult_V]['instrucoes'].append(removeTabs(linha))

    DFS(alvo_v)
    sortedInstructions()

#Inicialização das variáveis
alvo = ''
alvo_v = -1
count_pos = 0
count_pre = 0
grafo = {}      #matriz para armazenar a lista de adjacentes
grafo_v = {}    #dict para buscar o valor numérico do vértice passando o alvo
ordem = []      #lista para armazenar valor de pré ordem
pos = []        #lista para armazenar valor de pós ordem
pred = []       #lista para armazenar valor de predecessor
visitado = []   #lista de booleano que armazena se se o vértice já foi visitado

#Executa a função principal
main()
