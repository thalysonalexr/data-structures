def bubble_sort(l):
	tam = len(l)
	for i in range(tam):
		trocou = False
		for j in range(tam-1):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
				trocou = True
		if not trocou:
			return


if __name__ == '__main__':
	l = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
	print('---- * BUBBLE SORT * ----')
	print('Antes: ', l)
	bubble_sort(l)
	print('Depois: ', l)