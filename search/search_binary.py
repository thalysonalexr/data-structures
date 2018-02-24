from Ordenation import insertion_sort as ord


def pesquisa_binaria(elemento, l):
    tam = len(l)
    inicio = i = 0
    fim = tam -1

    while i < tam:
        meio = (fim + inicio) // 2
        if elemento > l[meio]:
            inicio = meio + 1
        elif elemento < l[meio]:
            fim = meio - 1
        else:
            return meio
        i += 1
    return -1


def pesquisa_binaria_recursiva(l, elemento, inicio, fim):
    meio = int((inicio + fim) / 2)
    if elemento == l[meio]:
        return meio
    if inicio == fim:
        return -1
    else:
        if elemento > l[meio]:
            return pesquisa_binaria_recursiva(l, elemento, meio + 1, fim)
        else:
            return pesquisa_binaria_recursiva(l, elemento, inicio, meio - 1)


if __name__ == '__main__':
    l = ['Maria', 'Nike', 'Thalyson', '@hotmail', 'Ford', 'Battlefield 4']
    ord.insertion_sort(l)
    print(l)
    print('---- * SEARCH BINARY * -----')
    i = pesquisa_binaria_recursiva(l, input('Elemento: '), 0, len(l)-1)
    if i != -1:
        print('Elemento encontrado! Posição %d.' % i)
    else:
        print('O elemento não está na lista.')