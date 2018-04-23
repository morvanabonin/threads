# coding: utf-8

from threading import Thread

""" Faça um programa composto por duas threads: a
primeira deve exibir em ordem crescente os números
de 1 a 500; a segunda deve exibir em ordem
decrescente os números entre 500 e 1. Lembre-se: As
threads devem ser executadas concorrentemente.

"""

def asc(n):
    """Função de ordenação crescente"""

    for x in range(0, n):
        print("ASC:", x)

def desc(n):
    """Função de ordenação decrescente"""
    l = []
    for x in range(0, n):
        l.append(x)
        l.sort(reverse=True)
        for z in l:
            print("DESC:", z)


if __name__ == "__main__":
    # Criando a Thread de ordem crescente
    th_asc = Thread(target=asc, args=(5,))

    # Criando a Thread de ordem decrescente
    th_desc = Thread(target=desc, args=(5,))

    # começando a thread de ordem crescente
    th_asc.start()

    # começando a thread de ordem decrescente
    th_desc.start()

    # espera até a thread impar executar completamente
    th_asc.join()

    # espera até a thread impar executar completamente
    th_desc.join()

    # Todas as threads foram executadas
    print("Feito!")