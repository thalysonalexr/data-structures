def busca_linear_recursiva(elemento, l, idx=0):
    if elemento == l[idx]:
        return idx
    if idx == len(l)-1:
        return -1
    return busca_linear_recursiva(elemento, l, idx + 1)


def busca_linear(elemento, l):
    for i, e in enumerate(l):
        if elemento == e:
            return i
    return -1


if __name__ == '__main__':
    l = [44, 12, 43, 8, 99, 13, 1, -1, 4]
    i = busca_linear_recursiva(int(input('Elemento: ')), l)
    print('---- * LINEAR SEARCH * ----')
    if i != -1:
        print('Elemento encontrado! Posição %d.' % i)
    else:
        print('O elemento não está na lista.')