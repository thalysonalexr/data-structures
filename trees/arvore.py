'''
ÁRVORE BINÁRIA DE BUSCA
'''

'''
Trabalho para dia 12/04

 =|=|= *** Sistemas *** =|=|=

- Classificação de cerveja
- Cadastro de clientes
- Classificação de personagens de jogos
- Classificação de cinema
- Jogo da memória

'''


class No:
    def __init__(self, valor=None):
        self.inform = valor
        self.filho_esq = None
        self.filho_dir = None


# Sub-árvores vázias é onde será inseridos elementos
def inserir(raiz, valor):
    if raiz is None:
        raiz = No(valor)
    else:
        if valor > raiz.inform:
            raiz.filho_dir = inserir(raiz.filho_dir, valor)
        else:
            raiz.filho_esq = inserir(raiz.filho_esq, valor)

    return raiz

'''
VERIFICAR NA REMOÇÃO

* filho é folha
* filho tem filho na esquerda
* filho tem filho na direita
* filho tem filhos
'''


# def remover(raiz, valor):
#     pai = busca(raiz, valor)
#     if pai.filho_esq.inform == valor:
#         remover(raiz.filho_esq, valor)
#     else:
#         remover(raiz.filho_dir, valor)


def buscar(raiz, valor):
    if raiz is None:
        return raiz

    if raiz.filho_esq is not None:
        if raiz.filho_esq.inform == valor:
            return raiz
    if raiz.filho_dir is not None:
        if raiz.filho_dir.inform == valor:
            return raiz

    node = raiz.filho_esq if valor < raiz.inform else raiz.filho_dir

    if node is not None:
        return buscar(node, valor)
    else:
        return None


def altura(raiz):
    if raiz is None:
        return -1
    alt_esq = altura(raiz.filho_esq)
    alt_dir = altura(raiz.filho_dir)

    if alt_esq < alt_dir:
        alt_dir += 1
        return alt_dir
    else:
        alt_esq += 1
        return alt_esq


def soma(raiz):
    if raiz is None:
        return 0
    return soma(raiz.filho_esq) + soma(raiz.filho_dir) + raiz.inform


def cont(raiz):
    if raiz is None:
        return 0
    if raiz.filho_esq is None and raiz.filho_dir is None:
        return 1
    return cont(raiz.filho_esq) + cont(raiz.filho_dir) + 1


def folhas(raiz):
    if raiz is None:
        return 0
    if raiz.filho_esq is None and raiz.filho_dir is None:
        return 1
    return folhas(raiz.filho_esq) + folhas(raiz.filho_dir)

'''
Identificar o pivot e a raiz
* Rotação simples a direita
* Rotação simples a esquerda
* Rotação dupla a direita - Você obtém um sinal de menor
* Rotação dupla a esquerda - Você obtém um sinal de maior
'''


def balancear(raiz):
    pass


def imprimir_red(raiz):
    if raiz is not None:
        print(raiz.inform)
        imprimir_red(raiz.filho_esq)
        imprimir_red(raiz.filho_dir)


def imprimir_edr(raiz):
    if raiz is not None:
        imprimir_erd(raiz.filho_esq)
        imprimir_edr(raiz.filho_dir)
        print(raiz.inform)


def imprimir_erd(raiz):
    if raiz is not None:
        imprimir_edr(raiz.filho_esq)
        print(raiz.inform)
        imprimir_erd(raiz.filho_dir)


def imprimir_indentado(raiz, nivel=0):
    if raiz is None:
        return
    imprimir_indentado(raiz.filho_esq, nivel + 1)
    print('.' * nivel + str(raiz.inform))
    imprimir_indentado(raiz.filho_dir, nivel + 1)


def main():

    raiz = None

    opcao = -1

    while opcao != 0:
        print("""
        == ÁRVORE BINÁRIA DE BUSCA ==

        1 - Inserir
        2 - Remover
        3 - Imprimir RED
        4 - Imprimir EDR
        5 - Imprimir ERD
        6 - Indentado
        7 - Buscar
        8 - Altura
        9 - Soma
        10 - Contagem de nós
        11 - Contagem de folhas""")

        opcao = int(input(">> "))

        if opcao == 1:
            raiz = inserir(raiz, int(input("Insira um valor: ")))

        # elif opcao == 2:
        #     remover(raiz, int(input("Insira um valor: ")))

        elif opcao == 3:
            imprimir_red(raiz)

        elif opcao == 4:
            imprimir_edr(raiz)

        elif opcao == 5:
            imprimir_erd(raiz)

        elif opcao == 6:
            imprimir_indentado(raiz)

        elif opcao == 7:
            valor = int(input('Valor a ser procurado: '))
            pai = buscar(raiz, valor) if raiz.inform != valor else raiz
            if pai is None:
                print('Valor não encontrado.')
            elif pai.inform == valor:
                print('O valor está na raiz.')
            else:
                print('Valor encontrado. Pai: ', pai.inform)

        elif opcao == 8:
            print(altura(raiz))

        elif opcao == 9:
            print(soma(raiz))

        elif opcao == 10:
            print(cont(raiz))

        elif opcao == 11:
            print(folhas(raiz))

main()