def min_arista(nodos,aristas,nodo,visitados):
    min = (21,nodo)
    for destino in range(len(nodos)):
            if nodo!=destino and aristas[nodo][destino] < min[0]:
                min = (aristas[nodo][destino],destino)
    return min

def min_arista1(nodos,aristas,visitados):
    min = (21,visitados[0])
    for nodo in visitados:
        for destino in range(len(nodos)):
            if destino not in visitados and aristas[nodo][destino] < min[0]:
                min = (aristas[nodo][destino],destino,nodo)
    return min

def costos(n,aristas,nodos):
    for nodo in range(n):
        for destino in range(nodo,n):
            if nodo != destino:
                costo = 0
                for i in range(4):
                        c = abs(nodos[nodo][i] - nodos[destino][i])
                        if c > 5:
                            costo+= 10-c
                        else:
                            costo+=c
                aristas[nodo][destino] = costo
                aristas[destino][nodo] = costo

def prim(n,nodos,aristas):
    conexos = [-1 for _ in range(n)]
    visitados = [nodos[0]]
    arbol = []
    while len(visitados) < n:
         min = min_arista1(nodos,aristas,visitados)
         visitados.append(min[1])
         arbol.append((min[2],min[1]))
    #for nodo in range(n):
         
            #if conexos[nodo] == -1:
            #    min = min_arista(nodos,aristas,nodo,visitados)

#                if conexos[min[1]] == -1:
 #                     conexos[min[1]] = min[1]
  #              conexos[nodo] = conexos[min[1]]
   #             for i in range(n):
    #                if conexos[i] == nodo:
     #                   conexos[i] = conexos[min[1]]
                          
            #if nodo not in visitados:
            #    visitados.append(nodo)
            #    min = min_arista(nodos,aristas,nodo,visitados)
            #    arbol.append((nodo,min[1]))
            #    visitados.append(min[1])

    return arbol

def main():
    test_case = int(input())
    
    for _ in range(test_case):
        string_nodes = input().split()
        n = int(string_nodes[0])
        nodos = []
        aristas = [[0]*n for _ in range(n)]

        #creamos nuestros nodos a partir de nuestro input str (separamos los digitos en listas de de 4 números)
        for i in range(n):
            nodos.append( [int(x) for x in string_nodes[i+1]] )

        #calculamos el costo de todas las aristas entre los nodos (el costo de cambiar de una contraseña a otra)
        #O(n**2)/2
        costos(n,aristas,nodos)
        
        arbol = prim(n,nodos,aristas)
        print(arbol)

        #agregamos el nodo [0,0,0,0] y calculamos su distancia al resto de nodos
        nodos.append([0,0,0,0])
        aristas_1 = [0 for _ in range(n)]
        for nodo in range(n):
            costo = 0
            for i in range(4):
                        c = nodos[nodo][i]
                        if c > 5:
                            costo+= 10-c
                        else:
                            costo+=c
            aristas_1[nodo] = costo
        #agregamos la conexión al nodo [0000] como la cantidad de rolls iniciales
        rolls = min(aristas_1)
        for i in range(len(arbol)):
            rolls += aristas[arbol[i][0]][arbol[i][1]]
        print(rolls)

if __name__ == "__main__":
    main()