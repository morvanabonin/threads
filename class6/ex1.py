# coding: utf-8

from threading import Thread

""" Faça um programa concorrente que imprima em
uma thread os números pares e, em
outra thread, os números ímpares (até 100).

"""

def impar(n):
    """Função de aprendizado de Threads em Python"""

    for x in range(0, n):
        if x % 2:
            print("Eu sou um número impar", x)

def par(n):
    for x in range(0, n):
        if not x % 2:
            print("Eu sou um número par", x)


if __name__ == "__main__":
    # Criando a Thread Impar
    th_impar = Thread(target=impar, args=(100,))
    # começando a thread impar
    th_impar.start()

    # espera até a thread impar executar completamente
    th_impar.join()

    # Criando a Thread Par
    th_par = Thread(target=par, args=(100,))

    # começando a thread par
    th_par.start()

    # espera até a thread par executar completamente
    th_par.join()

    # Todas as threads foram executadas
    print("Feito!")

