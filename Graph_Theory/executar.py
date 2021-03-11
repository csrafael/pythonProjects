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
    {"v":0,"nome":"Oradea","h":380 , "vizinhos":[1,7], "dist":[71,151]},
    {"v":1,"nome":"Zerind","h":374 , "vizinhos":[0,2], "dist":[71,75]},
    {"v":2,"nome":"Arad","h":366 , "vizinhos":[1,3,7], "dist":[75,118,140]},
    {"v":3,"nome":"Timisoara","h":329 , "vizinhos":[2,4], "dist":[118,111]},
    {"v":4,"nome":"Lugoj","h":244 , "vizinhos":[3,5], "dist":[111,70]},
    {"v":5,"nome":"Mehadia","h":241 , "vizinhos":[4,6], "dist":[70,75]},
    {"v":6,"nome":"Dobreta","h":242 , "vizinhos":[5,9], "dist":[75,120]},
    {"v":7,"nome":"Sibiu","h":253 , "vizinhos":[0,2,8,10], "dist":[151,140,80,99]},
    {"v":8,"nome":"Rimnicu Vilcea","h":193 , "vizinhos":[7,9,11], "dist":[80,146,97]},
    {"v":9,"nome":"Craiova","h":160 , "vizinhos":[6,8,11], "dist":[120,146,138]},
    {"v":10,"nome":"Fagaras","h":176 , "vizinhos":[7,12], "dist":[99,211]},
    {"v":11,"nome":"Pitesti","h":100 , "vizinhos":[8,9,12], "dist":[97,138,101]},
    {"v":12,"nome":"Bucarest","h":0 , "vizinhos":[10,11,13,14], "dist":[211,101,90,85]},
    {"v":13,"nome":"Giurgiu","h":77 , "vizinhos":[12], "dist":[90]},
    {"v":14,"nome":"Urziceni","h":80 , "vizinhos":[12,15,18], "dist":[85,142,98]},
    {"v":15,"nome":"Vaslui","h":199 , "vizinhos":[14,16], "dist":[142,92]},
    {"v":16,"nome":"Iasi","h":226 , "vizinhos":[15, 17],"dist":[92,87]},
    {"v":17,"nome":"Neamt","h":234 , "vizinhos":[16],"dist":[87]},
    {"v":18,"nome":"Hirsova","h":151 , "vizinhos":[14, 19],"dist":[98,86]},
    {"v":19,"nome":"Eforie","h":161 , "vizinhos":[18],"dist":[86]}
]


caminho1 = []
caminho2 = []
caminho3 = []
fila = []
dist = 0
buscas.busca_largura(listaAdj, 2, 12)

print (buscas.busca_profundidade(listaAdj,2,12,caminho1))

print ( buscas.busca_gulosa(grafo, 2, caminho2) )

print ( buscas.busca_aEstrela(grafo, 2, caminho3, fila, dist) )
