def quickSort(lista, idxPri, idxUlt):
    if idxPri < idxUlt:
        pontoDiv = dividir(lista, idxPri, idxUlt)
        quickSort(lista, idxPri, pontoDiv-1)
        quickSort(lista, pontoDiv+1, idxUlt)


def dividir(lista, idxPri, idxUlt):
    pivo = lista[idxPri]

    marcEsq = idxPri + 1
    marcDir = idxUlt

    while marcEsq < marcDir:
        while marcEsq <= marcDir and lista[marcEsq] <= pivo:
            marcEsq += 1

        while lista[marcDir] >= pivo and marcDir >= marcEsq:
            marcDir -= 1

        if marcEsq < marcDir:
            temp = lista[marcEsq]
            lista[marcEsq] = lista[marcDir]
            lista[marcDir] = temp

    temp = lista[idxPri]
    lista[idxPri] = lista[marcDir]
    lista[marcDir] = temp

    return marcDir


lista = [5, 3, 2, 4, 1]
quickSort(lista, 0, len(lista)-1)
print(lista)
