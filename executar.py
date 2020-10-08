import buscas

listaAdj = [
    [1,7],              #Oradea
    [0,2],              #Zerind
    [1,3,7],            #Arad
    [2,4],              #Timisoara
    [3,5],              #Lugoj
    [4,6],              #Mehadia
    [5,9],              #Dobreta
    [0,2,8,10],         #Sibiu
    [7,9,11],           #Rimnicu Vilcea
    [6,8,11],           #Craiova
    [7,12],             #Fagaras
    [8,9,12],           #Pitesti
    [10,11,13,14],      #Bucarest
    [12],               #Giurgiu
    [12,15,18],         #Urziceni
    [14,16],            #Vaslui
    [15, 17],           #Lasi
    [16],               #Neamt
    [14, 19],           #Hirsora
    [18]                #Eforie
]

grafo = [
    {"id":"0","nome":"Oradea", "vizinhos":[1,7]},
    {"id":"1","nome":"Zerind", "vizinhos":[0,2]},
    {"id":"2","nome":"Arad", "vizinhos":[1,3,7]},
    {"id":"3","nome":"Timisoara", "vizinhos":[2,4]},
    {"id":"4","nome":"Lugoj", "vizinhos":[3,5]},
    {"id":"5","nome":"Mehadia", "vizinhos":[4,6]},
    {"id":"6","nome":"Dobreta", "vizinhos":[5,9]},
    {"id":"7","nome":"Sibiu", "vizinhos":[0,2,8,10]},
    {"id":"8","nome":"Rimnicu Vilcea", "vizinhos":[7,9,11]},
    {"id":"9","nome":"Craiova", "vizinhos":[6,8,11]},
    {"id":"10","nome":"Fagaras", "vizinhos":[7,12]},
    {"id":"11","nome":"Pitesti", "vizinhos":[8,9,12]},
    {"id":"12","nome":"Bucarest", "vizinhos":[10,11,13,14]},
    {"id":"13","nome":"Giurgiu", "vizinhos":[12]},
    {"id":"14","nome":"Urziceni", "vizinhos":[12,15,18]},
    {"id":"15","nome":"Vaslui", "vizinhos":[14,16]},
    {"id":"16","nome":"Lasi", "vizinhos":[15, 17]},
    {"id":"17","nome":"Neamt", "vizinhos":[16]},
    {"id":"18","nome":"Hirsora", "vizinhos":[14, 19]},
    {"id":"19","nome":"Eforie", "vizinhos":[18]}
]

caminho = []
buscas.busca_largura(listaAdj, 2, 12)
print (buscas.busca_profundidade(listaAdj,2,12,caminho))
