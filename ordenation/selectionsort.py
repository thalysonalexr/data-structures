def selection_sort(l):
    tam = len(l)
    for i in range(tam):
        menor = i
        for j in range(i, tam):
            if l[j] < l[menor]:
                menor = j
        l[i], l[menor] = l[menor], l[i]


if __name__ == '__main__':
    l = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print('---- * SELECTION SORT * ----')
    print('Antes: ', l)
    selection_sort(l)
    print('Depois: ', l)