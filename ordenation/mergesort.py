def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        listLeft = l[:mid]
        listRight = l[mid:]

        merge_sort(listLeft)
        merge_sort(listRight)

        i = j = k = 0
        
        while i < len(listLeft) and j < len(listRight):
            if listLeft[i] < listRight[j]:
                l[k] = listLeft[i]
                i += 1
            else:
                l[k] = listRight[j]
                j += 1
            k += 1

        while i < len(listLeft):
            l[k] = listLeft[i]
            i += 1
            k += 1

        while j < len(listRight):
            l[k] = listRight[j]
            j += 1
            k += 1

l = [99, 4, 1, -1, 5, 9, 3, 2]

print('Antes: ', l)
merge_sort(l)
print('Depois: ', l)