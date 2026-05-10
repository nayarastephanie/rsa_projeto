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
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    # Itera apenas até sqrt(numero) - muito mais rápido
    for i in range(3, int(numero**0.5) + 1, 2):
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
    return None


# Função para carregar chaves de arquivo
def carregar_chaves():
    import json
    try:
        with open("chaves.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


# Função para validar se n e d formam um par válido
def validar_par_descriptografia(n, d):
    """
    Retorna um dicionário com informações sobre a validade do par (n, d)
    """
    erros = []
    
    if n < 128:
        erros.append(f"❌ n={n} é muito pequeno (deve ser >= 128)")
    
    if d <= 0:
        erros.append(f"❌ d={d} deve ser positivo")
    
    if d > n:
        erros.append(f"⚠️  d={d} > n={n} (pode estar incorreto)")
    
    return {"valido": len(erros) == 0, "erros": erros}