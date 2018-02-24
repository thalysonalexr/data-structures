def insertion_sort(l):
    for i in range(1, len(l)):
        elemento = l[i]
        j = i
        while j > 0 and elemento < l[j-1]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1


if __name__ == '__main__':
    l = [3, 2, 1]
    print('---- * INSERTION SORT * ----')
    print('Antes: ', l)
    insertion_sort(l)
    print('Depois: ', l)