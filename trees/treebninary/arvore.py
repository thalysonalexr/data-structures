'''
- Classificação de cinema
'''


class No:
    def __init__(self, valor=None):
        self.filme = valor
        self.alt = 0
        self.filho_esq = None
        self.filho_dir = None


# Balanceamento
def altura_no(no):
    if no is None:
        return -1
    return no.alt


def fator_balanceamento(no):
    return abs(altura_no(no.filho_esq) - altura_no(no.filho_dir))


def maior(x, y):
    if x > y:
        return x
    else:
        return y


def rotacao_simples_dir(no):
    aux = no.filho_esq
    no.filho_esq = aux.filho_dir
    aux.filho_dir = no

    no.alt = maior(altura_no(no.filho_esq), altura_no(no.filho_dir)) + 1
    aux.alt = maior(altura_no(aux.filho_esq), no.alt) + 1

    no = aux
    return no


def rotacao_simples_esq(no):
    aux = no.filho_dir
    no.filho_dir = aux.filho_esq
    aux.filho_esq = no

    no.alt = maior(altura_no(no.filho_esq), altura_no(no.filho_dir)) + 1
    aux.alt = maior(altura_no(aux.filho_dir), no.alt) + 1

    no = aux
    return no


def rotacao_dupla_dir(no):
    no = rotacao_simples_esq(no.filho_esq)
    no = rotacao_simples_dir(no)
    return no


def rotacao_dupla_esq(no):
    no = rotacao_simples_dir(no.filho_dir)
    no = rotacao_simples_esq(no)
    return no


def entrada_de_dados():
    filmes = []
    filmes.append(input('Titulo: '))
    filmes.append(input('Titulo Original: '))
    filmes.append(input('Diretor: '))
    filmes.append(input('Distribuidora: '))
    filmes.append(input('Gênero: '))
    filmes.append(int(input('Duração (Min): ')))
    filmes.append(input('Classificação: '))
    filmes.append(input('Período(Cartaz): '))
    filmes.append(input('Modalidade: '))
    filmes.append(int(input('Sessão: ')))
    filmes.append(float(input('Bilheteria (R$): ')))
    return filmes


def inserir(raiz, filme, idx):
    if raiz is None:
        raiz = No(filme)
    else:
        if filme[idx] > raiz.filme[idx]:

            raiz.filho_dir = inserir(raiz.filho_dir, filme, idx)

            if fator_balanceamento(raiz) >= 2:
                if filme[idx] > raiz.filho_dir.filme[idx]:
                    raiz = rotacao_simples_esq(raiz)
                else:
                    raiz = rotacao_dupla_esq(raiz)
        else:
            raiz.filho_esq = inserir(raiz.filho_esq, filme, idx)

            if fator_balanceamento(raiz) >= 2:
                if filme[idx] < raiz.filho_dir.filme[idx]:
                    raiz = rotacao_simples_dir(raiz)
                else:
                    raiz = rotacao_dupla_dir(raiz)

        raiz.alt = maior(altura_no(raiz.filho_esq), altura_no(raiz.filho_dir)) + 1

    return raiz


def imprimir(raiz):
    if raiz is not None:
        imprimir(raiz.filho_dir)

        aux = ['Titulo: ', 'Titulo original: ', 'Diretor: ', 'Distribuidora: ', 'Gênero: ',
               'Duração (Min): ', 'Classificação: ', 'Período: ', 'Modalidade: ', 'Sessão: ', 'Bilheteria: ']

        for i in range(len(raiz.filme)):
            print(aux[i], raiz.filme[i])

        imprimir(raiz.filho_esq)


def soma(raiz, idx):
    if raiz is None:
        return 0
    return soma(raiz.filho_esq, idx) + soma(raiz.filho_dir, idx) + raiz.filme[idx]


def cont(raiz):
    if raiz is None:
        return 0
    if raiz.filho_esq is None and raiz.filho_dir is None:
        return 1
    return cont(raiz.filho_esq) + cont(raiz.filho_dir) + 1


def main():

    raiz = None

    opcao = -1
    bilheteria = 10 # Indice da info de bilheteria, mudar aqui o para modificar a condição a ser avaliada

    while opcao != 0:
        print("""
        == CINEMA ==

        1 - Inserir filme
        2 - Imprimir
        3 - Total de bilheteria
        4 - Total de filmes
        """)

        opcao = int(input(">> "))

        if opcao == 1:
            raiz = inserir(raiz, entrada_de_dados(), bilheteria)
        elif opcao == 2:
            imprimir(raiz)
        elif opcao == 3:
            print('Total arrecadado: ', soma(raiz, bilheteria), 'R$')
        elif opcao == 4:
            print('Filmes disponíveis: ', cont(raiz))
        else:
            print('Opção inválida!')



main()