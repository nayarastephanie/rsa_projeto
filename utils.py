# utils.py

import random

# Função para calcular o MDC (Máximo Divisor Comum)
def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Função para verificar se um número é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


# Função para gerar número primo aleatório
def gerar_primo():
    while True:
        numero = random.randint(100, 500)  # intervalo maior
        if eh_primo(numero):
            return numero


# Função para calcular o inverso modular (chave privada)
def calcular_inverso_modular(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d