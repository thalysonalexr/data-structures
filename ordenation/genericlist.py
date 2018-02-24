def add_sort(l, value):
    if not l:
        l.append(value)
    else:
        i = 0
        tam = len(l)
        while i < tam:
            if value < l[i]:
                l.insert(i, value)
                return
            i += 1
        l.append(value)


def add_des(l, value):
    l.append(value)


def insert_value():
    while True:
        try:
            return int(input('Value, Exit(0): '))
        except ValueError:
            print('Please, enter integer type numbers.')


def print_screen(list_value):
    print(list_value)


def main():
    l = []
    op = 1

    while op != 0:
        print('1 - Inserir ord.\n2 - Inserir des.\n3 - Imprimir\n0 - Sair')
        op = int(input('? '))
        if op == 1:
            n = int(input('Valor: '))
            add_sort(l, n)
        elif op == 2:
            n = int(input('Valor: '))
            add_des(l, n)
        elif op == 3:
            print_screen(l)
        elif op == 0:
            print('Adios')

main()