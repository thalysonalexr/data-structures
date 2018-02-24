'''

FILA AMERICANAS -

Compact static row if required
(Fila estatica compactada se necessario)

'''

__author__ = "Thalyson A. R. Sousa"
__Date__ = "26/12/2016"


class Client(object):
    def __init__(self, name=None, rg=None, cpf=None, birth=None, email=None, address=None):
        self.name = name
        self.cpf = cpf
        self.rg = rg
        self.birth = birth
        self.email = email
        self.address = address
        self.id = 0


# Variaveis globais
FIRST = -1
LAST = -1
ID_GLOBAL = 0


# Verifica se todos espacos da lista estão vazios
def is_empty(row):
    global FIRST
    return row[FIRST].name is None  # Utiliza a propriedade name como referencia para verificacao


# Verifica se esta cheia
def isnt_full(row):
    global FIRST, LAST
    return FIRST > 0 or LAST < len(row) - 1


def generator_id():
    global ID_GLOBAL
    ID_GLOBAL += 1
    return ID_GLOBAL


def compact(row):
    global FIRST, LAST
    var_next = 0
    for i in range(FIRST, len(row)):
        row[var_next] = row[i]           # Posicao INICIO da lista recebe o valor encontrado
        var_next += 1                    # Passo para proxima posicao a ser alterada

    # Definir novo INICIO e FIM da lista
    LAST -= FIRST
    FIRST = 0

    # Apagar dados repetidos
    i -= 1

    row[-1] = Client()
    for i in range(i, 0, -1):
        if row[i].name is None or i is LAST:
            return
        row[i] = Client()


def input_data(i, row):
    row[i].name = input("Nome: ")
    row[i].rg = input("RG/SSP: ")
    row[i].cpf = input("CPF: ")
    row[i].birth = input("Data nasc: ")
    row[i].email = input("E-mail: ")
    row[i].andress = input("Endereco(Rua, nº): ")
    row[i].id += generator_id()


def insert_client(row):
    global FIRST, LAST
    if isnt_full(row):  # Se a lista nao estiver cheia
        if row[-1].name is not None:  # Se a ultima posição da lista estiver ocupada COMPACTA
            compact(row)
        if is_empty(row):  # Se lista vazia, insere no inicio
            FIRST = LAST = 0
            input_data(FIRST, row)
        else:  # Insere dados nos proximos campos vazios
            LAST += 1
            input_data(LAST, row)
    else:
        print("\nFila cheia...\n")


def remove_client(row):
    global FIRST, LAST
    if is_empty(row):
        print("\nFila vazia...\n")
        return
    elif FIRST is LAST:  # Tem apenas um dado na lista, remove este entao
        print("\nCliente ", row[FIRST].name, " atendido(a)! Proximo...")
        row[FIRST] = Client()
        FIRST = LAST = -1  # Passam a "apontar" para lugar vazio
    else:
        print("\nCliente ", row[FIRST].name, " atendido(a)! Proximo...\n")
        row[FIRST] = Client()  # Remove e INICIO passa a ser o proximo
        FIRST += 1


def to_print(row):
    if is_empty(row):
        print("\nFila vazia...\n")
        return
    for i in range(len(row)):
        if row[i].name is not None:
            print("\nPOSIÇAO --- [", i+1, "] ---")
            print("Nome: ", row[i].name)
            print("RG/SSP: ", row[i].rg)
            print("CPF:", row[i].cpf)
            print("Data nasc: ", row[i].birth)
            print("E-mail", row[i].email)
            print("Endereco(Rua, nº): ", row[i].andress)
            print("ID: ", row[i].id, "\n")


def main():
    row = [Client(), Client(), Client(), Client(), Client()]
    operation = 0
    while operation != 4:
        print("<<<     MENU    >>>\n\n1 - Inserir novo\n2 - Visualizar fila\n3"
              " - Remover cliente atendido\n4 - Sair do sistema")
        operation = int(input("? "))
        if operation == 1:
            insert_client(row)
        elif operation == 2:
            to_print(row)
        elif operation == 3:
            remove_client(row)
        elif operation == 4:
            print("Ate a proxima...")
        else:
            print("Opcao invalida...")

main()
