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
    {"v":0,"nome":"Oradea","h":380 , "vizinhos":[1,7]},
    {"v":1,"nome":"Zerind","h":374 , "vizinhos":[0,2]},
    {"v":2,"nome":"Arad","h":366 , "vizinhos":[1,3,7]},
    {"v":3,"nome":"Timisoara","h":329 , "vizinhos":[2,4]},
    {"v":4,"nome":"Lugoj","h":244 , "vizinhos":[3,5]},
    {"v":5,"nome":"Mehadia","h":241 , "vizinhos":[4,6]},
    {"v":6,"nome":"Dobreta","h":242 , "vizinhos":[5,9]},
    {"v":7,"nome":"Sibiu","h":253 , "vizinhos":[0,2,8,10]},
    {"v":8,"nome":"Rimnicu Vilcea","h":193 , "vizinhos":[7,9,11]},
    {"v":9,"nome":"Craiova","h":160 , "vizinhos":[6,8,11]},
    {"v":10,"nome":"Fagaras","h":176 , "vizinhos":[7,12]},
    {"v":11,"nome":"Pitesti","h":100 , "vizinhos":[8,9,12]},
    {"v":12,"nome":"Bucarest","h":0 , "vizinhos":[10,11,13,14]},
    {"v":13,"nome":"Giurgiu","h":77 , "vizinhos":[12]},
    {"v":14,"nome":"Urziceni","h":80 , "vizinhos":[12,15,18]},
    {"v":15,"nome":"Vaslui","h":199 , "vizinhos":[14,16]},
    {"v":16,"nome":"Iasi","h":226 , "vizinhos":[15, 17]},
    {"v":17,"nome":"Neamt","h":234 , "vizinhos":[16]},
    {"v":18,"nome":"Hirsova","h":151 , "vizinhos":[14, 19]},
    {"v":19,"nome":"Eforie","h":161 , "vizinhos":[18]}
]


caminho = []
#buscas.busca_largura(listaAdj, 2, 12)
#print (buscas.busca_profundidade(listaAdj,2,12,caminho))

print ( buscas.busca_gulosa(grafo, 2, caminho) )
