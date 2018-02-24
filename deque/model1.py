'''
DEQUE - Double Ended Queue
Book Sale System

by: Thalyson A. R. de Sousa e Nicolas Thiago
'''

from datetime import date


class Data(object):
    def __init__(self, title=None, author=None, n_pages=0, price=0,
                 category=None, pub_company=None, year=0, id_b=0):
        self.title = title
        self.author = author
        self.n_pages = n_pages
        self.price = price
        self.category = category
        self.pub_company = pub_company
        self.year = year
        self.id = id_b
        self.next = None


class Deque(Data):
    def __init__(self):
        self.flag = None


ID_BOOK = 0


def generator_id():
    global ID_BOOK
    ID_BOOK += 1
    return ID_BOOK


# Verificar deque vazio
def is_empty(deque):
    return deque.flag is None


# Inserir novo nó no início do deque
def add_first(deque):
    new_node = input_data()
    new_node.next = deque.flag
    deque.flag = deque.next = new_node


# Remover nó do início do deque
def pop_first(deque):
    if is_empty(deque):
        return False
    deque.flag = deque.flag.next
    deque.next = deque.next.next


# Inserir nó no final do deque
def add_last(deque):
    new_node = input_data()
    while deque.next is not None:
        deque = deque.next
    deque.next = new_node


# Remover nó do final do deque
def pop_last(deque):
    if is_empty(deque):
        return False
    if deque.next.next is None:
        deque.flag = deque.next = None
        return
    while deque.next.next is not None:
        deque = deque.next
    deque.next = None


# Imprimir dados inseridos nos nós
def to_print(deque):
    print(" ------- MINHA BIBLIOTECA -------")
    if is_empty(deque):
        return False
    new_value = deque
    while new_value.next is not None:
        print("\nTitulo: %s" % new_value.next.title)
        print("Autor: %s" % new_value.next.author)
        print("Numero de paginas: %i" % new_value.next.n_pages)
        print("Preço: %.2f R$" % new_value.next.price)
        print("Categoria: %s" % new_value.next.category)
        print("Editora: %s" % new_value.next.pub_company)
        print("Ano: %i" % new_value.next.year)
        print("ID gerado: %i" % new_value.next.id)
        new_value = new_value.next


# Entrada de dados
def input_data():
    new_node = Data()
    while True:
        try:
            new_node.title = input("Titulo: ")
            new_node.author = input("Autor: ")
            new_node.n_pages = int(input("Numero de paginas: "))
            new_node.price = float(input("Preço(R$): "))
            new_node.category = input("Categoria: ")
            new_node.pub_company = input("Editora: ")
            year = input("Ano [Atual = ENTER]: ")
            if year.strip() == '':
                new_node.year = date.today().year
            else:
                new_node.year = int(year)

            new_node.id = generator_id()
            break
        except ValueError:
            print('Entre com valores corretos!')

    return new_node


# Função principal - chamada de funções
def main():
    deque = Deque()
    op = 1
    while op != 0:
        print("------------------------------------------------------------")
        print("                     BOOKS AND BOOKS")
        print("1 - Adicionar livro - [Inicio]\n2 - Adicionar livro - [Final]\n"
              "3 - Retirar livro - [Inicio]\n4 - Retirar livro - [Final]\n"
              "5 - Imprimir minha biblioteca\n0 - Sair do sistema\n")
        try:
            op = int(input("? "))
        except ValueError:
            print('Apenas numeros inteiros!')
            continue
        if op is 1:
            add_first(deque)
            print("Livro adicionado a biblioteca!")
        elif op is 2:
            add_last(deque)
            print("Livro adicionado a biblioteca!")
        elif op is 3:
            res = pop_first(deque)
            if not res:
                print("<Vazio>")
            else:
                print("Livro removido com sucesso!")
        elif op is 4:
            res = pop_last(deque)
            if not res:
                print("<Vazio>")
            else:
                print("Livro removido com sucesso!")
        elif op is 5:
            res = to_print(deque)
            if not res:
                print("<Vazio>")
        elif op is 0:
            print("Até mais!")
        else:
            print("Operação inválida!")

main()
