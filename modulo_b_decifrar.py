# modulo_b_decifrar.py

print("=== MÓDULO B - DECIFRAR ===")

# Entrada da chave privada
n = int(input("Digite o valor de n: "))
d = int(input("Digite o valor de d: "))

# Leitura do arquivo .rsa
with open("mensagem.rsa", "r") as arquivo:
    conteudo = arquivo.read()

# Converte string para lista de números
numeros = conteudo.split()

mensagem_original = ""

# Percorre cada número criptografado
for numero in numeros:
    
    numero = int(numero)
    
    # Aplica a fórmula da descriptografia
    decifrado = pow(numero, d) % n
    
    # Converte número de volta para caractere
    mensagem_original += chr(decifrado)

# Exibe resultado
print("\nMensagem descriptografada:")
print(mensagem_original)