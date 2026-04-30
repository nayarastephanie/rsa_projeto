# modulo_a_criptografar.py

import os

print("=== MÓDULO A - CRIPTOGRAFAR ===")

# Entrada da mensagem
mensagem = input("Digite a mensagem: ")

if not mensagem:
    print("❌ Erro: a mensagem não pode estar vazia.")
    exit()

# Entrada da chave pública
try:
    n = int(input("Digite o valor de n: "))
    e = int(input("Digite o valor de e: "))
except ValueError:
    print("❌ Erro: n e e devem ser números inteiros.")
    exit()

mensagem_criptografada = []

# Validação do tamanho de n
for caractere in mensagem:
    if ord(caractere) >= n:
        print("❌ Erro: n é muito pequeno para os caracteres da mensagem.")
        print("👉 Gere chaves maiores.")
        exit()

# Criptografia
for caractere in mensagem:
    
    numero = ord(caractere)
    
    cifrado = pow(numero, e) % n
    
    mensagem_criptografada.append(cifrado)

# Exibe resultado
print("\nMensagem criptografada:")
print(mensagem_criptografada)

print(f"\nQuantidade de caracteres criptografados: {len(mensagem_criptografada)}")



contador = 1

# Procura um nome disponível
while os.path.exists(f"mensagem{contador}.rsa"):
    contador += 1

nome_arquivo = f"mensagem{contador}.rsa"

# Salva em arquivo .rsa
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(" ".join(map(str, mensagem_criptografada)))

print(f"\nArquivo '{nome_arquivo}' gerado com sucesso!")