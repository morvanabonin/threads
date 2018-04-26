# coding: utf-8

import time

# from Tkinter import *
from mttkinter import *
from threading import Thread


""" Crie uma aplicação que apresenta numa tela 3 relógios digitais, que mostre inclusive os segundos.
Cada relógio inicia com 0 e a cada segundo se atualiza.
Adicione a opção para o usuário poder configurar alarmes (definidos por
um horário) para cada relógio. Quando chegar no horário do alarme, 
um alerta é disparado.

"""

root = Tk()
# time1 = ''

clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock2 = Label(root, font=('times', 20, 'bold'), bg='red')
clock3 = Label(root, font=('times', 20, 'bold'), bg='blue')
clock.pack(fill=BOTH, expand=1)
clock2.pack(fill=BOTH, expand=1)
clock3.pack(fill=BOTH, expand=1)


def timer():
    time1 = ''
    # pega a hora local e atual do pc
    time2 = time.strftime('%H:%M:%S')
    # Se a cadeia de tempo foi alterada, atualiza
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # chama a si mesmo a cada 200 millisegundos
    # para atualizar o display
    clock.after(200, timer)


def timer2():
    time1 = ''
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock2.config(text=time2)
    clock2.after(200, timer2)


def timer3():
    time1 = ''
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock3.config(text=time2)
    clock3.after(200, timer3)


if __name__ == "__main__":
    # timer()
    # timer2()
    # timer3()

    # Criando a Thread Timer
    th_timer = Thread(target=timer)
    # começando a thread timer
    th_timer.start()

    # espera até a thread timer
    th_timer.join()
    # root.mainloop()
