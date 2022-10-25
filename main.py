
from AutomatoFD import AutomatoFD

if __name__ == '__main__':

    afd = AutomatoFD('ab')

    for i in range(1, 5):
        afd.criaEstado(i)
    afd.mudaEstadoInicial(1)
    afd.mudaEstadoFinal(4, True)

    afd.criaTransicao(1, 2, 'a')
    afd.criaTransicao(2, 1, 'a')
    afd.criaTransicao(3, 4, 'a')
    afd.criaTransicao(4, 3, 'a')
    afd.criaTransicao(1, 3, 'b')
    afd.criaTransicao(2, 1, 'b')
    afd.criaTransicao(3, 4, 'b')
    afd.criaTransicao(4, 2, 'b')

    print(afd)
    