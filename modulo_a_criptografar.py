# modulo_a_criptografar.py

print("=== MÓDULO A - CRIPTOGRAFAR ===")

# Entrada de dados
mensagem = input("Digite a mensagem: ")
n = int(input("Digite o valor de n: "))
e = int(input("Digite o valor de e: "))

mensagem_criptografada = []

# Percorre cada caractere da mensagem
for caractere in mensagem:
    
    # Converte caractere para número usando ASCII
    numero = ord(caractere)
    
    # Aplica a fórmula da criptografia
    cifrado = pow(numero, e) % n
    
    # Armazena o valor criptografado
    mensagem_criptografada.append(cifrado)

# Exibe resultado
print("\nMensagem criptografada:")
print(mensagem_criptografada)

# Salva em arquivo .rsa
with open("mensagem.rsa", "w") as arquivo:
    for numero in mensagem_criptografada:
        arquivo.write(str(numero) + " ")

print("\nArquivo 'mensagem.rsa' gerado com sucesso!")