def algoritmo(input, arreglo):
    i = rango[0]
    j = rango[1]
    coma = False
    while i <= j:
        encontrado = False
        for k in range(len(input)):
            elem = input[k]
            if i == elem:
                encontrado = True
                break;
        if encontrado == False:
            if coma == False:
                coma = True
                print(i, end = ""),
            else:
                print(", " + str(i), end = "")
        i += 1

if __name__ == "__main__":
    input = [10,12,11,15]
    rango = [10,17]
    algoritmo(input, rango)