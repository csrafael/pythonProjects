print('Enter your name:')
x = input()
print('Hello, ' + x)

6
6
0 1
0 4
5 3
3 2
2 1
1 3
3
3 0 1 3
3 1 2 3
2 4 3


for j in range(len(listaC[i])):
    if j == 0:
        continue

    print("Lista ",convidados[i])

    vertice = convidados[i].pop(j)
    print("Vertice ",vertice)
    amigos = grafo[j]
    print("AMIGOS ",amigos)
    for k in len(convidados[i]):
        if convidados[i][k] in amigos:
            convidados[i].insert(j,vertice)
            continue
        else:
            resultado = "NAO"
            break
