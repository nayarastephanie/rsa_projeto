# modulo_b_decifrar.py

import os

print("=== MÓDULO B - DECIFRAR ===")

# 📂 Listar arquivos disponíveis (.rsa)
arquivos = [f for f in os.listdir() if f.endswith(".rsa")]

if not arquivos:
    print("❌ Nenhum arquivo .rsa encontrado.")
    exit()

print("\nArquivos disponíveis:")
for arquivo in arquivos:
    print("-", arquivo)

# Usuário escolhe o arquivo
nome_arquivo = input("\nDigite o nome do arquivo (ex: mensagem1.rsa): ")

# Entrada da chave privada
try:
    n = int(input("Digite o valor de n: "))
    d = int(input("Digite o valor de d: "))
except ValueError:
    print("❌ Erro: n e d devem ser números inteiros.")
    exit()

# Leitura do arquivo escolhido
try:
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("❌ Erro: arquivo não encontrado.")
    exit()

# Verifica se está vazio
if not conteudo.strip():
    print("❌ Erro: arquivo vazio.")
    exit()

# Converte para lista
numeros = conteudo.split()

mensagem_original = ""

# Descriptografia
for numero in numeros:
    try:
        numero = int(numero)
    except ValueError:
        print("❌ Erro: conteúdo inválido no arquivo.")
        exit()

    decifrado = pow(numero, d) % n

    try:
        mensagem_original += chr(decifrado)
    except ValueError:
        print("❌ Erro ao converter número para caractere.")
        exit()

# Exibe resultado
print("\nMensagem descriptografada:")
print(mensagem_original)

print(f"\nQuantidade de caracteres decifrados: {len(numeros)}")