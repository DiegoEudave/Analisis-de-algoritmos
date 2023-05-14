import random
import sys

def solInicial(tamano):
    reinas = []
    for i in range(tamano):
        reinas.append(i)
    return reinas
    
#Sabemos que no pueden estar en la misma fila ni columna
def evaluar(reinas):
    eval = 0
    for x in range(len(reinas)):
        y = reinas[x]
        for r in range(len(reinas)):
            if r != x:
                if reinas[r] == y - x + r or reinas[r] == y + x - r:
                    eval += 1
                    break
    return eval

def mutar(reinas):
    nuevaSol = reinas.copy()
    indices = list(range(len(nuevaSol)))
    i = random.choice(indices)
    indices.remove(i)
    j = random.choice(indices)
    tmp = nuevaSol[i]
    nuevaSol[i] = nuevaSol[j]
    nuevaSol[j] = tmp
    return nuevaSol

def hillClimbing(reinas):
    sol = solInicial(reinas)
    iters = 0
    while(evaluar(sol) != 0):#Si se queda estancado mucho tiempo, reiniciamos la búsqueda
        iters += 1
        if(iters == 1000):
            sol = solInicial(reinas)
            iters = 0
        solCand = mutar(sol)
        if(evaluar(solCand) <= evaluar(sol)):
            sol = solCand
    return sol

def printBonito(sol):
    tablero = []
    for i in sol:
        lista = ["."] * len(sol)
        lista[i] = "Q"
        tablero.append("".join(lista))
    for l in tablero:
        print(str(l))

def printCorrecto(sol):
    tablero = []
    for i in sol:
        lista = ["."] * len(sol)
        lista[i] = "Q"
        tablero.append("".join(lista))
    print(tablero)


if __name__ == "__main__":
    n = int(sys.argv[1])
    solucion = hillClimbing(n)
    #printCorrecto(solucion)
    printBonito(solucion)
    
    